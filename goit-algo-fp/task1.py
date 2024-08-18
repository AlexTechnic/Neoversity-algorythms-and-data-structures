""" Модуль, що містить класи для роботи з однозв'язним списком (linked list), 
такі як вставка, видалення, пошук, реверсування та сортування вставками. """


class Node:
    """ Клас, що представляє вузол однозв'язного списку """
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    """ Клас, що представляє однозв'язний список """
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        """ Функція для вставки вузла в початок списку """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """ Функція для вставки вузла в кінець списку """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        """ Функція для вставки вузла після заданого вузла """
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        """ Функція для видалення вузла за ключем """
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        """ Функція для пошуку вузла за даними """
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        """ Функція для виведення списку на екран """
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


    def reverse(self):
        """ Функція для реверсування однозв'язного списку """
        prev = None
        current = self.head
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


    def insertion_sort(self):
        """ Функція для сортування однозв'язного списку вставками """
        sorted_list = None
        current = self.head
        while current:
            next_node = current.next
            if sorted_list is None or sorted_list.data >= current.data:
                current.next = sorted_list
                sorted_list = current
            else:
                temp = sorted_list
                while temp.next is not None and temp.next.data < current.data:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
            current = next_node
        self.head = sorted_list


    @staticmethod
    def merge_sorted_lists(list1, list2):
        """ Функція для об'єднання двох відсортованих списків в один відсортований список """
        dummy = Node()
        tail = dummy

        while list1 and list2:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        if list1:
            tail.next = list1
        else:
            tail.next = list2

        return dummy.next


# Приклад використання
if __name__ == "__main__":

    # Створення зв'язного списку
    llist = LinkedList()
    llist.insert_at_beginning(3)
    llist.insert_at_end(7)
    llist.insert_at_end(1)
    llist.insert_at_end(4)
    llist.insert_at_end(9)

    print("Оригінальний зв'язний список:")
    llist.print_list()


    # Реверсування зв'язного списку (перевертання)
    llist.reverse()
    print("\nРеверсований зв'язний список:")
    llist.print_list()


    # Сортування зв'язного списку вставками (insertion sort)
    llist.insertion_sort()
    print("\nВідсортований зв'язний список:")
    llist.print_list()


    # Об'єднання двох відсортованих списків в один відсортований список
    list1 = LinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(3)
    list1.insert_at_end(5)

    list2 = LinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(4)
    list2.insert_at_end(6)

    merged_head = LinkedList.merge_sorted_lists(list1.head, list2.head)
    merged_list = LinkedList()
    merged_list.head = merged_head

    # Виведення об'єднаного списку
    print("\nОб'єднаний відсортований список (list1 та list2):")
    merged_list.print_list()


""" Результат виконання:

Оригінальний зв'язний список:
3 -> 7 -> 1 -> 4 -> 9 -> None     

Реверсований зв'язний список:     
9 -> 4 -> 1 -> 7 -> 3 -> None     

Відсортований зв'язний список:    
1 -> 3 -> 4 -> 7 -> 9 -> None     

Об'єднаний відсортований список:  
1 -> 2 -> 3 -> 4 -> 5 -> 6 -> None
"""
