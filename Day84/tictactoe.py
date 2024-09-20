class Tictactoe:

    def __init__(self):
        self.item = [[' ' for _ in range(3)] for _ in range(3)]

    def show(self):
        print(f" {self.item[0][0]} | {self.item[0][1]} | {self.item[0][2]} ")
        print("-----------")
        print(f" {self.item[1][0]} | {self.item[1][1]} | {self.item[1][2]} ")
        print("-----------")
        print(f" {self.item[2][0]} | {self.item[2][1]} | {self.item[2][2]} ")

    def put(self, x, y, val):
        self.item[x-1][y-1] = val

    def reset(self):
        self.item = [[' ' for _ in range(3)] for _ in range(3)]
        self.show()