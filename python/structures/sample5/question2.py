"""
Fr4nc3
10/10/2016

implements DAO, StockStatsDAO, BaseballStatsDAO
"""

import sqlite3
import collections

# import classes from My hw4
from Riesco_Francia_Assignment4 import BaseballCSVReader, StocksCSVReader, file_exist, BaseballStatRecord, StockStatRecord


class AbstractDAO:
    def __init__(self, db_name=""):
        """
        :param db_name:
        :return:
        """
        self.db_name = db_name

    def insert_records(self, records):
        """
        This is not implemented on the abstract class
        :param records:
        :return: raise error
        """
        raise NotImplementedError()

    def select_all(self):
        """
        This is not implemented on the abstract class
        :param:
        :return: raise error
        """
        raise NotImplementedError()

    def connect(self):
        """
        :return: sqlite.connect
        """
        return sqlite3.connect(self.db_name)


class BaseballStatsDAO(AbstractDAO):
    def __init__(self, db_name):
        """
        :param db_name: file path or file name we don't check if exist
        call init from parent and pass the db_name
        """
        super().__init__(db_name)

    def insert_records(self, records):
        """
        :param records: list of BaseBallStatRecord  records
        :return: void
        """
        conn = self.connect()
        cursor = conn.cursor()
        for rec in records:
            try:
                # baseball_stats (player_name,game_played,average,salary)
                cursor.execute("INSERT INTO baseball_stats VALUES (?,?,?,?)", (rec.name, rec.g,
                                                                               rec.avg, rec.salary))
            except sqlite3.DatabaseError:  # avoid a sql error
                # print('Database Error')
                pass
        conn.commit()
        conn.close()

    def select_all(self):
        """
        :return: deque collection of BaseBallStatRecord records
        """
        deque = collections.deque()
        conn = self.connect()
        cursor = conn.cursor()

        cursor.execute("SELECT player_name,game_played,average,salary FROM baseball_stats")
        for row in cursor.fetchall():
            deque.append(BaseballStatRecord(name=row[0], g=row[1], avg=row[2], salary=row[3]))
        conn.close()
        return deque


class StockStatsDAO(AbstractDAO):
    def __init__(self, db_name):
        """
        :param db_name: file path or file name we don't check if exist
        call init from parent and pass the db_name
        """
        super().__init__(db_name)

    def insert_records(self, records):
        conn = self.connect()
        cursor = conn.cursor()

        for rec in records:
            # company_name,ticker,exchange_country,price,exchange_rate,shares_outstanding,
            # net_income,market_value_usd,pe_ratio
            try:
                cursor.execute("INSERT INTO stock_stats VALUES(?,?,?,?,?,?,?,?,?)", (
                    rec.company_name, rec.name, rec.exchange_country, rec.price, rec.exchange_rate,
                    rec.shares_outstanding, rec.net_income, rec.market_value_usd, rec.pe_ratio))
            except sqlite3.DatabaseError:  # avoid sql error
                # print('Database Error')
                pass

        conn.commit()
        conn.close()

    def select_all(self):
        """
        :return: deque collection of StockStatRecord records
        """
        deque = collections.deque()
        conn = self.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT company_name,ticker,country,price,exchange_rate,"
                       "shares_outstanding,net_income,market_value,pe_ratio FROM stock_stats")
        for row in cursor.fetchall():
            deque.append(StockStatRecord(company_name=row[0], name=row[1], exchange_country=row[2], price=row[3],
                                         exchange_rate=row[4], shares_outstanding=row[5],
                                         net_income=row[6], market_value_usd=row[7],
                                         pe_ratio=row[8]))

        conn.close()
        return deque


# Test HW5
if __name__ == '__main__':

    # This part of the code is for help o test the hw4/hw5
    question = "The name of {}  or empty string to use {} : "
    default_baseball_file = "MLB2008.csv"
    default_stock_file = "StockValuations.csv"
    file_path_baseball = input(question.format("baseball csv file", default_baseball_file))
    if not file_path_baseball or not file_exist(file_path_baseball):
        file_path_baseball = default_baseball_file  # give a default name assuming the file is in the same folder

    file_path_stock = input(question.format("Stock csv file", default_stock_file))
    if not file_path_stock or not file_exist(file_path_stock):
        file_path_stock = default_stock_file  # give a default name assuming the file is in the same folder

    if not file_exist(file_path_baseball) or not file_exist(file_path_stock):
        exit("Missing files")  # stop if the files are missing

    # load the files
    b = BaseballCSVReader(file_path_baseball).load()
    s = StocksCSVReader(file_path_stock).load()

    b_dao = BaseballStatsDAO("baseball.db")
    b_dao.insert_records(b)
    b_deque = b_dao.select_all()

    s_dao = StockStatsDAO("stocks.db")
    s_dao.insert_records(s)
    s_deque = s_dao.select_all()

    s_dict = {}
    for record in s_deque:
        if record.exchange_country in s_dict:
            s_dict[record.exchange_country] += 1
        else:
            s_dict[record.exchange_country] = 1

    for k, v in s_dict.items():
        print("exchange country: {k} has {v} tickers".format(k=k, v=v))

    b_dict = {}
    for record in b_deque:
        avg = round(record.avg, 3)
        if avg in b_dict:
            b_dict[avg].append(record.salary)
        else:
            b_dict[avg] = [record.salary]  # first element/salary of the list

    for k, v in b_dict.items():
        salary = sum(v) / len(v) if len(v) > 0 else 0  # avoid divide by zero
        print("avg {k} salary avg {salary:.2f}".format(k=k, salary=salary))

    # test only to clean the table at the end
    # b_conn = b_dao.connect()
    # b_cursor = b_conn.cursor()
    # b_cursor.execute("DELETE FROM baseball_stats")
    # b_conn.commit()
    # b_conn.close()
    #
    # s_conn = s_dao.connect()
    # s_cursor = s_conn.cursor()
    # s_cursor.execute("DELETE FROM stock_stats")
    # s_conn.commit()
    # s_conn.close()
