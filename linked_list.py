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
# Собственно, создаём))

class LinkedList:
    head = None
    length = 0

    class Node:
        element = None
        next_node = None

        def __init__(self, element, next_node=None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            self.length += 1
            return element
        node = self.head
        while node.next_node:
            node = node.next_node

        node.next_node = self.Node(element)
        self.length += 1

    def insert(self, element, index):
        count = 0
        node = self.head
        previously_node = self.head

        while count < index:
            previously_node = node
            node = node.next_node
            count += 1

        previously_node.next_node = self.Node(element, next_node=node)

        self.length += 1

        return element

    def assign(self, element, index):
        node = self.head
        count = 0

        while count < index:
            node = node.next_node
            count += 1

        node.element = element

    def delete(self, index):
        if index == 0:
            self.head = self.head.next_node

        node = self.head
        count = 0
        previously_node = node

        while count < index:
            previously_node = node
            node = node.next_node
            count += 1

        previously_node.next_node = node.next_node
        element = node.element

        del node
        self.length -= 1

    def get(self, index):
        count = 0
        node = self.head
        previously_node = self.head

        while count < index:
            previously_node = node
            node = node.next_node
            count += 1

        return node.element

    def out(self):
        node = self.head

        while node:
            print(node.element)
            node = node.next_node




if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append(10)
    linked_list.append(20)
    linked_list.append(30)
    linked_list.insert(666, 2)
    linked_list.append(50)
    linked_list.append(100)
    linked_list.delete(2)
    print('\n')
    linked_list.append('Complete!')
    linked_list.assign('More complete!', 5)
    linked_list.assign(999, 0)
    a = linked_list.get(5)

    linked_list.out()
    print(linked_list.get(2))

    print(a)

    print(linked_list.length)




