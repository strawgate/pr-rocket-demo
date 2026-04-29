from validation import validate_email, validate_phone, validate_age, sanitize_html


def test_validate_email_valid():
    assert validate_email("user@example.com") is True


def test_validate_email_invalid():
    assert validate_email("not-an-email") is False
    assert validate_email("") is False


def test_validate_phone_10_digits():
    assert validate_phone("555-123-4567") == "+15551234567"


def test_validate_phone_11_digits():
    assert validate_phone("1-555-123-4567") == "+15551234567"


def test_validate_phone_invalid():
    assert validate_phone("123") == ""


def test_validate_age():
    assert validate_age(25) == 25
    assert validate_age("30") == 30
    assert validate_age(-1) is None
    assert validate_age(200) is None


def test_sanitize_html():
    assert sanitize_html("<b>hello</b>") == "hello"
    assert sanitize_html("no tags") == "no tags"
