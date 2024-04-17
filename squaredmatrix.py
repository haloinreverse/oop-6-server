import copy
from rational import TRational
from matrix import Matrix



# описываем класс "Квадратная матрица"
class SquaredMatrix(Matrix):
    # задаём матрицу по умолчанию - единичная матрица 3х3
    # данные самой матрицы - private, поэтому два нижних подчёркивания перед data
    def __init__(self, number):
        super().__init__(number)

    # метод получения k-ого минора
    def __get_minor(self, data, k):
        res = []
        for r in data[1:]:
            row = []
            for j in range(len(r)):
                if j != k:
                    row.append(r[j])
            res.append(row)
        return res

    # рекурсивный метод для вычисления определителя матрицы
    def det_count(self, data):
        n = len(data)
        if n == 2:
            return data[0][0] * data[1][1] - data[0][1] * data[1][0]
        s = self.number(0)
        z = self.number(1)
        for i in range(n):
            s = s + z * data[0][i] * self.det_count(self.__get_minor(data, i))
            z = -z
        return s

    # публичный метод для нахождения определителя матрицы
    def det(self):
        return self.det_count(self._Matrix__data)
