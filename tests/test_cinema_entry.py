
import pytest
from src.cinema_entry import can_watch


# Test screening eligibility using valid ages
@pytest.mark.parametrize("age, expected", [
    (0, False),
    (15, False),
    (16, True),
    (17, True),
    (100, True)
])
def test_valid_age_eligibility(age, expected):
    # Arrange: Test data is provided above

    # Act: Check screening eligibility
    result = can_watch(age)

    # Assert: Compare actual and expected results
    assert result is expected


# Test negative ages
@pytest.mark.parametrize("age", [-1, -10])
def test_negative_age(age):
    # Act and Assert: Expect a ValueError
    with pytest.raises(ValueError):
        can_watch(age)


# Test invalid input data types
@pytest.mark.parametrize("age", [
    True, False, 16.5, "16", None, [16]
])
def test_invalid_age_type(age):
    # Act and Assert: Expect a TypeError
    with pytest.raises(TypeError):
        can_watch(age)

