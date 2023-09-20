class Node:
    def __init__(self,val=None,next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None
    
    def print(self):
        if self.head == None:
            print("linked_list is empty!")
            return
        
        lis = []
        node = self.head
        while node:
            lis.append(node.val)
            node = node.next
        print(lis)
        return
    
    def len(self):
        num = 0
        node = self.head
        while node:
            if node.next == None:
                return num
            node = node.next
            num+=1
        return num

    def insert_at_beginning(self,val):
        if self.head == None:
            node = Node(val,None)
            self.head = node
            return
        
        node = Node(val,self.head)
        self.head = node
        return

    def insert_at_end(self,val):
        if self.head == None:
            node = Node(val,None)
            self.head = node
            return
        
        node = self.head
        while node:
            if node.next == None:
                node.next = Node(val,None)
                return
            node = node.next

    def insert_at_index(self,val,index):
        if (self.head == None) or (0 > index) or  (index > self.len()+1):
            raise IndexError("index is not valid!")
        
        num = 0
        node = self.head
        while node:
            if num+1 == index:
                node.next = Node(val,node.next)
                return
            num+=1
            node = node.next

    def insert_after_value(self,value,previous_value):
        if self.head == None:
            raise ValueError("invalid argument!")

        node = self.head 
        while node:
            if node.val == previous_value:
                node.next = Node(value,node.next)
                return
            node = node.next

        raise ValueError("invalid argument, value not found!")
    
    def insert_values (self,values):
            for i in values:
                self.insert_at_end(i)
            return

    def remove_by_value(self,value):
        if self.head == None:
            raise ValueError("invalid argument!")

        node = self.head
        while node:
            if node.next.val == value:
                node.next = node.next.next
                return
            node = node.next
    
    

        

linked_list = LinkedList()