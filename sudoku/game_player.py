import model.game_identifier as gi
import solver.solver as s

game_numbers = gi.get_game_string_numbers('sudoku_expert_example.png')
game = s.Sudoku(game_numbers)
print('Game:')
game.show()
print('Solution:')
game.solve()

