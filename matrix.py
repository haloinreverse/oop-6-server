
from rational import TRational
from complex import TComplex
import copy


class Matrix:
    # задаём матрицу по умолчанию - единичная матрица 3х3
    # данные самой матрицы - private, поэтому два нижних подчёркивания перед data
    def __init__(self, number):
        self.__data = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        self.number = number


    # опредяляем метод для того, чтобы получать элемент матрицы через [][]
    def __getitem__(self, item: int):
        return self.__data[item]

    # метод, возвращающий число строк в матрице
    def get_number_of_rows(self):
        return len(self.__data)

    # метод, возвращающий число столбцов в матрице
    def get_number_of_columns(self):
        return len(self.__data[0])

    # публичный метод для нахождения определителя матрицы
    def det(self):
        return 'Не существует'

    # публичный метод для вывода матрицы на печать
    def print(self):
        print('Матрица:')
        for i in range(self.get_number_of_rows()):
            for j in range(self.get_number_of_columns()):
                print(self[i][j], end=' ')
            print('\n')
        print('')

    # публичный метод для расчёта ранга матрицы
    def rank(self):
        n = self.get_number_of_columns()
        m = self.get_number_of_rows()
        data = copy.deepcopy(self.__data)
        rank = max(n, m)
        lines = [False for x in range(n)]
        for i in range(0, n):
            for j in range(0, m):
                if self.number == TComplex:
                    if (not lines[j]) and (abs(data[j][i]) > 0):
                        break
                else:
                    if (not lines[j]) and (abs(data[j][i]) > self.number(0)):
                        break
            if j == n:
                rank = rank - 1
            else:
                lines[j] = True
                for p in range(i + 1, n):
                    data[j][p] = data[j][p] / data[j][i]
                for k in range(0, m):
                    if self.number == TComplex:
                        if (k != j) and (abs(data[k][i]) > 0):
                            for p in range(i + 1, m):
                                data[k][p] = data[k][p] - data[j][p] * data[k][i]
                    else:
                        if (k != j) and (abs(data[k][i]) > self.number(0)):
                            for p in range(i + 1, m):
                                data[k][p] = data[k][p] - data[j][p] * data[k][i]
        return rank

    def transpose(self):
        n = self.get_number_of_columns()
        m = self.get_number_of_rows()
        new_matrix = [[0 for j in range(m)] for i in range(n)]
        for i in range(n):
            for j in range(m):
                new_matrix[i][j] = self.__data[j][i]
        self.__data = new_matrix

    def set_data(self, data):
        self.__data = data
