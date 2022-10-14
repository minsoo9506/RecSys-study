import argparse
from typing import List
import numpy as np
import pandas as pd
import pytorch_lightning as pl
import torch
from torch.utils.data import DataLoader
from src.dataload.load_data import NCFDataset, NCFMakeData
from src.lit_model.NCF_lit_model import NCFLitModel
from src.model import NeuralMatrixFactorization


def define_argparser():
    parser = argparse.ArgumentParser()

    parser.add_argument("--project", default="NCF")
    parser.add_argument(
        "--batch_size",
        type=int,
        default=16,
        help="input batch size for training (default: 16)",
    )
    parser.add_argument(
        "--gmf_emb_dim",
        type=int,
        default=16,
        help="input GMF embedding dimension for training (default: 16)",
    )
    parser.add_argument(
        "--mlp_emb_dim",
        type=int,
        default=16,
        help="input MLP embedding dimension for training (default: 16)",
    )
    parser.add_argument(
        "--mlp_hidden_dims_list",
        type=List[int],
        default=[32, 16],
        help="MLP hidden layer dimension list (default: [32, 6])",
    )
    parser.add_argument(
        "--epochs", type=int, default=10, help="number of epochs to train (default: 10)"
    )
    parser.add_argument("--cuda", type=int, default=0, help="0 for cpu -1 for all gpu")
    config = parser.parse_args()
    if config.cuda == 0 or torch.cuda.is_available() == False:
        config.cuda = 0

    return config


def main(config):
    # data
    data_path = "./data/kmrd/kmr_dataset/datafile/kmrd-small"
    data_class = NCFMakeData(data_path)
    X_train, y_train = data_class.generate_train_df()
    X_valid, y_valid = data_class.generate_valid_df()

    train_dataset = NCFDataset(X_train, y_train)
    valid_dataset = NCFDataset(X_valid, y_valid)

    train_loader = DataLoader(train_dataset, batch_size=config.batch_size)
    valid_loader = DataLoader(valid_dataset, batch_size=config.batch_size)
    test_loader = DataLoader(test_dataset, batch_size=config.batch_size)

    # model
    if config.model == "LitBaseAutoEncoder":
        model = LitBaseAutoEncoder(n_layers=2, features_list=[8, 4, 2])
    if config.model == "LitBaseVAE":
        model = LitBaseVAE()

    # trainer
    logger = pl.loggers.WandbLogger()
    early_stopping_callback = pl.callbacks.EarlyStopping(
        monitor="val_loss", mode="min", patience=20
    )
    trainer = pl.Trainer(
        logger=logger,
        log_every_n_steps=10,  # set the logging frequency
        gpus=config.cuda,  # use all GPUs
        max_epochs=config.epochs,  # number of epochs
        deterministic=True,  # keep it deterministic
        callbacks=[early_stopping_callback],
    )

    # fit the model
    trainer.fit(model, train_loader, valid_loader)

    # error
    ############
    # # validate
    # trainer.validate(valid_loader)

    # # test
    # trainer.test(test_loader)

    # inference
    # result = trainer.predict(test_loader)
    # print(result.shape)
    #############


if __name__ == "__main__":
    config = define_argparser()
    main(config)
