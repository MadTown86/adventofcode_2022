import os
import dotenv

dotenv.load_dotenv()
input_dir = os.getenv('adventofcode2022')
fname = os.path.join(input_dir, 'dec9thexample.txt')

tail_positions = []
xh, xt, yh, ht = 0, 0, 0, 0
class Snake:

    class Node:
        __slots__ = 'x', 'y'

        def __init__(self):
            self.x = 0
            self.y = 0

        def _coord(self):
            return (self.x, self.y)


    def __init__(self):
        self.head = self.Node()
        self.tail = self.Node()
        self.positions = [self.tail._coord()]

    def _move_head(self, left: int = None, right: int = None, up: int = None, down: int = None):
        if left:
            self.head.x = self.head.x - left
        if right:
            self.head.x = self.head.x + right
        if up:
            self.head.y = self.head.y + up
        if down:
            self.head.y = self.head.y - down

    def _move_tail(self):
        if self.head.x == self.tail.x:
            pass
        if self.head.y == self.tail.y:
            pass

    def snake_run(self, f: str):
        with open(f, 'r') as fl:
            lines = fl.readlines()
        for line in lines:
            print(line)
            if "L" in line:
                self._move_head(left=int(line[2:].strip()))
                print(self.head.x, self.head.y)
                self._move_tail()
            if "R" in line:
                self._move_head(right=int(line[2:].strip()))
                print(self.head.x, self.head.y)
                self._move_tail()
            if "U" in line:
                self._move_head(up=int(line[2:].strip()))
                print(self.head.x, self.head.y)
                self._move_tail()
            if "D" in line:
                self._move_head(down=int(line[2:].strip()))
                print(self.head.x, self.head.y)
                self._move_tail()

if __name__ == "__main__":
    S = Snake()
    S.snake_run(fname)