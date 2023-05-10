# Связный список представляет собой еще одну реализацию списка как абстрактного типа данных.
# Вы можете добавлять, вставлять, удалять и искать элементы
# в связном списке таким же образом, как и в массиве.
# Однако у элементов связного списка нет индексов,
# потому что компьютер не хранит элементы в последовательных ячейках памяти.
# Вместо этого связный список имеет цепочку узлов,
# каждый из которых содержит фрагмент данных и информацию о местоположении следующего узла в цепи.
# Информация о местоположении следующего
# узла в связном списке называется указателем. Первый узел в связном списке
# называется головным. Указатель из последнего элемента в связном списке часто
# указывает на None, поэтому вы знаете, что это последний узел в списке

# Связному списку не нужно хранить узлы
# в последовательных ячейках памяти

# Существует много различных типов связных списков.
#
# Односвязный список — тип связного списка с указателями, которые указывают только на следующий элемент.
# В двусвязном списке у каждого узла есть два указателя: один указывает на следующий узел,
# а другой — на предыдущий.
# Это позволяет перемещаться по двусвязному списку в обоих направлениях
#
# В круговом связном списке последний узел указывает на первый узел,
# что позволяет переходить от последнего элемента списка обратно к началу

# Создание связного списка
# Применяем ООП
# Сначала создаём класс узла

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

# Затем уже создаём сам связной список

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data): # метод "добавить"
        if not self.head: # если нет головного узла
            self.head = Node(data) # то головной узел будет равен присвоенному значению
            return # возвращаем, т.е. заканчиваем функцию
        current = self.head # в противном случае создаём переменную котрой присваиваем значение головного узла
        while current.next: # пока есть следующий элемент
            current = current.next # наша созданная переменная будет равна следующему элементу
        current.next = Node(data) # после окончания цикла (когда будет найден последний элемент)
                                  # добавляем новое значение в конец связного списка

    def __str__(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next




from collections import deque
# импорт стандартного связного списка из встроенной библиотеки collections


if __name__ == '__main__':
    linked = LinkedList()
    linked.append('123')
    linked.append('456')
    print(linked)


    d = deque()

    d.append('First')
    d.append('Second')
    d.append('Third')

    for item in d:
        print(item)