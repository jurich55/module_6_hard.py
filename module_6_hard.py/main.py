import math


class Figure:
    sides_count = 0

    def __init__(self, color, sides, filled=bool):
        self.__sides = [sides for i in range(self.sides_count)]  # список сторон (int)
        self.__color = list(color)  # список цветов  (RGB)
        self.filled = filled  # окрашенный, (bool)

    def __len__(self):
        return sum(self.__sides)  # периметр фигуры

    def get_color(self):
        return self.__color  # список цветов  (RGB)

    def get_sides(self):
        return self.__sides  # список сторон

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b) is True:
            self.__color = [r, g, b]

    def set_sides(self, *args):
        my_list = [*args]       # проверяет кол-во сторон у фигуры
        if self.__is_valid_sides(my_list) is True:
            self.__sides = my_list

    def __is_valid_sides(self, my_list):
        if len(my_list) == self.sides_count:
            for i in my_list:    # проверяет кол-во сторон у фигуры
                if i < 0:
                    return False
            return True
        else:
            return False

    @staticmethod
    def __is_valid_color(r, g, b):     # числовые значения цветов  (RGB)
        return True if 0 < r < 255 and 0 < g < 255 and 0 < b < 255 else False


class Circle(Figure):      # круг
    sides_count = 1

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__radius = sides / 2 * math.pi  # радиус круга
        self.__square = 0

    def get_square(self):
        return math.pi * (self.__radius ** 2)  # площадь круга


class Triangle(Figure):      # треугольник
    sides_count = 3

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__sides = sides


class Cube(Figure):           # куб
    sides_count = 12

    def __init__(self, color, sides):
        super().__init__(color=color, sides=sides)
        self.__sides = sides

    def get_volume(self):
        return self.__sides ** 3  # объём куба


circle1 = Circle((200, 200, 100), 1)  # (Цвет, окружность)
cube1 = Cube((222, 35, 130), 6)  # (Цвет, сторона)
triangle1 = Triangle((122, 35, 234), [5, 4, 6])

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
cube1.set_color(300, 70, 15)  # (300 > 255) --> не изменится
print(circle1.get_color())
print(cube1.get_color())
print(triangle1.get_color())

#  изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # не изменится
circle1.set_sides(15)  # длина окружности
triangle1.set_sides(8, 6, 9)  # длины сторон треугольника
print(cube1.get_sides())
print(circle1.get_sides())
print(triangle1.get_sides())

print(len(circle1))  # длина окружности круга
print(len(triangle1))  # периметр треугольника

print(cube1.get_volume())  # объём (куба):

print("Площадь круга:", round(circle1.get_square(), 4))
