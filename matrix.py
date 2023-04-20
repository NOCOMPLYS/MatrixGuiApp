from copy import copy
from rational import TRational

class matrix():

    def __init__(self):
        self.__matrix_array = []

    def is_empty(self):
        return not bool(len(self.__matrix_array))

    def get_matrix_array(self):
        return self.__matrix_array

    def fill_in_matrix(self, matrix_size, elements):
        self.__matrix_array = [[] for i in range(matrix_size)]
        element_id = 0
        for i in range(matrix_size):
            while element_id < matrix_size * (i + 1):
                self.__matrix_array[i].append(elements[element_id])
                element_id += 1
            element_id = (i + 1) * matrix_size

    def __output(self, matrix_array):
        matrix_text = '\n'.join([''.join(['{:12}'.format(item.value.text_representation) for item in row]) for row in matrix_array])
        print(matrix_text) 

    def output_original(self):
        matrix_text = '\n'.join([''.join(['{:12}'.format(item.value.text_representation) for item in row]) for row in self.__matrix_array])
        print(matrix_text) 

    def determinant_rec(self, matrix):
        if isinstance(matrix[0][0].value, float):
            det = 0
        elif isinstance(matrix[0][0].value, TRational):
            det = TRational(0, 1)
        match ln := len(matrix):
            case 1:
                return matrix[0][0].value
            case 2:
                return matrix[0][0].value * matrix[1][1].value - matrix[0][1].value * matrix[1][0].value
            case _:
                if isinstance(matrix[0][0].value, float):
                    for k in range(ln):
                        det += matrix[0][k].value * (-1.0) ** float(k) * self.determinant_rec([matrix[i][:k] + matrix[i][k+1:] for i in range(1,ln)])
                elif isinstance(matrix[0][0].value, TRational):
                    for k in range(ln):
                        det += matrix[0][k].value * (-1) ** k * self.determinant_rec([matrix[i][:k] + matrix[i][k+1:] for i in range(1,ln)])
        
        return det

    def determinant(self):
        matrix = copy(self.__matrix_array)
        det = self.determinant_rec(matrix)
        if isinstance(matrix[0][0].value, float):
            return str(det)
        elif isinstance(matrix[0][0].value, TRational):
            return det.text_representation

    def transpose(self):
        transposed_matrix = [[] for i in range(len(self.__matrix_array))]
        for i in range(len(self.__matrix_array)):
            for j in range(len(self.__matrix_array)):
                transposed_matrix[i].append(self.__matrix_array[j][i])

        return transposed_matrix

    def swap(self, Matrix, row1, row2, col):
        for i in range(col):
            temp = Matrix[row1][i].value
            Matrix[row1][i].value = Matrix[row2][i].value
            Matrix[row2][i].value = temp

    def rank(self):
        matrix = copy(self.__matrix_array)
        size = len(matrix)
        rank = copy(size)
        for row in range(0, rank, 1):
            if matrix[row][row].value != 0:
                for col in range(0, size, 1):
                    if col != row:
                        multiplier = (matrix[col][row].value /
                                      matrix[row][row].value)
                        for i in range(rank):
                            matrix[col][i].value -= (multiplier *
                                               matrix[row][i].value)
            else:
                reduce = True
                for i in range(row + 1, size, 1):
                    if matrix[i][row].value != 0:
                        self.swap(matrix, row, i, rank)
                        reduce = False
                        break
                if reduce:
                    rank -= 1
                    for i in range(0, size, 1):
                        matrix[i][row].value = matrix[i][rank].value 
                row -= 1

        return str(rank)