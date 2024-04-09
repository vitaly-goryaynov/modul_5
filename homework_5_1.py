# def find_max_in_digit(digit:int) -> int or None:
#     """
#     Функция находит максимальную цифру в целом числе, если ее нет выводит None
#     :return: целое цисло или None
#     """
#     if not isinstance(digit, int):
#             return
#     digit = str(digit)
#     max = digit[0]
#     for i in digit:
#         if i >= max[0]:
#             max = i
#     return max
#
#
# def inverter_index_list(array:list, left_index: int, right_index:int):
#     """
#     Функция инвертирует список по заданным индексам
#     :param array: список чисел и 2 натуральных числа
#     :return: инвертированный список или None
#     """
#     lst1 = array[:left_index]
#     lst2 = array[left_index:right_index+1:]
#     lst3 = array[right_index+1:]
#     rev = lst2[::-1]
#     lst2 = rev
#     array = lst1+lst2+lst3
#     return array
#
# array = [11,12,13,14,15,16,17,18,19]
# print(inverter_index_list(array, 2, 7))
#
#
# def output_digit_Fibonachi(inp:int) -> [int] or int:
#     """
#     Функция выводит все числа Фибоначи до введенного натурального числа
#     :return: числа Фибоначи или -1
#     """
#     a = 0
#     b = 1
#     summ = 0
#     lst = []
#     lst.append(a)
#
#     while inp >= summ:
#         summ = a + b
#         a = b
#         b = summ
#         lst.append(a)
#
#     if not inp in lst:
#         print(-1)
#         return
#
#     print(*lst)
#
# output_digit_Fibonachi(609)
#
#
# def summ_elem_two_aray(array1: list[int], array2: list[int]) -> list[int] or None:
#     """
#     Функция складывает элементы двух списков
#     :return: список с элементами или None
#     """
#     array3 = []
#     if not isinstance(array1, int):
#         return
#     if not isinstance(array2, int):
#         return
#     if len(array1) != len(array2):
#         return
#     if len(array1) == 0 or len(array2) == 0:
#         return
#
#     for i in range(len(array1)):
#         for j in range(len(array2)):
#             summ = array1[i] + array2[i]
#         array3.append(summ)
#     return array3
#
#
# array1 = []
# array2 = []
# print(summ_elem_two_aray(array1, array2))


# def arithmetic_mean():
#     """
#     Функция находит среднее арифметическое элементов, соответствующих предикату
#     :return: целое число или None
#     """
