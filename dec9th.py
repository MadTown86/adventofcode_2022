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
        self.positions = {(self.tail.x, self.tail.y)}


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
        x_dif = self.head.x - self.tail.x
        y_dif = self.head.y - self.tail.y

        def same_axis(delt, x=True):
            if delt > 0:
                while delt > 1:
                    if x:
                        self.tail.y += 1
                    else:
                        self.tail.x += 1
                    self.positions.add(self.tail._coord())
                    delt -= 1
            elif delt < 0:
                while delt < -1:
                    if x:
                        self.tail.y -= 1
                    else:
                        self.tail.x -= 1
                    self.positions.add(self.tail._coord())
                    delt += 1

        # UP/DOWN - same axis:
        if self.head.x == self.tail.x:
            same_axis(y_dif)
        # LEFT/RIGHT - same axis:
        if self.head.y == self.tail.y:
            same_axis(x_dif, x=False)

        # 1 STEP MOVES:
        if x_dif == 1 and y_dif == 1:







    def snake_run(self, f: str):
        with open(f, 'r') as fl:
            lines = fl.readlines()
        for line in lines:
            print(line)
            if "L" in line:
                self._move_head(left=int(line[2:].strip()))
                print(f'HEAD: {self.head.x, self.head.y}')
                self._move_tail()
                print(f'TAIL: {self.tail.x, self.tail.y}')
            if "R" in line:
                self._move_head(right=int(line[2:].strip()))
                print(f'HEAD: {self.head.x, self.head.y}')
                self._move_tail()
                print(f'TAIL: {self.tail.x, self.tail.y}')
            if "U" in line:
                self._move_head(up=int(line[2:].strip()))
                print(f'HEAD: {self.head.x, self.head.y}')
                self._move_tail()
                print(f'TAIL: {self.tail.x, self.tail.y}')
            if "D" in line:
                self._move_head(down=int(line[2:].strip()))
                print(f'HEAD: {self.head.x, self.head.y}')
                self._move_tail()
                print(f'TAIL: {self.tail.x, self.tail.y}')

if __name__ == "__main__":
    S = Snake()
    S.snake_run(fname)