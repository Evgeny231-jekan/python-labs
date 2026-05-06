import math


# ---------- Исключения ----------
class InvalidShapeError(Exception):
    """Выбрасывается, когда фигура создана с некорректными параметрами."""
    pass


class InvalidMoveError(Exception):
    """Выбрасывается при попытке некорректного перемещения."""
    pass


class IntersectionError(Exception):
    """Выбрасывается при ошибках в проверке пересечения."""
    pass


class Shape:
    """Абстрактный базовый класс для всех фигур."""

    def __init__(self, identifier: str):
        if not identifier or not isinstance(identifier, str):
            raise InvalidShapeError("Идентификатор должен быть непустой строкой.")
        self._id = identifier

    @property
    def id(self):
        return self._id

    def area(self) -> float:
        """Возвращает площадь фигуры. Должен быть переопределён."""
        raise NotImplementedError("Метод area() должен быть реализован в наследнике.")

    def move(self, dx: float, dy: float):
        """Перемещает фигуру на (dx, dy). Должен быть переопределён."""
        raise NotImplementedError("Метод move() должен быть реализован в наследнике.")

    def is_intersect(self, other: 'Shape') -> bool:
        """Проверяет пересечение с другой фигурой. Должен быть переопределён."""
        raise NotImplementedError("Метод is_intersect() должен быть реализован в наследнике.")


class Triangle(Shape):
    """Треугольник, заданный тремя вершинами."""

    def __init__(self, identifier: str, x1, y1, x2, y2, x3, y3):
        super().__init__(identifier)
        self._vertices = [(float(x1), float(y1)),
                          (float(x2), float(y2)),
                          (float(x3), float(y3))]
        
        # Проверка невырожденности (площадь > 0)
        if self.area() <= 1e-10:
            raise InvalidShapeError(f"Треугольник {identifier} вырожден (площадь <= 0).")

    def _get_vertices(self):
        """Возвращает список вершин."""
        return self._vertices

    def area(self) -> float:
        """Вычисление площади треугольника по формуле Герона."""
        x1, y1 = self._vertices[0]
        x2, y2 = self._vertices[1]
        x3, y3 = self._vertices[2]
        return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)

    def move(self, dx: float, dy: float):
        """Перемещение треугольника."""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise InvalidMoveError("Смещение должно быть числом.")
        self._vertices = [(x + dx, y + dy) for (x, y) in self._vertices]

    def _point_in_triangle(self, px, py) -> bool:
        """Проверяет, находится ли точка внутри треугольника."""
        def sign(p1, p2, p3):
            return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
        
        v1, v2, v3 = self._vertices
        d1 = sign((px, py), v1, v2)
        d2 = sign((px, py), v2, v3)
        d3 = sign((px, py), v3, v1)
        
        has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
        has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
        
        return not (has_neg and has_pos)

    def _segments_intersect(self, p1, p2, p3, p4) -> bool:
        """Проверяет пересечение двух отрезков."""
        def orientation(p, q, r):
            val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
            if abs(val) < 1e-10:
                return 0
            return 1 if val > 0 else 2
        
        o1 = orientation(p1, p2, p3)
        o2 = orientation(p1, p2, p4)
        o3 = orientation(p3, p4, p1)
        o4 = orientation(p3, p4, p2)
        
        if o1 != o2 and o3 != o4:
            return True
        
        # Проверка коллинеарности
        if o1 == 0 and self._on_segment(p1, p3, p2):
            return True
        if o2 == 0 and self._on_segment(p1, p4, p2):
            return True
        if o3 == 0 and self._on_segment(p3, p1, p4):
            return True
        if o4 == 0 and self._on_segment(p3, p2, p4):
            return True
        
        return False
    
    def _on_segment(self, p, q, r):
        """Проверяет, лежит ли точка q на отрезке pr."""
        return (min(p[0], r[0]) <= q[0] <= max(p[0], r[0]) and
                min(p[1], r[1]) <= q[1] <= max(p[1], r[1]))

    def is_intersect(self, other: Shape) -> bool:
        """Проверяет пересечение треугольника с прямоугольником."""
        if not isinstance(other, Rectangle):
            raise TypeError("Метод is_intersect для Triangle реализован только с Rectangle.")
        
   
        rect_vertices = other._get_vertices()
        
     
        tri_edges = [(self._vertices[i], self._vertices[(i+1)%3]) for i in range(3)]
        rect_edges = [(rect_vertices[i], rect_vertices[(i+1)%4]) for i in range(4)]
        
        for t_edge in tri_edges:
            for r_edge in rect_edges:
                if self._segments_intersect(t_edge[0], t_edge[1], r_edge[0], r_edge[1]):
                    return True
        
        
        for v in self._vertices:
            if other._point_in_rectangle(v[0], v[1]):
                return True
        
        
        for v in rect_vertices:
            if self._point_in_triangle(v[0], v[1]):
                return True
        
        return False

    def __repr__(self):
        return f"Triangle(id='{self.id}', vertices={self._vertices})"



