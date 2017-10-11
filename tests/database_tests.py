from numpy.testing import assert_almost_equal

from datetime import datetime
from microgrid.history.database import Database

def test_database_get_one():
    database = Database('../data/dataset.csv')
    dt = datetime(2014, 1, 1, 0, 0, 0)
    v = database.get_columns("C2", dt)

    assert_almost_equal(v, 1.71754247975)


def test_database_get_all():
    database = Database('../data/dataset.csv')
    dt = datetime(2014, 1, 1, 0, 0, 0)

    data = database.get_times(dt)

    assert_almost_equal(data['Price'], 23.86, decimal=4)
    assert_almost_equal(data['EPV'], 0.0, decimal=4)
    assert_almost_equal(data['C1'], 0.0, decimal=4)
    assert_almost_equal(data['C2'], 1.71754, decimal=4)
    assert_almost_equal(data['C3'], 0.42162, decimal=4)