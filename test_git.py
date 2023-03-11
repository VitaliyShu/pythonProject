print("Введи стороны треугольника:")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a + b > c and a + c > b and b + c > a:
    print("Эти числа могут быть длинами сторон треугольника")
else:
    print("Эти числа не могут быть длинами сторон треугольника")
