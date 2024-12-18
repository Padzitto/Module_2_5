# Объявите функцию get_matrix и напишите в ней параметры размеров n(строк), m(столбцов) и value(значений).
def get_matrix(n, m, value):
    matrix = []  # Создайте пустой список Matrix внутри функции get_matrix.

    for i in range(n):  # Напишите первый(внешний) цикл for для кол-ва строк матрицы, n повторов.
        matrix_ = []  # В первом цикле добавляйте пустой список в список matrix_.

        for j in range(m):  # Напишите второй(внутренний) цикл for для кол-ва столбцов матрицы, m повторов.
            matrix_.append(value)  # Во втором цикле пополняйте ранее добавленный пустой список значениями value.

        matrix.append(matrix_)  # Добавляем строку в матрицу

    return matrix  # После всех циклов верните значение переменной matrix.

# Исходный код:
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод на консоль:
print(result1)  # [[10, 10], [10, 10]]
print(result2)  # [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
print(result3)  # [[13, 13], [13, 13], [13, 13], [13, 13]]
