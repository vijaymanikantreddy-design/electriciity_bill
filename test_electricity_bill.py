import pytest
from electricity_bill import calculate_bill

def test_zero_units():
    assert calculate_bill(0) == 50

def test_units_under_100():
    assert calculate_bill(50) == 50 + 50 * 1.50

def test_units_100():
    assert calculate_bill(100) == 50 + 100 * 1.50

def test_units_150():
    assert calculate_bill(150) == 50 + 100*1.5 + 50*2.5

def test_units_250():
    assert calculate_bill(250) == 50 + 100*1.5 + 100*2.5 + 50*4

def test_units_350():
    assert calculate_bill(350) == 50 + 100*1.5 + 100*2.5 + 100*4 + 50*6

def test_negative_units():
    with pytest.raises(ValueError):
        calculate_bill(-10)
