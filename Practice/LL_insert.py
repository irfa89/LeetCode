
class Node:

    def __init__(self,data):
        self.data = data           # Assigns data.
        self.next = None           # Initialize next as Null.

class linked_list:

    def __init__(self):
        self.head = None  # Funtion to initialize linked List object.

    # The function prints the content of linked list starting from head.
    def prinList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next

    def push(self,new_data):

        # Allocates the new node and put in data
        new_node = Node(new_data)

        # Make the next of new node as head
        new_node.next = self.head

        # Move the head to point to new node
        self.head = new_node

    def insertAfter(self,prev_node,new_data):

        #check if the given prev_node exists
        if prev_node is None:
            print("Does not exists")
            return

        # create new node and put in data
        new_node = Node(new_data)

        # Make next of new node as next of prev_node
        new_node.next = prev_node.next

        # make the next of prev_node as new_node
        prev_node.next = new_node

    def append(self,new_data):

        # create a new node,put data,set next as none
        new_node = Node(new_data)

        # if the linked list is empty, then new_node as head.
        if self.head is None:
            self.head = new_node
            return

        # else traverse till last node
        last = self.head
        while(last.next):
            last = last.next

        # change the next of last node
        last.next = new_node






def main():
    ll = linked_list()
    ll.head = Node(1)
    n2 = Node(2)
    n3 = Node(3)    # Nodes created

    ll.head.next = n2
    n2.next = n3

    ll.prinList()



if __name__ == "__main__":
    main()