# List
#
# add_back(item) -> None добавить в конец эл
# add_front(item) -> None добавитиь в начало
# count(item) -> int считает количество элементов в списке
# find(item) -> int or -1 поиск первого вхождения элемента  индекс
# remove_to_item(item) -> bool удаляет первое вхождение числа в списке
# pop(index) -> int or Exception удаляет число по индексу
# insert_to_index(item, index) -> None вставка по индексу
# reverse() -> None инверсирует значения
# sort() сортирует список

class List:


    def __init__(self, size=2):
        """
        Конструктор создаёт объекты класса List
        :param size: выделяемая память
        """

        self.__size = size
        self.__count = 0
        self.__array = [None] * size


    def __str__(self):
        """
        Вывод списка на консоль
        :return: None
        """
        return f"{self.__array}"


    def get_array(self) -> list:
        """
        Возвращает список
        :return: список элементов
        """
        return self.__array


    def set_array(self, array: list[any]) -> None:
        """
        Добавляет элементы в список
        :param array: любой тип данных
        :return: список элементов
        """

        self.__array = array
        for i in self.__array:
            self.__count += 1


    def add_back(self, item: any) -> None:
        """
        Добавляет элемент в конец списка
        :param item: элемент любого типа данных
        :return: None
        """

        self.__add_size()

        self.__array[self.__count] = item
        self.__count += 1


    def add_front(self, item: any) -> None:
        """
        Добавляет элемент в начало списка
        :param item: элемент любого типа данных
        :return: None
        """

        self.__add_size()

        new_array = self.__array

        for i in range(self.__count, 0, -1):
            self.__array[i] = new_array[i-1]

        new_array[0] = item
        self.__count += 1


    def count(self, item: any) -> int:
        """
        Считает количество искомых элементов в списке
        :param item: элемент для поиска
        :return: целое не отрицательное число
        """

        if self.__count == 0:
            return 0

        count = 0

        for i in range(0, self.__size // 2, 1):
            if item == self.__array[i]:
                count += 1

            if item == self.__array[self.__size - 1 - i]:
                count += 1

        return count


    def find(self, item: int) -> int or -1:
        """
        Поиск первого вхождения элемента
        :return: индекс первого вхождения или -1
        """

        index = -1
        for i in self.__array:
            index += 1
            if i == item:
                return index
        return -1


    def remove_to_item(self, item: int) -> bool:
        """
        Удаляет первое вхождение числа в списке
        :param item: элемент, который нужно удалить
        :return: bool
        """

        count = 0
        for i in self.__array:
            count += 1
            if i == item:
                self.__array[:count:] = self.__array[:count-1:]
                self.__array = self.__array + [None]
                return True
        return False


    def insert_to_index(self, item:any, index:int) -> None:
        """
        Добавляет элемент в список по индексу
        :param item: элемент любого типа
        :param index: индекс для вставки
        :return: None
        """

        if index < 0 or index > self.__count:
            raise Exception("Error!")

        self.__add_size()

        for i in range(self.__count, index, -1):
            self.__array[i] = self.__array[i-1]

        self.__array[index] = item


    def reverse(self) -> None:
        """
        Инверсирует список
        :return: None
        """

        for i in range(0, self.__count // 2, 1):
            self.__array[i], self.__array[self.__count - i] = self.__array[self.__count - i], self.__array[i]


    def pop(self, index: int) -> any:
        """
        Удаляет элемент по индексу
        :param index: целое число
        :return: удалённый элемент
        """

        if index < 0 or index > self.__size:
            raise Exception("errro!")

        target_elem = self.__array[index]

        for i in range(self.__count, index, -1):
            self.__array[i] = self.__array[i + 1]

        self.__array[self.__count - 1] = None

        return target_elem


    def sort(self) -> list[int or float]:
        """
        Сортирует спиcок с числами по возростанию
        :return: None
        """

        for i in range(0, self.__count, 1):
            min_index = i

            for j in range(i+1, self.__count, 1):
                if self.__array[min_index] > self.__array[j]:
                    min_index = j
            self.__array[i], self.__array[min_index] = self.__array[min_index], self.__array[i]
        return self.__array


    def __malloc(self) -> (int, list):
        """
        Выделяет резерную память
        :return: обновлённый список со свободными ячейками
        """

        new_size = self.__size + (self.__size // 2) + 1
        new_array = [None] * new_size

        return (new_size, new_array)



    def __add_size(self) -> None:
        """
        Вызывает проверку на наличие свободных ячеек
        :return: None
        """

        if self.__count == self.__size:
            new_size, new_array = self.__malloc()

            for i in range(0, self.__size, 1):
                new_array[i] = self.__array[i]

            self.__size = new_size
            self.__array = new_array




l = List()
l.set_array([8, 9])
l.add_front(5)
l.add_front(2)
l.add_front(3)
l.add_front(1)
# print(l)
# # l.insert_to_index(22, 0)
# print(l)
# print(l.pop(0))
# print(l.find(1))
# print(l.remove_to_item(1))
# print(l)

print(l.sort())
