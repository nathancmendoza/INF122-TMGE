from threading import Thread
import time
import pytest

from inf122_tmge.core.board_factory import BoardFactory
from inf122_tmge.core.tile_builder import TileBuilder
from inf122_tmge.model.tiles.tile import Tile
from inf122_tmge.view.view import View



# Mark test as integration to avoid executing with test suite
@pytest.mark.integration
def test_launch_view():
    """Manual integration test to visually inspect the board"""
    game_board = BoardFactory.create_board('default', 10, 24)
    view = View(game_board) 
    view.launch_view()


@pytest.mark.integration
def test_update_tile():
    """Manual integration test to see if a tile is drawn"""
    game_board = BoardFactory.create_board('default', 10, 24)
    tile_to_place = TileBuilder().add_position(3,3).add_color('red').construct()
    game_board.place_tile(tile_to_place, 3, 3)
    view = View(game_board) 
    view.launch_view()

@pytest.mark.integration
def test_threading_fill_board():
    """Manual integration test to see board is filled one by one"""
    game_board = BoardFactory.create_board('default', 10, 24)
    view = View(game_board) 

    def place_tiles():
        for i in range(1,11):
            for j in range(1,25):
                tile_to_place = TileBuilder().add_position(i,j).add_color('red').construct()

                game_board.place_tile(tile_to_place, i, j)
                view.update_board_view(game_board)
                time.sleep(.0165)

    view.launch_view(place_tiles)

@pytest.mark.integration
def test_user_input():
    """Manual integration testing a user input"""
    game_board = BoardFactory.create_board('default', 10, 24)
    view = View(game_board) 

    moving_tile = TileBuilder().add_position(5,1).add_color('red').construct()
    game_board.place_tile(moving_tile, moving_tile.position.x, moving_tile.position.y)

    view.add_keybind('KeyPress')
    def move_down():
        clear_tile = TileBuilder().add_position(moving_tile.position.x, moving_tile.position.y).add_color('#D3D3D3').construct()
        game_board.place_tile(clear_tile, moving_tile.position.x, moving_tile.position.y)
        moving_tile.position.y += 1
        game_board.place_tile(moving_tile, moving_tile.position.x, moving_tile.position.y)

    def gameloop():
        while True:
            try:
                if view.events.get(block=False) == 's':
                    move_down()
            except:
                pass
    
            view.update_board_view(game_board)
            time.sleep(.0165)

    view.launch_view(gameloop)