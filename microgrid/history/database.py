import pandas as pd

class Database:

    _inputs_ = ['Year', 'Month', 'Day', 'Hour', 'Minutes', 'Seconds', 'IsoDayOfWeek', 'IsoWeekNumber']
    _output_ = ['Price', 'EPV', 'C1', 'C2', 'C3'] # TODO Should be function of the CSV data

    def __init__(self, path_to_csv):
        """
        A Database objects holds the realized data of the microgrid in a pandas dataframe.

        The CSV file values are separated by ';' and the first line must contain series names.
        It must contain a 'DateTime' column with values interpretable as python date time objects.

        Some new columns are generated from the DateTime column to indicate e.g. whether
        a datetime corresponds to a day of the week or not.

        :param path_to_csv: Path to csv containing realized data
        """
        self.data_frame = self.read_data(path_to_csv)

    def read_data(self, path):
        """
        Read data and generate new columns based on the DateTime column.

        :param path: Path to the csv data file
        :return: A pandas dataframe
        """
        df = pd.read_csv(path, sep=";", parse_dates=True, index_col='DateTime')

        df['Year'] = df.index.map(lambda x: x.year)
        df['Month'] = df.index.map(lambda x: x.month)
        df['Day'] = df.index.map(lambda x: x.day)
        df['Hour'] = df.index.map(lambda x: x.hour)
        df['Minutes'] = df.index.map(lambda x: x.minute)
        df['Seconds'] = df.index.map(lambda x: x.second)
        df['IsoDayOfWeek'] = df.index.map(lambda x: x.isoweekday())
        df['IsoWeekNumber'] = df.index.map(lambda x: x.isocalendar()[1])

        return df

    def get_columns(self, column_indexer, time_indexer):
        """

        :param column_indexer: The name of a column
        :param time_indexer: A datetime
        :return: The realized value of the series column_indexer at time time_indexer
        """
        return self.data_frame[column_indexer].get(time_indexer)

    def get_column(self, column_indexer, dt_from, dt_to):
        """

        :param column_indexer: The name of a column
        :param dt_from: A start datetime
        :param dt_to: An end datetime
        :return: A list of values of the column_indexer series between dt_from and dt_to
        """
        return self.data_frame[column_indexer][dt_from:dt_to]

    def get_times(self, time_indexer):
        """

        :param time_indexer: A date time
        :return: A list containing the value of all the series at time time_indexer
        """
        return self.data_frame.loc[time_indexer, Database._output_]