"""
Fr4nc3
10/10/2016
file: create_dbs.py
This script create dbs for
"""

import sqlite3


def create_db(db_name, sql_table, table_name):
    """
    :param db_name:
    :param sql_table:
    :return:
    """
    conn = sqlite3.connect('{}.db'.format(db_name))
    c = conn.cursor()
    # drop the table if exist
    c.execute("DROP TABLE IF EXISTS {0}".format(table_name))
    c.execute(sql_table)
    conn.commit()
    conn.close()


if __name__ == '__main__':
    # Create baseball_stats
    baseball_table = ("CREATE TABLE baseball_stats (player_name TEXT,game_played REAL,average REAL,salary REAL)")
    create_db("baseball", baseball_table, "baseball_stats")

    # Create stock_stats
    stocks_table = ("CREATE TABLE stock_stats (company_name TEXT,ticker TEXT,country TEXT,price  REAL,"
                    "exchange_rate REAL,shares_outstanding REAL,net_income REAL,market_value REAL,pe_ratio REAL)")
    create_db("stocks", stocks_table, "stock_stats")
