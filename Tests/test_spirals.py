from Spirals.spirals import vel
import numpy as np
import pytest

max = 1.4*5*np.exp(-5.0/20.0)
min = 5.0
m = (max - min)/(-1.0)


def test_spirals_1():
    assert vel(2.0) == 1.4*2.0*np.exp(-2.0/20.0)  # this tests case r<=5


def test_spirals_2():
    assert vel(-2.0) == 1.4*2.0*np.exp(-2.0/20.0)  # this tests case of negative r


def test_spirals_3():
    assert vel(5.1) == m*(5.1 - 5.0) + max  # this tests case 5<r<6


def test_spirals_4():
    assert vel(7.0) == 5.0  # this tests case r>=6
