import pandas as pd

class Database:

    _inputs_ = ['Year', 'Month', 'Day', 'Hour', 'Minutes', 'Seconds', 'IsoDayOfWeek', 'IsoWeekNumber']
    _output_ = ['Price', 'EPV', 'C1', 'C2', 'C3']

    def __init__(self, path_to_csv):
        self.data_frame = self.read_data(path_to_csv)

    def read_data(self, path):
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
        return self.data_frame[column_indexer].get(time_indexer)

    def get_column(self, column_indexer, dt_from, dt_to):
        return self.data_frame[column_indexer][dt_from:dt_to]

    def get_times(self, time_indexer):
        return self.data_frame.loc[time_indexer, Database._output_]