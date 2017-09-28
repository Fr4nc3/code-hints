"""
Fr4nc3
10/18/2016

implements  Runnable, FastStocksCSVReader
"""

import csv
import os
import os.path
import queue
import threading

# Global variables
stocks_rows = queue.Queue()
stocks_records = queue.Queue()

baseball_rows = queue.Queue()
baseball_records = queue.Queue()


# HW6
class Runnable:
    def __call__(self, *args, **kwargs):
        global stocks_rows, stocks_records
        while True:
            try:
                row = stocks_rows.get(False)
                print("{worker_id} working hard!!".format(worker_id=id(self)))
                # if these fields come empty ignore the row
                if not row["ticker"]:
                    pass
                if not row["exchange_country"]:
                    pass
                if row["company_name"]:
                    pass
                # if cannot convert the values ignore the row
                try:
                    price = float(row["price"])
                except ValueError:
                    pass
                try:
                    exchange_rate = float(row["exchange_rate"])
                except ValueError:
                    pass
                try:
                    shares_outstanding = float(row["shares_outstanding"])
                except ValueError:
                    pass
                try:
                    net_income = float(row["net_income"])
                except ValueError:
                    pass
                try:
                    pe_ratio = (price * shares_outstanding) / net_income
                except ZeroDivisionError:
                    pass

                # at this point all the variables are validated
                market_value_usd = price * exchange_rate * shares_outstanding
                # ready to put on the queue
                stocks_records.put(
                    StockStatRecord(name=row["ticker"], exchange_country=row["exchange_country"], price=price,
                                    exchange_rate=exchange_rate, shares_outstanding=shares_outstanding,
                                    net_income=net_income, market_value_usd=market_value_usd,
                                    pe_ratio=pe_ratio, company_name=row["company_name"]), timeout=1)
            except queue.Empty:  # if the queue is empty break the loop
                break


class FastStocksCSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        """
        :return: list of records
        """
        # local variables used in load
        record_list = []
        threads = []
        # globals variables
        global stocks_rows, stocks_records
        try:
            with open(self.file_path) as file:
                try:
                    reader = csv.DictReader(file)
                    for row in reader:
                        stocks_rows.put(row)
                except csv.Error as e:  # this just will let the system known that there was an error in csv
                    print("Error to load csv error message {}".format(e))
        except IOError:  # this will let the system known that the file wasn't  open
            print("Error to open file {}".format(self.file_path))

        for num in range(4):
            # print(num)
            new_thread = threading.Thread(target=Runnable())
            new_thread.start()
            threads.append(new_thread)

        for t in threads:  # each thread in the threads list
            t.join()

        while True:  # populate the record_list from queue
            if not stocks_records.empty():
                record_list.append(stocks_records.get())
            else:
                break
        return record_list


#####################################
# this is the Baseball implementation
#####################################
class FastBaseBallCSVReader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        """
        :return: list of records
        """
        record_list = []
        threads = []
        global stocks_rows, stocks_records
        try:
            with open(self.file_path) as file:
                try:
                    reader = csv.DictReader(file)
                    for row in reader:
                        baseball_rows.put(row)
                except csv.Error as e:  # this just will let the system known that there was an error in csv
                    print("Error to load csv error message {}".format(e))
        except IOError:  # this will let the system known that the file wasn't  open
            print("Error to open file {}".format(self.file_path))

        for num in range(4):
            # print(num)
            new_thread = threading.Thread(target=RunnableBaseBall())
            new_thread.start()
            threads.append(new_thread)

        for t in threads:  # each thread in the threads list
            t.join()

        while True:
            if not baseball_records.empty():
                record_list.append(baseball_records.get())
            else:
                break
        return record_list


class RunnableBaseBall:
    def __call__(self, *args, **kwargs):
        global baseball_rows, baseball_records
        while True:
            try:  # if the queue is not empty we get one element
                row = baseball_rows.get(False)
                print("{worker_id} working hard from baseball!!".format(worker_id=id(self)))
                if not row["PLAYER"]:  # if player row is empty
                    pass
                # try to convert if fails skip the row
                try:
                    salary = float(row["SALARY"])
                except ValueError:
                    pass
                try:
                    game = int(row["G"])
                except ValueError:
                    pass
                try:
                    avg = float(row["AVG"])
                except ValueError:
                    pass

                # at this point all the variables are validated add to the queue
                baseball_records.put(BaseballStatRecord(name=row["PLAYER"], salary=salary, game=game, avg=avg),
                                     timeout=1)
            except queue.Empty:  # if the queue is Empty break the loop
                break


########################################
# FROM HW4
########################################

class AbstractRecord:
    def __init__(self, name):
        self.name = name


class StockStatRecord(AbstractRecord):
    def __init__(self, name, exchange_country, price, exchange_rate, shares_outstanding, net_income, market_value_usd,
                 pe_ratio, company_name):
        """
        :param name: string
        :param exchange_country: string
        :param price: float
        :param exchange_rate: float
        :param shares_outstanding: float
        :param net_income: float
        :param market_value_usd: float
        :param pe_ratio: float
        :name is sent to parent init to set it there
        """
        super().__init__(name)
        self.exchange_country = exchange_country
        self.price = price
        self.exchange_rate = exchange_rate
        self.shares_outstanding = shares_outstanding
        self.net_income = net_income
        self.market_value_usd = market_value_usd
        self.pe_ratio = pe_ratio
        self.company_name = company_name

    def __str__(self):
        return ("{name} ({company_name}, {exchange_country}, {price:.2f}, {exchange_rate:.2f}, "
                "{shares_outstanding:.2f}, {net_income:.2f}, "
                "{market_value_usd:.2f}, {pe_ratio:.2f})").format(name=self.name,
                                                                  exchange_country=self.exchange_country,
                                                                  price=self.price,
                                                                  exchange_rate=self.exchange_rate,
                                                                  shares_outstanding=self.shares_outstanding,
                                                                  net_income=self.net_income,
                                                                  market_value_usd=self.market_value_usd,
                                                                  pe_ratio=self.pe_ratio,
                                                                  company_name=self.company_name)


class BaseballStatRecord(AbstractRecord):
    def __init__(self, name, salary, game, avg):
        """
        :param name: string
        :param salary: float
        :param game: int
        :param avg: float
        name is sent to parent init to set it there
        """
        super().__init__(name)
        self.salary = salary
        self.game = game
        self.game = game
        self.avg = avg

    def __str__(self):
        return "{name} ({salary:.2f}, {game:.0f}, {avg:.2f})".format(name=self.name, salary=self.salary, game=self.game,
                                                                     avg=self.avg)


# end HW4
# this method only used for test
def file_exist(file_path):
    """
    This method
    :param file_path:
    :return:
    True or False
    """
    return os.path.isfile(file_path) and os.access(file_path, os.R_OK)


# Test HW6
if __name__ == '__main__':
    # help to test HW6
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

    # HW6 Main
    stocks_list = FastStocksCSVReader(file_path_stock).load()
    baseball_list = FastBaseBallCSVReader(file_path_baseball).load()
    for record in stocks_list:
        print(record)
    for record in baseball_list:
        print(record)
