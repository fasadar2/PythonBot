import numpy as np
class GenerateMatrix:
    @staticmethod
    def Generate(transports_list):
        if len(transports_list) < 25:
            raise ValueError("Недостаточно элементов для создания матрицы 5x5")

        np.random.shuffle(transports_list)  # перемешиваем элементы списка
        matrix = np.array(transports_list[:25]).reshape(5, 5)  # создаем матрицу 5x5 из первых 25 элементов
        return matrix

