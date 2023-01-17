import os
import dotenv
import matplotlib.pyplot as plt

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
        old = [self.head.x, self.head.y]

        if left:
            self.head.x = self.head.x - left
            return "left"
        if right:
            self.head.x = self.head.x + right
            return "right"
        if up:
            self.head.y = self.head.y + up
            return "up"
        if down:
            self.head.y = self.head.y - down
            return "down"

    def _move_tail(self, direc: 'str' = "up"):
        x_dif = self.head.x - self.tail.x
        y_dif = self.head.y - self.tail.y

        print(f'DIF: {x_dif, y_dif}')

        def same_axis(delt, x=True, ):
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

        if all([self.head.x == self.tail.x, self.head.y == self.tail.y]):
            pass
        # UP/DOWN - same axis:
        elif self.head.x == self.tail.x and self.head.y != self.tail.y:
            same_axis(y_dif)
        # LEFT/RIGHT - same axis:
        elif self.head.y == self.tail.y and self.head.x != self.tail.x:
            same_axis(x_dif, x=False)

        # 1 STEP MOVES:

        elif x_dif == 1 and y_dif == 1:
            # before h/y | after h/y - h(3, 3)t(3, 2) after: h(4, 3)t(3,2)
            if direc == "right":
                self.tail.y += 1
            # before: h(3, 3) t(2, 3) - after: h(3, 4) t(2, 3)
            elif direc == "up":
                self.tail.x += 1
        elif x_dif == -1 and y_dif == 1:
            # before h(3, 3) t(3, 2) after: h(2, 3) t(3, 2)
            if direc == "left":
                self.tail.y += 1
            elif direc == "up":
                self.tail.x -= 1
        elif x_dif == -1 and y_dif == -1:
            if direc == "left":
                self.tail.y -= 1
            elif direc == "down":
                self.tail.x -= 1
        elif x_dif == 1 and y_dif == -1:
            if direc == "down":
                self.tail.x += 1
            elif direc == "right":
                self.tail.y -= 1

        elif x_dif == 1 and y_dif > 0:
            self.tail.y += 1
            y_dif -= 1
            self.tail.x += 1
            self.positions.add(self.tail._coord())
            same_axis(y_dif, x=False)

        elif x_dif == 1 and y_dif < 0:
            self.tail.y -= 1
            y_dif += 1
            self.tail.x += 1
            self.positions.add(self.tail._coord())
            same_axis(y_dif, x=False)

        elif x_dif == -1 and y_dif > 0:
            self.tail.y += 1
            y_dif -= 1
            self.tail.x -= 1
            self.positions.add(self.tail._coord())
            same_axis(y_dif, x=False)

        elif x_dif == -1 and y_dif < 0:
            self.tail.y -= 1
            y_dif += 1
            self.tail.x -= 1
            self.positions.add(self.tail._coord())
            same_axis(y_dif, x=False)

        elif y_dif == 1 and x_dif > 0:
            self.tail.x += 1
            x_dif -= 1
            self.tail.y += 1
            self.positions.add(self.tail._coord())
            same_axis(x_dif)

        elif y_dif == 1 and x_dif < 0:
            self.tail.x -= 1
            x_dif += 1
            self.tail.y += 1
            self.positions.add(self.tail._coord())
            same_axis(x_dif)

        elif y_dif == -1 and x_dif > 0:
            self.tail.x += 1
            x_dif -= 1
            self.tail.y -= 1
            self.positions.add(self.tail._coord())
            same_axis(x_dif)

        elif y_dif == -1 and x_dif < 0:
            self.tail.x -= 1
            x_dif += 1
            self.tail.y -= 1
            self.positions.add(self.tail._coord())
            same_axis(x_dif)

        else:
            print("missed element")
            print(f'TAIL CURRENT: {self.tail.x, self.tail.y}')
            print(f'HEAD CURRENT: {self.head.x, self.head.y}')

    def snake_run(self, f: str):
        with open(f, 'r') as fl:
            lines = fl.readlines()
        for line in lines:
            print(line)
            torg = self.tail.x, self.tail.y
            horg = self.head.x, self.head.y
            print(f'TAIL ORIGINAL: {torg}')
            print(f'HEAD ORIGINAL: {horg}')
            if "L" in line:
                hm = self._move_head(left=int(line[2:].strip()))
                print(f'HEAD: {self.head.x, self.head.y}')
                self._move_tail(hm)
                print(f'TAIL: {self.tail.x, self.tail.y}')
            if "R" in line:
                hm = self._move_head(right=int(line[2:].strip()))
                print(f'HEAD: {self.head.x, self.head.y}')
                self._move_tail(hm)
                print(f'TAIL: {self.tail.x, self.tail.y}')
            if "U" in line:
                hm = self._move_head(up=int(line[2:].strip()))
                print(f'HEAD: {self.head.x, self.head.y}')
                self._move_tail(hm)
                print(f'TAIL: {self.tail.x, self.tail.y}')
            if "D" in line:
                hm = self._move_head(down=int(line[2:].strip()))
                print(f'HEAD: {self.head.x, self.head.y}')
                self._move_tail(hm)
                print(f'TAIL: {self.tail.x, self.tail.y}')


if __name__ == "__main__":
    S = Snake()
    S.snake_run(fname)