class Rectangle(Shape):
    """Прямоугольник, заданный координатами противоположных углов (оси aligned)."""

    def __init__(self, identifier: str, x1, y1, x2, y2):
        super().__init__(identifier)
        self._x1 = float(min(x1, x2))
        self._y1 = float(min(y1, y2))
        self._x2 = float(max(x1, x2))
        self._y2 = float(max(y1, y2))
        
        # Проверка, что это не вырожденный прямоугольник
        if abs(self._x2 - self._x1) < 1e-10 or abs(self._y2 - self._y1) < 1e-10:
            raise InvalidShapeError(f"Прямоугольник {identifier} вырожден (нулевая площадь).")

    def _get_vertices(self):
        """Возвращает вершины прямоугольника в порядке обхода."""
        return [(self._x1, self._y1),
                (self._x2, self._y1),
                (self._x2, self._y2),
                (self._x1, self._y2)]

    def area(self) -> float:
        """Площадь прямоугольника."""
        return abs(self._x2 - self._x1) * abs(self._y2 - self._y1)

    def move(self, dx: float, dy: float):
        """Перемещение прямоугольника."""
        if not isinstance(dx, (int, float)) or not isinstance(dy, (int, float)):
            raise InvalidMoveError("Смещение должно быть числом.")
        self._x1 += dx
        self._x2 += dx
        self._y1 += dy
        self._y2 += dy

    def _point_in_rectangle(self, px, py) -> bool:
        """Проверяет, находится ли точка внутри прямоугольника."""
        return (self._x1 - 1e-10 <= px <= self._x2 + 1e-10 and
                self._y1 - 1e-10 <= py <= self._y2 + 1e-10)

    def is_intersect(self, other: Shape) -> bool:
        """Проверяет пересечение прямоугольника с треугольником."""
        if not isinstance(other, Triangle):
            raise TypeError("Метод is_intersect для Rectangle реализован только с Triangle.")
        
        # Используем уже реализованный метод треугольника
        return other.is_intersect(self)

    def __repr__(self):
        return f"Rectangle(id='{self.id}', x=[{self._x1},{self._x2}], y=[{self._y1},{self._y2}])"



def main():
    print("=" * 60)
    print("Лабораторная работа №3. Вариант 4")
    print("T1 = Triangle, T2 = Rectangle")
    print("Методы: move, is_intersect")
    print("=" * 60)
    
    # Создание объектов
    print("\n1. Создание фигур:")
    try:
        # Создаем треугольник
        triangle1 = Triangle("T1", 0, 0, 4, 0, 2, 3)
        print(f"  ✓ {triangle1}")
        print(f"    Площадь: {triangle1.area():.2f}")
        
        # Создаем прямоугольник
        rect1 = Rectangle("R1", 1, 1, 3, 2)
        print(f"  ✓ {rect1}")
        print(f"    Площадь: {rect1.area():.2f}")
        
        # Создаем второй прямоугольник (не пересекается с треугольником)
        rect2 = Rectangle("R2", 5, 5, 7, 6)
        print(f"  ✓ {rect2}")
        print(f"    Площадь: {rect2.area():.2f}")
        
        # Создаем третий прямоугольник (внутри треугольника)
        rect3 = Rectangle("R3", 1.5, 0.5, 2.5, 1.5)
        print(f"  ✓ {rect3}")
        print(f"    Площадь: {rect3.area():.2f}")
        
    except InvalidShapeError as e:
        print(f"  ✗ Ошибка: {e}")
        return
    
    # Проверка пересечения
    print("\n2. Проверка пересечения (is_intersect):")
    print(f"  Triangle T1 ∩ Rectangle R1: {triangle1.is_intersect(rect1)}")
    print(f"  Triangle T1 ∩ Rectangle R2: {triangle1.is_intersect(rect2)}")
    print(f"  Triangle T1 ∩ Rectangle R3: {triangle1.is_intersect(rect3)}")
    
    # Перемещение фигур
    print("\n3. Перемещение фигур (move):")
    print(f"  До перемещения: {triangle1}")
    triangle1.move(2, 1)
    print(f"  После move(2, 1): {triangle1}")
    print(f"  Площадь треугольника не изменилась: {triangle1.area():.2f}")
    
    print(f"\n  До перемещения: {rect1}")
    rect1.move(-0.5, -0.5)
    print(f"  После move(-0.5, -0.5): {rect1}")
    print(f"  Площадь прямоугольника не изменилась: {rect1.area():.2f}")
    
    # Проверка пересечения после перемещения
    print("\n4. Проверка пересечения после перемещения:")
    print(f"  Triangle T1 ∩ Rectangle R1: {triangle1.is_intersect(rect1)}")
    
    # Демонстрация обработки ошибок
    print("\n5. Обработка ошибочных ситуаций:")
    
    # Ошибка: вырожденный треугольник
    try:
        bad_triangle = Triangle("Bad", 0, 0, 1, 1, 2, 2)
    except InvalidShapeError as e:
        print(f"  ✓ Поймана ошибка: {e}")
    
    # Ошибка: вырожденный прямоугольник
    try:
        bad_rect = Rectangle("Bad", 0, 0, 0, 5)
    except InvalidShapeError as e:
        print(f"  ✓ Поймана ошибка: {e}")
    
    # Ошибка: некорректное перемещение
    try:
        triangle1.move("abc", 5)
    except InvalidMoveError as e:
        print(f"  ✓ Поймана ошибка: {e}")
    
    # Ошибка: пустой идентификатор
    try:
        bad_shape = Triangle("", 0, 0, 1, 0, 0, 1)
    except InvalidShapeError as e:
        print(f"  ✓ Поймана ошибка: {e}")
    
    # Ошибка: неправильный тип при пересечении
    try:
        triangle1.is_intersect(rect2)  # здесь norm
        print(triangle1.is_intersect(triangle1))  # здесь ошибка
    except TypeError as e:
        print(f"  ✓ Поймана ошибка: {e}")
    
    print("\n" + "=" * 60)
    print("Программа успешно завершена!")


if __name__ == "__main__":
    main()
