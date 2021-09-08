import model.game_identifier as gi
import solver.solver as s

game_numbers = gi.get_game_string_numbers('sudoku_game_image.png')
s.Sudoku(game_numbers).solve()
