import pytest

from data_handler import mask_email


@pytest.mark.parametrize(
    "email,expected",
    [
        (None, None),
        ("", ""),
        ("a@example.com", "a*@example.com"),
        ("ab@example.com", "a*@example.com"),
        ("abc@example.com", "a*c@example.com"),
        ("john.doe+tag@Example.COM", "j******e+tag@Example.COM"),
        ("  alice@example.com  ", "a***e@example.com"),
    ],
)
def test_mask_email(email, expected):
    assert mask_email(email) == expected
