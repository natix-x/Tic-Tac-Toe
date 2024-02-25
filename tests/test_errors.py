from game.errors import Errors
import pytest
import unittest.mock as mock


class TestErrors:
    @pytest.fixture
    def mocked_messagebox(self):
        with mock.patch('game.errors.messagebox') as mocked:
            yield mocked

    def test_error_occurrence_same_nicknames(self, mocked_messagebox):
        mocked_messagebox.askyesno.return_value = True
        errors = Errors("Player1", "Player1")
        assert errors.error_occurrence() is True

    def test_error_occurrence_empty_nicknames(self, mocked_messagebox):
        mocked_messagebox.askyesno.return_value = True
        errors = Errors("", "Player2")
        assert errors.error_occurrence() is True

        errors = Errors("Player1", "")
        assert errors.error_occurrence() is True

    def test_error_occurrence_long_nicknames(self, mocked_messagebox):
        mocked_messagebox.askyesno.return_value = True
        errors = Errors("PlayerWithVeryLongName", "Player2")
        assert errors.error_occurrence() is True

        errors = Errors("Player1", "AnotherPlayerWithVeryLongName")
        assert errors.error_occurrence() is True

    def test_error_occurrence_valid_nicknames(self, mocked_messagebox):
        mocked_messagebox.askyesno.return_value = False
        errors = Errors("Player1", "Player2")
        assert errors.error_occurrence() is False

    def test_show_error_message(self, mocked_messagebox):
        Errors.show_error_message("Test message")
        mocked_messagebox.showinfo.assert_called_once_with("Error", message="Test message")

