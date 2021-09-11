import img_transform.find_game as fg
import model.game_identifier as gi
import solver.solver as s

fg.gen_sudoku_image()
game_numbers = gi.get_game_string_numbers('../images/cropped_screenshot.png')
game = s.Sudoku(game_numbers)
print('Game:')
game.show()
key = input('Correct game?')
if key == ord('y'):
    print('Solution:')
    game.solve()
