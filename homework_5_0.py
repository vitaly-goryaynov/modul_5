def length(array: list) -> int or str:
    """
    Функция считает длинну списка
    :param array: список
    :return: одно целое не отрицательное число
    """
    try:
        if isinstance(array, list):
            count = 0
            for i in range(0, len(array), 1):
                count = count + 1
            return count
        else:
            return 'Не правильный тип данных'
    except TypeError:
        return 0

print(length([1,3,'']))

# 1 + n * (1 + 1) + 1 = 2 + 2n -> O(n)


def find_max(array: list) -> int or float:
    """
    Функция находит максимальный элеммент в списке
    :param array: список чисел
    :return: максимальное число и индекс первого повторения
    """
    if len(array) == 0:
        return 0

    if isinstance(array, list):
        try:
            imax = 0
            for i in range(0, len(array), 1):
                if array[i] > array[imax]:
                    imax = i
            return array[imax], imax
        except TypeError:
            return 'Список должен состоять только из цифр'
    return 'На вход принимается только список чисел'

print(find_max([1]))
#


# 1 n * (1+1+1+1+1) + 1 = 2 + 5n -> O(n)


def reverse(array: list):  # input -> 1, 2, 3, 4; output -> 4, 3, 2, 1.
    """
    Функция выводит в обратном порядке список элементов
    :param array: список
    :return: элемент списка
    """
    if isinstance(array, list):
        lenght = len(array)
        if lenght <= 0:
            return 'Список пустой'
        for i in range(0, lenght // 2, 1):
            buff = array[i]
            array[i] = array[lenght - 1 - i]
            array[lenght - 1 - i] = buff
        return array
    return 'На вход не получен список'

array = []
print(reverse(array))
#
# # 1 + n * (6) + 1 = 2 + 6n -> O(n / 2)
#
def lianer_search(array, target) -> (int or -1):
    """
    Функция для поиска позиции элемента в списке, если его нет вывести -1
    :param array: Список
    :param target: одно целое не отрицательное число или -1
    :return: целое число
    """

    for i in range(0, len(array), 1):
        if array[i] == target:
            return i
    return -1
#
print(lianer_search([1,2,4,-1,'1'], 1))

# # Тестовый пример №1 для случая - лучший
# # Входные данные: array = [1, 2, 3], target = 1
# # Выходные данные: 0
# # Оценка: 1 + 1*(4) = 5 -> O(1)
#
# # Лучший 1 + n * (1 + 1 + 1 + 1) = 1 + 4n -> O(1)
# # Средний 1 + n * (1 + 1 + 1 + 1) = 1 + 4n -> O(n / 2)
# # Худший 1 + n * (1 + 1 + 1 + 1) = 1 + 4n -> O(n)
#
def binary_search(array: list, target) -> (int or -1):
    """
    Функция бинарного поиска
    :param array: список
    :param target: параметр поиска
    :return: одно целое число, если нет то -1
    """

    left = 0
    right = len(array) - 1

    index_target = -1

    while index_target == -1 and right > left:
        center = (right + left) // 2

        if array[center] == target:
            index_target = center
            break

        if target > array[center]:
            left = center + 1
        else:
            right = center - 1

    return index_target


array = [i for i in range(1, 15, 1)]
print(f"array: {array}")


print(binary_search(array, 5))

# # Лучший 1 + 1 + 1 + n->1 * (1+1+1) -> O(1)
# # Средний -> O(1) or O(n / 2) -> O(log(n))
# # Худший -> O(n / 2)
#
#
# # Тестовый пример №1
# # Выходные данные: 7+4+1+3+2 = 17 -- 1 + 7 = 8
# # Входные данные: number = 74132
#
# # Тестовый пример №2
# # Выходные данные: 4+1+3+2 = 10 -- 1 + 0 = 1
# # Входные данные: number = 4132
#
#
def some_function(number):

    if number <= 9:
        return number

    while number > 9:
        sum = 0
        while number != 0:
            sum += number % 10
            number //= 10
        number = sum
    return number


#