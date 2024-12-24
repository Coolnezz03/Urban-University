from math import pi, pow, sqrt

class Figure:
    sides_count = 0
    def __init__(self, color, *sides):
        self.__color = list(color)
        self.filled = True
        if not self.__is_valid_sides(*sides):
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = list(sides)

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
        return(0 <= self.r <= 255 and 0<= self.g <= 255 and 0<= self.b <= 255)

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        return(all(isinstance(item, int) for item in args) and
               all(map(lambda x: x >= 0, args)) and
                   len(args) == self.sides_count)


    def get_sides(self):
        return self.__sides


    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)
        elif len(new_sides) == 1:
            self.__sides = list(new_sides * self.sides_count)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0]*2*pi

    def get_square(self):
        return pi*(self.__radius ** 2)

class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b , c = self.get_sides()
        s = (a + b + c) / 2
        square = sqrt(s * (s - a) * (s - b) * (s - c))
        if square <= 0:
            print('Такой треугольник не существует')
        else:
            return square

class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, sides)
        if len(sides) == 1:
            super().set_sides(*sides * 12)
        elif all(x == sides[0] for x in sides):
            super().set_sides(*sides)

    def get_volume(self):
        return self.get_sides()[0]**3



circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
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

#Проверка площади треугольника
bb = Triangle((200, 200, 100), 10, 6,5)
print(f'Площадь треугольника = {bb.get_square()}')

#Проверка замены значений сторон треугольника
bb.set_sides(2, 5, 3)
print(bb.get_sides())
print(f'Площадь треугольника = {bb.get_square()}')

#Проверка замены длинны стороны куба и его объема
aa = Cube((100, 50 , 10), 18)
aa.set_sides(10)
print(aa.get_sides())

#Проверка запишутся ли единицы в значения сторон куба, при не правильной записи
yy = Cube((200, 200, 100), 9, 9, 8, 7, 6, 5, 4, 3, 2, 1, 12, 12)
print(yy.get_sides())