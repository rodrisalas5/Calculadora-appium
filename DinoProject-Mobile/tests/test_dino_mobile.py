from displays_PO import CellPhone
import time
import pytest


def create():
    display = CellPhone.CellPhone()
    return display


def test_five_add_seven():
    display = create()
    assert display.add() == '= 12'


def test_five_less_seven():
    display = create()
    assert display.less() == '= 2'


def test_five_multiplied_two():
    display = create()
    assert display.multiplied() == '= 10'


def test_four_divided_two():
    display = create()
    assert display.divided() == '= 2'