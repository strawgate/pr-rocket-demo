from string_utils import reverse, is_palindrome


def test_reverse():
    assert reverse("hello") == "olleh"
    assert reverse("") == ""


def test_is_palindrome():
    assert is_palindrome("racecar")
    assert is_palindrome("A man a plan a canal Panama")
    assert not is_palindrome("hello")
