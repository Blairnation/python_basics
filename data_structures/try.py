class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_array = Node(data)

        if not self.head:
            self.head = new_array
            return

        current = self.head
        while current.next:
            current = current.next
        current = new_array

    def display(self):
        current = self.head
        while current:
            print(current.data, end='->')
            current = current.next           
        print('None')








# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def append(self, data):
#         new_node = Node(data)
#         if not self.head:
#             self.head = new_node
#             return
#         current = self.head
#         while current.next:
#             current = current.next
#         current.next = new_node

#     def display(self):
#         current = self.head
#         while current:
#             print(current.data, end=" -> ")
#             current = current.next
#         print("None")

# # Create a linked list
# linked_list = LinkedList()
# linked_list.append(10)
# linked_list.append(20)
# linked_list.append(30)

# # Display the linked list
# linked_list.display()
