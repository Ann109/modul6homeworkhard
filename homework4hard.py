from math import pi
class Figure:
        sides_count = 0

        def __init__(self, color=(0, 0, 0), *sides, filled = bool):
            self.__sides = [sides for i in range(self.sides_count)]  # список сторон (целые числа)
            self.__color = list(color)  # список цветов в формате RGB
            self.filled = filled  # закрашенный, bool

        def get_color(self):
            return self.__color

        def __is_valid_color(self, r, g, b):
            if isinstance(r,int) and isinstance(g, int) and isinstance(b, int): #  проверка на принадлежность к целочисленным данным
                if 0<= r<= 255 and 0<= g<= 255 and 0<= b<= 255:  #  проверка r, g, b чтобы значения не были больше 255
                    return True
            return False

        def set_color(self, r, g, b): #Метод set_color принимает параметры r, g, b - числа и изменяет атрибут __color на соответствующие значения, предварительно проверив их на корректность.
            if self.__is_valid_color(r, g, b): # к методу __is_valid_color
                self.__color = [r, g, b]
                self.filled = True

        def __is_valid_sides(self, *new_sides):
            # if not isinstance(sides, int) and sides<0
                     #return False
             if len(new_sides) == self.sides_count: #если кол-во новых сторон=текущим+принадлежит числу и больше 0 то правильно
                   for sides in new_sides:
                           if isinstance(new_sides, int) and side > 0:
                                   return True
             else:
                     return False

        def _len_(self):
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

        def __init__(self, color, sides):  # R = C/2𝛑 , где C — длина окружности
            super().__init__(self, color, sides)

            self.__radius = self.get_sides()[0] / (2 * pi)

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

        def __init__(self, color, sides):
                side_12 = sides * 12
                super().__init__(color, side_12)

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