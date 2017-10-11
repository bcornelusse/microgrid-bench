from datetime import datetime, timedelta

import numpy as np
import pandas as pd

from microgrid.forecast import Forecaster
from microgrid.history import Database


def test_history_roll():
    nobs, history_size = 10, 3
    y = np.arange(nobs)

    df = pd.DataFrame(data={'y': y})
    for tau in range(1, history_size):
        col_name = "shift_%d" % tau
        df[col_name] = df['y'].shift(tau)

    df = df.dropna(axis=0, how='any')

    X_pandas = df.as_matrix()

    X_gme = np.zeros((nobs, history_size))
    for h in range(history_size):
        X_gme[:, h] = np.roll(y, h + 1)
    X_gme = X_gme[history_size:, :]

    X_bcr = np.zeros((nobs, history_size))
    for h in range(history_size, nobs):
        X_bcr[h, :] = y[h - history_size:h]
    X_bcr = X_bcr[history_size:, :]

    np.array_equal(X_gme, X_bcr)
    np.array_equal(X_pandas, X_gme)
    np.array_equal(X_pandas, X_bcr)


def test_one_hour_forecast():
    database = Database('../data/dataset.csv')
    forecaster = Forecaster(database)

    dt_from = datetime(2015, 1, 1, 0, 0, 0)
    dt_to = datetime(2015, 1, 1, 0, 0, 0)

    ypred = forecaster.forecast("Price", dt_from, dt_to)

    assert ypred is not None
    assert ypred.shape[0] == 1


def test_one_day_forecast():
    database = Database('../data/dataset.csv')
    forecaster = Forecaster(database)

    dt_from = datetime(2015, 1, 1, 0, 0, 0)
    dt_to = datetime(2015, 1, 1, 23, 0, 0)

    ypred = forecaster.forecast("Price", dt_from, dt_to)

    assert ypred is not None
    assert ypred.shape[0] == 24


def test_repeated_hourly_forecast():
    quantity = "Price"
    database = Database('../data/dataset.csv')
    forecaster = Forecaster(database)

    num_hours = 20
    dt_start = datetime(2015, 1, 1, 0, 0, 0)
    dt_stop = dt_start + timedelta(hours=num_hours - 1)

    ypred = np.zeros((num_hours))
    for i in range(num_hours):
        print "Hour %d" % (i + 1)
        dt_from = dt_start + timedelta(hours=i)
        dt_to = dt_from

        ypred[i] = forecaster.forecast(quantity, dt_from, dt_to)

    df_ytrue = database.data_frame.loc[dt_start:dt_stop, quantity]

    dates = df_ytrue.index.values
    ytrue = df_ytrue.as_matrix()

    assert ytrue.shape == ypred.shape

    # plt.plot_date(dates, ytrue, "g")
    # plt.plot_date(dates, ypred, "k--")
    # plt.show()


def test_repeated_daily_forecast():
    quantity = "Price"
    database = Database('../data/dataset.csv')
    forecaster = Forecaster(database)

    num_days = 20
    ypred = np.zeros((num_days * 24))
    for i in range(num_days):
        print "Day %d" % (i + 1)
        dt_from = datetime(2015, 1, i + 1, 0, 0, 0)
        dt_to = datetime(2015, 1, i + 1, 23, 0, 0)

        ypred[i * 24:((i + 1) * 24)] = forecaster.forecast(quantity, dt_from, dt_to)

    df_ytrue = database.data_frame.loc['2015-1-1 00:00:00':'2015-1-20 23:00:00', quantity]

    dates = df_ytrue.index.values
    ytrue = df_ytrue.as_matrix()

    assert ytrue.shape == ypred.shape

    # plt.plot_date(dates, ytrue, "g")
    # plt.plot_date(dates, ypred, "k--")
    # plt.show()
