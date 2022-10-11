import argparse
from typing import Any, Dict, Tuple, Union

import pytorch_lightning as pl
import torch
from torchmetrics import Accuracy

OPTIMIZER = "Adam"
LOSS = "binary_cross_entropy"  # model의 최종 out이 sigmoid를 거침
LR = 0.001


class NCFLitModel(pl.LightningModule):
    def __init__(self, model, args: argparse.Namespace = None):
        """_summary_

        Parameters
        ----------
        model : _type_
            NCF model
        args : argparse.Namespace, optional
            _description_, by default None
        """
        super().__init__()
        self.model = model
        self.args = vars(args) if args is not None else {}

        optimizer = self.args.get("optimizer", OPTIMIZER)
        self.optimizer = getattr(torch.optim, optimizer)

        self.lr = self.args.get("lr", LR)

        loss = self.args.get("loss", LOSS)
        self.loss_fn = getattr(torch.nn.functional, loss)

        self.train_acc = Accuracy()
        self.val_acc = Accuracy()
        self.test_acc = Accuracy()

    # @staticmethod
    # def add_to_argparse(parser):
    #     parser.add_argument(
    #         "--optimizer",
    #         type=str,
    #         default=OPTIMIZER,
    #         help="optimizer class from torch.optim",
    #     )
    #     parser.add_argument("--lr", type=float, default=LR)
    #     parser.add_argument("--one_cycle_max_lr", type=float, default=None)
    #     parser.add_argument(
    #         "--loss",
    #         type=str,
    #         default=LOSS,
    #         help="loss function from torch.nn.functional",
    #     )
    #     return parser

    def configure_optimizers(self) -> Dict[str, Any]:
        """set optimizer

        Returns
        -------
        Dict[str, Any]
            opimizer, validation loss
        """
        optimizer = self.optimizer(self.model.parameters(), lr=self.lr)
        # if self.one_cycle_max_lr is None:
        #     return optimizer
        # scheduler = torch.optim.lr_scheduler.OneCycleLR(
        #     optimizer=optimizer,
        #     max_lr=self.one_cycle_max_lr,
        #     total_steps=self.one_cycle_total_steps,
        # )
        return {
            "optimizer": optimizer,
            # "lr_scheduler": scheduler,
            "monitor": "validation/loss",
        }

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.model(x)

    def predict(self, x: torch.Tensor) -> torch.Tensor:
        logits = self.model(x)
        return logits

    def _run_on_batch(
        self, batch: Tuple[torch.Tensor, torch.Tensor], with_preds: bool = False
    ) -> Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]:
        """batch train

        Parameters
        ----------
        batch : Tuple[torch.Tensor, torch.Tensor]
            batch data
        with_preds : bool, optional
            _description_, by default False

        Returns
        -------
        Tuple[torch.Tensor, torch.Tensor, torch.Tensor, torch.Tensor]
            x, y, logits, loss
        """
        x, y = batch
        logits = self(x)
        loss = self.loss_fn(logits, y)

        return x, y, logits, loss

    def training_step(
        self, batch: Tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> Dict[str, torch.Tensor]:
        """training step

        Parameters
        ----------
        batch : Tuple[torch.Tensor, torch.Tensor]
            batch data
        batch_idx : int
            batch index

        Returns
        -------
        Dict[str, torch.Tensor]
            {"loss": loss}
        """
        x, y, logits, loss = self._run_on_batch(batch)
        self.train_acc(logits, y)

        self.log("train/loss", loss)
        self.log("train/acc", self.train_acc, on_step=False, on_epoch=True)

        return {"loss": loss}

    def validation_step(
        self, batch: Tuple[torch.Tensor, torch.Tensor], batch_idx: int
    ) -> Dict[str, torch.Tensor]:
        """validation step

        Parameters
        ----------
        batch : Tuple[torch.Tensor, torch.Tensor]
            batch data
        batch_idx : int
            batch index

        Returns
        -------
        Dict[str, torch.Tensor]
            {"loss": loss}
        """
        x, y, logits, loss = self._run_on_batch(batch)
        self.val_acc(logits, y)

        self.log("validation/loss", loss, prog_bar=True, sync_dist=True)
        self.log(
            "validation/acc", self.val_acc, on_step=False, on_epoch=True, prog_bar=True
        )

        return {"loss": loss}

    def test_step(self, batch: Tuple[torch.Tensor, torch.Tensor], batch_idx: int):
        """test step

        Parameters
        ----------
        batch : Tuple[torch.Tensor, torch.Tensor]
            batch data
        batch_idx : int
            batch index
        """
        x, y, logits, loss = self._run_on_batch(batch)
        self.test_acc(logits, y)

        self.log("test/loss", loss, on_step=False, on_epoch=True)
        self.log("test/acc", self.test_acc, on_step=False, on_epoch=True)
