# Maze Generator

穴掘り法、壁伸ばし法、棒倒し法による迷路の自動生成を行えるモジュール。

```python
from maze import Maze
import maze_generator

maze = Maze()

# 穴掘り法による迷路生成
maze_generator.generate1(maze)
# 壁伸ばし法による迷路生成
maze_generator.generate2(maze)
# 棒倒し法による迷路生成
maze_generator.generate3(maze)

maze.display()
```
