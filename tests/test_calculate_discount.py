"""Lab 3: EP and BVA tests for calculate_discount (T1-T10).

Spec assumptions:
- premium -> price * 0.8; regular -> price unchanged; no rounding
- price must be a number >= 0 (negative -> ValueError, non-number -> TypeError)
"""

import pytest

from app.tasks import calculate_discount


@pytest.mark.parametrize(
    "price, is_premium, expected",
    [
        pytest.param(100, True, 80, id="T1-EP-typical-premium"),
        pytest.param(100, False, 100, id="T2-EP-typical-regular"),
        pytest.param(0, True, 0, id="T3-BVA-zero-premium"),
        pytest.param(0, False, 0, id="T4-BVA-zero-regular"),
        pytest.param(0.01, True, 0.008, id="T5-BVA-just-inside-premium"),
        pytest.param(0.01, False, 0.01, id="T6-BVA-just-inside-regular"),
        pytest.param(159.66, True, 127.728, id="T9-EP-float-premium"),
    ],
)
def test_valid_inputs_return_expected_price(price, is_premium, expected):
    """Valid partitions and on/inside boundary values give the right price."""
    assert calculate_discount(price, is_premium) == pytest.approx(expected)


@pytest.mark.parametrize(
    "price, is_premium, error",
    [
        pytest.param(-0.01, True, ValueError, id="T7-BVA-just-outside"),
        pytest.param("50", False, TypeError, id="T8-EP-string-price"),
        pytest.param(-45.99, False, ValueError, id="T10-EP-negative-price"),
    ],
)
def test_invalid_inputs_are_rejected(price, is_premium, error):
    """Invalid partitions and just-outside boundary must raise an error."""
    with pytest.raises(error):
        calculate_discount(price, is_premium)