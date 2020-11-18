class DoubleNode:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DoubleNode(data)

        new_node.next = None

        if self.head == None:
            new_node.previous = None
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

        new_node.previous = last_node
        return

    def length(self):
        if self.head == None:
            return 0
        current_node = self.head
        total = 0
        while current_node:
            total += 1
            current_node = current_node.next
        return total

    def to_list(self):

        node_data = []
        current_node = self.head

        while current_node:
            node_data.append(current_node.data)
            current_node = current_node.next
        return node_data

    def display(self):
        contents = self.head
        if contents is None:
            print("nao à elementos")
        while contents:
            print(contents.data)
            contents = contents.next
        print("----------")

    def insert_at_start(self, data):
        if self.head == None:
            new_node = DoubleNode(data)
            self.head = new_node
            return
        new_node = DoubleNode(data)
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    def insert_at_end(self, data):
        if self.head == None:
            new_node = DoubleNode(data)
            self.head = new_node
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        new_node = DoubleNode(data)
        current_node.next = new_node
        new_node.previous = current_node


    def remove_at_start(self):
        if self.head == None:
            print("nao à elementos")
            return
        if self.head.next == None:
            self.head = None
            return
        self.head = self.head.next
        self.start_prev = None


    def remove_at_end(self):
        if self.head == None:
            print("nao à elementos")
            return
        if self.head.next == None:
            self.head = None
            return
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.previous.next = None

    def remove_element_by_value(self, value):
        if self.head == None:
            print("nao à elementos ")
            return
        if self.head.next == None:
            if self.head.item == value:
                self.head = None
            else:
                print("erro")
            return

        if self.head.data == value:
            self.head = self.head.next
            self.head.previous = None
            return

        current_node = self.head
        while current_node.next != None:
            if current_node.data == value:
                break
            current_node = current_node.next
        if current_node.next != None:
            current_node.previous.next = current_node.next
            current_node.next.previous = current_node.previous
        else:
            if current_node.data == value:
                current_node.previous.next = None
            else:
                print("nao à elementos")

    def clear(self):
        self.head = None
        self.tail = None

my_list = DoublyLinkedList()
my_list.display()
my_list.append(3)
my_list.append(2)
my_list.append(7)
my_list.append(1)

my_list.display()

print("o numero total de elementos na lista e " + str(my_list.length()))
print(my_list.to_list())
print("---------")

my_list.display()

my_list.remove_at_start()
my_list.display()

my_list.remove_at_end()
my_list.display()

my_list.insert_at_start(1)
my_list.display()

my_list.insert_at_end(3)
my_list.display()

my_list.remove_element_by_value(7)
my_list.display()

my_list.clear()
my_list.display()