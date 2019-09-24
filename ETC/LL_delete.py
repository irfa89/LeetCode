
class Node:

    def __init__(self,data):
        """
        constructor to
        :param data:
        """
        self.data = data
        self.next = None


class linked_list:

    def __init__(self):
        self.head = None

    # insert a new_node at the beginning
    def push(self,new_data):

        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # taking the reference to the head of a list
    # and key, delete the first occurence of key in linked list
    def deleteNode(self,key):

        # store head node
        temp = self.head

        # if head node itself holds the key to be deleted
        if (temp is not None):
            if(temp.data == key):
                self.head = temp.next
                temp = None
                return

        # Serach for the key to be deleted, keep track of the
        # previous node as we need to change 'prev.next'
        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        # if key was not present in linked List
        if(temp == None):
            return

        #Unlike the node from linked list
        prev.next = temp.next
        temp = None


    def prinList(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next




def main():
    ll = linked_list()
    ll.push(5)
    ll.push(2)
    ll.push(7)
    ll.push(4)

    ll.prinList()
    print("------------------")
    ll.deleteNode(2)
    ll.deleteNode(4)

    ll.prinList()
    print("------------------")

if __name__ == "__main__":
    main()








