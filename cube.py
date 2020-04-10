import numpy as np

class Cube:
    """A rubiks cube class. yet to be compatible with sizes other than 3X3."""
    def __init__(self, size):
        self.size = size
        self.sides = np.zeros((6, self.size, self.size))
        for i in range(6):
            self.sides[i] = i

    def is_solved(self):
        a = Cube(3)
        return np.array_equal(a.sides, self.sides)

    def rotate(self, direction):
        """
        Rotates the cube in a given direction
        :param direction: R,L,Rz,Lz
        :return: None
        """
        if direction == "R":
            for i in range(6):
                self.sides[i] = np.rot90(self.sides[i])
            self.sides[4] = np.rot90(np.rot90(self.sides[4]))
            temp = np.copy(self.sides[0])
            self.sides[0] = np.copy(self.sides[3])
            self.sides[3] = np.copy(self.sides[5])
            self.sides[5] = np.copy(self.sides[1])
            self.sides[1] = temp
        elif direction == "L":
            self.rotate("R")
            self.rotate("R")
            self.rotate("R")
        elif direction == "Rz":
            for i in range(3):
                self.sides[0] = np.rot90(self.sides[0])
            self.sides[5] = np.rot90(self.sides[5])
            temp = np.copy(self.sides[2])
            self.sides[2] = np.copy(self.sides[3])
            self.sides[3] = np.copy(self.sides[4])
            self.sides[4] = np.copy(self.sides[1])
            self.sides[1] = temp
        elif direction == "Lz":
            self.rotate("Rz")
            self.rotate("Rz")
            self.rotate("Rz")

        else:
            print("error")

    def move(self, shift):
        """
        Moves a piece in a certain way
        :param shift: U,u,R,r,L,l,D,d,F,f
        :return: None
        """
        if shift == "U":
            self.sides[0] = np.rot90(np.rot90(np.rot90(self.sides[0], 3)))
            temp = np.copy(self.sides[2, 0])
            self.sides[2, 0] = np.copy(self.sides[3, 0])
            self.sides[3, 0] = np.copy(self.sides[4, 0])
            self.sides[4, 0] = np.copy(self.sides[1, 0])
            self.sides[1, 0] = temp
        elif shift == "u":
            self.move("U")
            self.move("U")
            self.move("U")
        elif shift == "R":
            self.rotate("R")
            self.move("U")
            self.rotate("L")
        elif shift == "r":
            self.move("R")
            self.move("R")
            self.move("R")
        elif shift == "L":
            self.rotate("L")
            self.move("U")
            self.rotate("R")
        elif shift == "l":
            self.move("L")
            self.move("L")
            self.move("L")
        elif shift == "D":
            self.rotate("R")
            self.rotate("R")
            self.move("U")
            self.rotate("R")
            self.rotate("R")
        elif shift == "d":
            self.move("D")
            self.move("D")
            self.move("D")
        elif shift == "F":
            self.rotate("Rz")
            self.move("L")
            self.rotate("Lz")
        elif shift == "f":
            self.move("F")
            self.move("F")
            self.move("F")
        else:
            print("error")

    def scramble(self, alg):
        """
        moves the cube by a string.
        :param alg: string of moves
        :return: None
        """
        for letter in alg:
            self.move(letter)

    def solve3moves(self, cube):
        """
        finds all possible algorithms to take a cube to a certain state (max 3 moves)
        :param cube: the wanted cube
        :return: None
        """
        arr = ["R", "r", "L", "l", "d", "D", "F", "f", "U", "u"]
        for a in arr:
            self.move(a)
            if np.array_equal(self.sides[2], cube.sides[2]):
                print(a)
            self.scramble(a + a + a)
        for a in arr:
            for b in arr:
                self.scramble(a+b)
                if np.array_equal(self.sides[2], cube.sides[2]):
                    print(a, b)
                self.scramble(b+b+b+a+a+a)
        for a in arr:
            for b in arr:
                for c in arr:
                    self.scramble(a+b+c)
                    if np.array_equal(self.sides[2], cube.sides[2]):
                        print(a, b, c)
                    self.scramble(c+c+c+b+b+b+a+a+a)