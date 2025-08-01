#This is the blueprint for every node in the linked list

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

#Class LinkedList  is the class that controls the full Linked List
class LinkedList:
    def __init__(self):
        self.head = None # head referst to dirst node in the list. At first when the list is empty , head is set to none

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, datalist):
        self.head = None
        for data in datalist:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove(self, index):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid Index")
            
        
        if index ==0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
    
    def insert_at(self, index, data):
        if index<0 or index>= self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.insert_at_beginning(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index -1:
                node = Node (data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count = count + 1
                


if __name__== '__main__': # run the code  only if this file is running directly not being imported into another file
    l1 = LinkedList()
    l1.insert_values(["car","ball","warehouse"])
    l1.print()
    l1.insert_at(1,"wow")
    l1.insert_at(2,"bob")
    l1.insert_at(4,"Nothing is impossible")
    l1.print()
    print(l1.get_length())