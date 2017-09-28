"""
Fr4nc3
10/03/2016
Fr4nc3
This program implement  AbstractRecord and more !
"""
import csv
import os
import os.path


class AbstractRecord:
    def __init__(self, name=""):
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
    def __init__(self, name, salary, g, avg):
        """
        :param name: string
        :param salary: float
        :param g: int
        :param avg: float
        name is sent to parent init to set it there
        """
        super().__init__(name)
        self.salary = salary
        self.g = g
        self.avg = avg

    def __str__(self):
        return "{name} ({salary:.2f}, {g:.0f}, {avg:.2f})".format(name=self.name, salary=self.salary, g=self.g,
                                                                  avg=self.avg)


class AbstractCSVReader:
    def __init__(self, file_path=""):
        """
        :param file_path: file path or file name we don't check if exist
        :return:
        """
        self.file_path = file_path

    def row_to_record(self, row):
        """
        This is not implemented on the abstract class
        :param row:
        :return: raise error
        """
        raise NotImplementedError()

    def load(self):
        """
        :return: list of records
        """
        record_list = []
        try:
            with open(self.file_path) as file:
                try:
                    reader = csv.DictReader(file)
                    for row in reader:
                        try:
                            record_list.append(self.row_to_record(row))
                        except BadDataException:  # this will come from row_to_record error
                            pass
                        except NotImplementedError:  # this is a reminder if somebody implement the abstract class
                            print("You are using the abstract class!")
                            pass
                        except:  # Unexpected error
                            pass
                except csv.Error as e:  # this just will let the system known that there was an error in csv
                    print("Error to load csv return empty list error message {}".format(e))
        except IOError:  # this will let the system known that the file wasn't  open
            print("Error to open file {} return empty list".format(self.file_path))
        return record_list


class BaseballCSVReader(AbstractCSVReader):
    def __init__(self, file_path):
        super().__init__(file_path)

    def row_to_record(self, row):
        """
        This method
        :param row dictionary
        :return:
        return BaseballStatRecord
        """
        if not row["PLAYER"] or not row["SALARY"] or not row["G"] or not row["AVG"]:
            # if any of the fields are empty or null raise error
            raise BadDataException
        # convert the string to float or int raise error if it fails
        try:
            salary = float(row["SALARY"])
        except ValueError:
            raise BadDataException
        try:
            g = int(row["G"])
        except ValueError:
            raise BadDataException
        try:
            avg = float(row["AVG"])
        except ValueError:
            raise BadDataException
        # at this point all the variables are validated
        return BaseballStatRecord(name=row["PLAYER"], salary=salary, g=g, avg=avg)


class StocksCSVReader(AbstractCSVReader):
    def __init__(self, file_path):
        """
        :param file_path: file path or file name we don't check if exist
        call init from parent and pass the file_path
        """
        super().__init__(file_path)

    def row_to_record(self, row):
        """
        This method
        :param row dictionary
        :return:
        return StockStatRecord
        """
        if not row["ticker"] or not row["exchange_country"] or not row["price"] or not row["exchange_rate"] \
                or not row["shares_outstanding"] or not row["net_income"] or not row["company_name"]:
            # if any of the fields are empty or null raise error
            raise BadDataException
        # convert the string to float  raise error if it fails
        try:
            price = float(row["price"])
        except ValueError:
            raise BadDataException
        try:
            exchange_rate = float(row["exchange_rate"])
        except ValueError:
            raise BadDataException
        try:
            shares_outstanding = float(row["shares_outstanding"])
        except ValueError:
            raise BadDataException
        try:
            net_income = float(row["net_income"])
        except ValueError:
            raise BadDataException
        try:
            pe_ratio = (price * shares_outstanding) / net_income
        except ZeroDivisionError:
            raise BadDataException
        # at this point all the variables are validated
        market_value_usd = price * exchange_rate * shares_outstanding
        return StockStatRecord(name=row["ticker"], exchange_country=row["exchange_country"], price=price,
                               exchange_rate=exchange_rate, shares_outstanding=shares_outstanding,
                               net_income=net_income, market_value_usd=market_value_usd,
                               pe_ratio=pe_ratio, company_name=row["company_name"])


class BadDataException(Exception):
    """ Convert dict csv to record error handle"""

    def __init__(self):
        pass


def file_exist(file_path):
    """
    This method
    :param file_path:
    :return:
    True or False
    """
    return os.path.isfile(file_path) and os.access(file_path, os.R_OK)

