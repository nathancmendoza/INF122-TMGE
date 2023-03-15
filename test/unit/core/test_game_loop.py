"""Test for game_loop"""

import pytest
import time

from tilematch_tools.core import GameLoop, GameState
from tilematch_tools.view import View

@pytest.fixture
def simple_game_loop():
    class SimpleGameLoop(GameLoop):
        def handle_input(self):
            super().handle_input()

        def find_matches(self, match_conditions):
            super().find_matches(match_conditions)

        def clear_matches(self, matches_found):
            super().clear_matches(matches_found)

        def update_view(self):
            super().update_view()

    return SimpleGameLoop('GameState', 'GameView', 2_000_000_000)

def test_game_loop_subclass_implements_template():
    class InvalidGameLoop(GameLoop):
        def __init__(self):
            pass

    with pytest.raises(TypeError):
        InvalidGameLoop()

def test_delay_between_loop_interations(simple_game_loop):
    start = time.time_ns()
    simple_game_loop()
    end = time.time_ns()
    assert end - start > 1_000_000_000
