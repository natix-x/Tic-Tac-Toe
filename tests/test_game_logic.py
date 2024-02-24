import pytest
from game.game_logic import GameLogic


class TestGameLogic:
    @pytest.fixture
    def game(self):
        buttons = [[" " for _ in range(3)] for _ in range(3)]
        return GameLogic(buttons)

    @pytest.mark.parametrize(
        "buttons, expected_winning_combination",
        [
            ([["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]], [(0, 0), (0, 1), (0, 2)]),
            ([[" ", " ", "X"], [" ", " ", "X"], [" ", " ", "X"]], [(0, 2), (1, 2), (2, 2)]),
            ([["X", " ", " "], ["X", " ", " "], ["X", " ", " "]], [(0, 0), (1, 0), (2, 0)]),
            ([["O", " ", " "], [" ", "O", " "], [" ", " ", "O"]], [(0, 0), (1, 1), (2, 2)]),
            ([[" ", " ", " "], [" ", "X", " "], [" ", " ", " "]], None)
        ],
    )
    def test_check_if_win(self, game, buttons, expected_winning_combination):
        game.buttons = [[{"text": symbol} for symbol in row] for row in buttons]
        assert game.check_if_win() == expected_winning_combination

    @pytest.mark.parametrize(
        "buttons, expected_result",
        [
            ([["X", "O", "X"], ["O", "X", "O"], ["O", "X", "X"]], True),
            ([["X", "O", "X"], ["O", "X", "O"], ["O", " ", "X"]], False),
            ([["X", "X", "O"], ["O", "O", "X"], ["X", "O", "X"]], True),
            ([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]], True),
            ([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], False)
        ],
    )
    def test_check_if_tie(self, game, buttons, expected_result):
        game.buttons = [[{"text": symbol} for symbol in row] for row in buttons]
        assert game.check_if_tie() == expected_result



