"""Regression tests for parse_quantity."""
import pytest

from warehouse.quantity import parse_quantity


def test_positive_quantity():
    assert parse_quantity("5") == 5


def test_zero_quantity():
    assert parse_quantity("0") == 0


def test_negative_quantity_raises():
    with pytest.raises(ValueError):
        parse_quantity("-1")


def test_large_negative_quantity_raises():
    with pytest.raises(ValueError):
        parse_quantity("-100")


def test_whitespace_stripped():
    assert parse_quantity("  3  ") == 3
