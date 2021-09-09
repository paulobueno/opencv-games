Libraries build to identify Sudoku games in images and solve it

Example:  
![sudoku game](https://github.com/paulobueno/opencv-games/blob/master/images/sudoku_expert_example.png?raw=true "Sudoku Game")

```python
import model.game_identifier as gi
import solver.solver as s

game_numbers = gi.get_game_string_numbers('sudoku_expert_example.png')
game = s.Sudoku(game_numbers)
print('Game:')
game.show()
print('Solution:')
game.solve()
```

Game loaded and solved:
```
Game:
[0, 0, 3, 2, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 0, 0, 8, 0, 7]
[6, 0, 0, 9, 0, 0, 5, 3, 0]
[0, 0, 9, 0, 4, 0, 2, 0, 0]
[0, 7, 5, 0, 0, 2, 0, 9, 0]
[0, 0, 0, 0, 0, 0, 0, 5, 0]
[4, 0, 1, 0, 0, 0, 0, 0, 0]
[0, 8, 0, 5, 6, 1, 0, 0, 0]
[7, 0, 0, 0, 0, 0, 0, 0, 0]
Solution:
[8, 1, 3, 2, 5, 7, 6, 4, 9]
[5, 9, 4, 6, 1, 3, 8, 2, 7]
[6, 2, 7, 9, 8, 4, 5, 3, 1]
[3, 6, 9, 7, 4, 5, 2, 1, 8]
[1, 7, 5, 8, 3, 2, 4, 9, 6]
[2, 4, 8, 1, 9, 6, 7, 5, 3]
[4, 5, 1, 3, 7, 8, 9, 6, 2]
[9, 8, 2, 5, 6, 1, 3, 7, 4]
[7, 3, 6, 4, 2, 9, 1, 8, 5]
```

