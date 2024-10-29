from math import pi
class Figure:
        sides_count = 0

        def __init__(self, color=(0, 0, 0), *sides):
            self.filled = False  # закрашенный, bool
            self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count  # список сторон (целые числа)
            self.__color = list(color)  # список цветов в формате RGB

        def get_color(self):
            return self.__color

        def __is_valid_color(self, r, g, b):
            if isinstance(r, int) and isinstance(g, int) and isinstance(b, int): #  проверка на принадлежность к целочисленным данным
                if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:  #  проверка r, g, b чтобы значения не были больше 255
                    return True
            return False

        def set_color(self, r, g, b): #Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность.
            if self.__is_valid_color(r, g, b): # к методу __is_valid_color
                self.__color = (r, g, b)
                self.filled = True

        def __is_valid_sides(self, *args):
                return len(args) == self.sides_count and all(isinstance(args1, int) and args1 > 0 for args1 in args)

        def __len__(self):
            return sum(self.__sides)

        def get_sides(self):
            return self.__sides

        def set_sides(self, *sides):
                if len(sides) == len(self.__sides):
                        valid_sides = []
                        for side in sides:
                                if self.__is_valid_sides(side):
                                        valid_sides.append(side)

                                self.__sides = valid_sides


class Circle(Figure): #класс круг
        sides_count = 1

        def __init__(self, color, *sides):  # R = C/2𝛑 , где C — длина окружности
            super().__init__(color, *sides)
            sideL = sides[0]
            self.__radius = sideL / (2 * pi)

        def get_square(self): #S = πr².
            return pi * self.__radius**2


class Triangle(Figure): #класс треугольник
        sides_count = 3

        def __init__(self, color, *sides):
            super().__init__(self, color, *sides) # super() обращение к родительскому классу как и Figure.

        def get_square(self): # P = a+b+c/2 т.к. сторон у треугольника 3, то его стороны будут - [1, 1, 1]
            p = self.sides_count / 2 #получается 1,5- это полупериметр
            a = 1
            b = 1
            c = 1
            S = ((p*(p - a))*(p - b)*(p - c))**0,5
            print(S)


class Cube(Figure): #класс куб
        sides_count = 12

        def __init__(self, color, *sides):
            side = sides[0] if len(sides) == 1 else 1
            super().__init__(color, *[side] * self.sides_count)

        def get_volume(self):
            return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
