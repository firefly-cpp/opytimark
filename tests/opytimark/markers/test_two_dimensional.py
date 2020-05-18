import numpy as np
import pytest

from opytimark.markers import two_dimensional


def test_ackley2():
    f = two_dimensional.Ackley2()

    x = np.array([0.5, 0.5])

    y = f(x)

    assert np.round(y, 2) == -173.62


def test_ackley3():
    f = two_dimensional.Ackley3()

    x = np.array([0.5, 0.5])

    y = f(x)

    assert np.round(y, 2) == -159.07


def test_adjiman():
    f = two_dimensional.Adjiman()

    x = np.array([0.5, 0.5])

    y = f(x)

    assert np.round(y, 2) == 0.02


def test_bartels_conn():
    f = two_dimensional.BartelsConn()

    x = np.array([0, 0])

    y = f(x)

    assert y == 1


def test_beale():
    f = two_dimensional.Beale()

    x = np.array([3, 0.5])

    y = f(x)

    assert y == 0


def test_biggs_exponential2():
    f = two_dimensional.BiggsExponential2()

    x = np.array([1, 10])

    y = f(x)

    assert y == 0


def test_bird():
    f = two_dimensional.Bird()

    x = np.array([4.70104, 3.15294])

    y = f(x)

    assert y == -106.76453674760198


def test_bohachevsky1():
    f = two_dimensional.Bohachevsky1()

    x = np.array([0, 0])

    y = f(x)

    assert y == 0


def test_bohachevsky2():
    f = two_dimensional.Bohachevsky2()

    x = np.array([0, 0])

    y = f(x)

    assert y == 0


def test_bohachevsky3():
    f = two_dimensional.Bohachevsky3()

    x = np.array([0, 0])

    y = f(x)

    assert y == 0


def test_booth():
    f = two_dimensional.Booth()

    x = np.array([1, 3])

    y = f(x)

    assert y == 0


def test_branin_hoo():
    f = two_dimensional.BraninHoo()

    x = np.array([9.42478, 2.475])

    y = f(x)

    assert y == 0.39788735775266204
