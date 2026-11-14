
import pytest
from src.cinema_price import ticket_price


# Test ticket prices using valid ticket quantities
@pytest.mark.parametrize("ticket_count, expected", [
    (0, 0),
    (1, 1200),
    (2, 2400),
    (10, 12000)
])
def test_valid_ticket_price(ticket_count, expected):
    # Arrange: Test data is provided above

    # Act: Calculate the ticket price
    result = ticket_price(ticket_count)

    # Assert: Compare the actual and expected prices
    assert result == expected


# Test negative ticket quantities
@pytest.mark.parametrize("ticket_count", [-1, -10])
def test_negative_ticket_count(ticket_count):
    # Act and Assert: Expect a ValueError
    with pytest.raises(ValueError):
        ticket_price(ticket_count)


# Test invalid input data types
@pytest.mark.parametrize("ticket_count", [
    True, False, 1.5, "2", None, [2]
])
def test_invalid_ticket_type(ticket_count):
    # Act and Assert: Expect a TypeError
    with pytest.raises(TypeError):
        ticket_price(ticket_count)
