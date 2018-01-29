#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2018/1/29 16:41
"""

import pymongo

import pandas as pd


def deal(db, table_name):
    tb_qtum = db[table_name]
    df = pd.DataFrame(list(tb_qtum.find()))
    s = df['token']
    s.to_csv("%s.csv" % table_name, index=False)


if __name__ == '__main__':
    client = pymongo.MongoClient("127.0.0.1", 27017)
    db = client["etherscan_token2"]
    deal(db, "tb_bnb")
    deal(db, "tb_eos")
    deal(db, "tb_omg")
    deal(db, "tb_qtm")
    deal(db, "tb_snt")
    deal(db, "tb_trx")
    deal(db, "tb_zrx")
