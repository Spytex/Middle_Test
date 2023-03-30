from main import Loader

import pytest


@pytest.fixture()
def loader():
    return Loader()


@pytest.mark.parametrize("filename, expected",
                         [("test_data_1.txt", {'USA': [(2000, 100), (2001, 200), (2002, 300)]})])
def test_read_population_data(loader, filename, expected):
    population_data = loader.read_population_data(filename)
    assert population_data == expected


@pytest.mark.parametrize("population_data, expected", [
    ({'USA': [(2000, 100), (2001, 200), (2002, 300)],
      'Canada': [(2000, 1000), (2001, 1200), (2002, 1500)]},
     {'USA': [(2001, 100), (2002, 100)],
      'Canada': [(2001, 200), (2002, 300)]}),
    ({'USA': [(2000, 100), (2001, 200), (2002, 300)],
      'Canada': [(2000, 1000), (2001, 1200), (2002, 1500)],
      'Japan': [(2000, 100), (2001, 200), (2002, 300)]},
     {'USA': [(2001, 100), (2002, 100)],
      'Canada': [(2001, 200), (2002, 300)],
      'Japan': [(2001, 100), (2002, 100)]})
])
def test_process_population_data_change(loader, population_data, expected):
    population_change = loader.process_population_data_change(population_data)
    assert population_change == expected
