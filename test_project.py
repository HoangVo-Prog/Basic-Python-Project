from project import draw_board, is_full, check_letter, game_over, move_to_win_and_defense


def test_draw_board():
    assert draw_board([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]) == ' | | \n | | \n | | \n'
    assert draw_board([["x", "o", "x"], ["o", "x", "o"], ["x", "o", " "]]) == 'x|o|x\no|x|o\nx|o| \n'
    assert draw_board([["o", "o", "x"], ["o", "o", "o"], ["x", "x", "x"]]) == 'o|o|x\no|o|o\nx|x|x\n'


def test_is_full():
    assert is_full([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]) is False
    assert is_full([["x", "o", "x"], ["o", "x", "o"], ["x", "o", "o"]]) is True
    assert is_full([["x", "o", "x"], ["o", "x", "o"], ["x", "o", " "]]) is False


def test_check_letter():
    assert check_letter([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]], [1, 1]) is True
    assert check_letter([["x", "o", "x"], ["o", "x", "o"], ["x", "o", "o"]], [1, 1], "o") is False
    assert check_letter([["x", "o", "x"], ["o", "x", "o"], ["x", "o", " "]], [2, 2]) is True


def test_game_over():
    assert game_over([["x", "o", "x"], ["o", "x", "o"], ["x", "o", " "]], "x") is True
    assert game_over([["o", "o", "x"], ["o", "o", "o"], ["x", "x", "x"]], "o") is True
    assert game_over([["x", "x", "o"], ["o", "o", " "], [" ", " ", " "]], "x") is False


def test_move_to_win_and_defense():
    assert move_to_win_and_defense([["x", " ", " "], ["x", "o", " "], [" ", " ", " "]], "x") == [2, 0]
    assert move_to_win_and_defense([["x", "x", "o"], ["o", "o", " "], [" ", " ", " "]], "x") is None
    assert move_to_win_and_defense([["x", " ", " "], [" ", "o", " "], [" ", " ", " "]], "o") is None
