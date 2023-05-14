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

class LinkedList: # создаём класс односвязного списка
    head = None # начало списка по умолчанию пустой
    length = 0 # для вычисления длины списка - по умолчанию 0
    with_list = list() # на случай, если захочется все данные перевести в обычный список

    class Node: # создаём внутри класса списка класс узла
        element = None # узел имеет какой-то элемент внутри себя
        next_node = None # узел связан со следующим узлом

        def __init__(self, element, next_node=None): # инициализация узла, следующий узел по умолчанию - пуст (его нет)
            self.element = element # элемент узла будет равен заданному элементу
            self.next_node = next_node # следующий узел будет равен заданному следующему узлу

    def append(self, element): # метод добавления узлов в конец списка (а у узла внутри элемент, помним)
        if not self.head: # если нет даже первого элемента (узла)
            self.head = self.Node(element) # то добавляем узел(элемент) в начало списка
            self.length += 1 # добавляем длины для вычислений длины списка
            self.with_list.append(element) # добавляем элемент в обычный список
            return element # возвращаем этот элемент (необязательно)
        node = self.head # объявляем переменную узла и присваиваем ей значение первого элемента списка
        while node.next_node: # пока у узла есть следующий узел (элемент)
            node = node.next_node # узел равен следующему узлу

        node.next_node = self.Node(element) # когда следующего узла нет, добавляем следующий узел(элемент)
        self.length += 1 # увеличиваем длину для вычисления длины
        self.with_list.append(element) # добавляем элемент в обычный список


    def insert(self, element, index): # вставка элемента в список, параметры - добавляемый элемент и индекс списка
        count = 0 # счётчик нужен для цикла - что бы дойти до нужного нам индекса
        node = self.head # объявляем переменную узла и присваиваем ей первый элемент списка
        previously_node = self.head # объявляем переменную предыдущего узла и присваиваем ей первый элемент списка

        while count < index: # пока счётчик меньше заданного индекса
            previously_node = node # предыдущий узел равен узлу на данный момент
            node = node.next_node # узел на данный момент равен следующему узлу
            count += 1 # добавляем единицу к счётчику что бы избежать бесконечный цикл и "бежать" по списку

        previously_node.next_node = self.Node(element, next_node=node) # когда дошли до нужного нам индекса
        # присваиваем следующему узлу предыдущего узла нужный нам элемент в новом узле, следующий узле которого
        # будет узлом на данный момент

        self.length += 1 # увеличиваем длину списка так как добавили новый элемент
        self.with_list.append(element) # добавляем элемент в обычный список

        return element # возвращаем новый элемент (необязательно)

    def assign(self, element, index): # изменение элемента в списке
        node = self.head # объявляем узел и присваеиваем ему первый элемент списка
        count = 0 # объявляем счётчик что бы "бежать" по списку

        while count < index: # пока счётчик меньше нужного нам индекса
            node = node.next_node # узел равен следующему узлу ("бежим" по списку)
            count += 1 # счётчик прибавляем на единицу

        node.element = element # когда дошли до нужного нам индекса присваиваем элементу узла новый эелемент
        self.with_list[index] = element # меняем элемент в обычном списке

    def delete(self, index): # удаление узла (элемента, соответственно)
        if index == 0: # если индекс удаляемого элемента равен нулю, то
            self.head = self.head.next_node # начала списка будет следующим элементом после начала списка

        node = self.head # объявляем узел и присваиваем ему начало узла
        count = 0 # объявляем счётчик для "пробега" по списку
        previously_node = node # предыдущий узел равен нынешнему узлу

        while count < index: # надоело повторяться
            previously_node = node # предыдущий узел равен нынешнему узлу
            node = node.next_node # нынешний узел равен следующему узлу
            count += 1 # счётчик плюс один ("бежим" по списку)

        previously_node.next_node = node.next_node # следующему узлу предыдущего узла присваиваем следующий узел
        # нынешнего узла
        del self.with_list[index] # удаляем элемент в обычном списке

        del node # удаляем узел, так как связи уже присвоены
        self.length -= 1 # уменьшаем длину списка так как удалили один элемент

    def get(self, index): # получение элемента списка
        count = 0 # счётчик
        node = self.head # начало списка в объявленном узле
        previously_node = self.head # предыдущий тоже

        while count < index: # и снова надоело повторяться, и так, я думаю понятно что это :)
            previously_node = node
            node = node.next_node
            count += 1

        return node.element # возвращаем элемент до которого дошли (по заданному индексу)

    def out(self): # вывод односвязного списка
        node = self.head # задаём начало списка объявленной переменной

        while node: # пока если узлы
            print(node.element) # выводим узел
            node = node.next_node # переходим на следующий

    def get_list(self): # возвращение обычного списка из связного
        return self.with_list




# ниже основная программа и проверки (без тестов)

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
    my_list = linked_list.get_list()
    print(my_list)




