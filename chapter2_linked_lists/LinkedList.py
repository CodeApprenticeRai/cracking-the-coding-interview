from cgi import test
from email import header
from operator import index

from pyrsistent import inc


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head_value=None):
        self.head = None
        # self.tail = None
        if (head_value != None):
            self.head = LinkedListNode(head_value)
            # self.tail = self.head

    def get_head(self):
        return self.head    
    
    def set_head(self, temp):
        self.head = temp
        return self.head

    def insert(self, value):
        curr = self.get_head()
        while ((curr) and (curr.next != None)):
            curr = curr.next
        if (curr==None):
            curr = LinkedListNode(value)
            # self.tail = curr
        else:
            curr.next = LinkedListNode(value)
            # self.tail = curr.next
        return id(curr.next)
    
    def get_by_id(self, _id):
        curr = self.get_head()
        while ((curr != None) and (id(curr) != _id)):
            curr = curr.next
        return curr

    def delete_by_id(self, _id):
        curr = self.get_head()
        while ((curr) and (curr.next != None) and (id(curr.next) !=_id)):
            curr = curr.next
        if (curr.next != None):
            temp = curr.next
            curr.next = curr.next.next
            del temp
            return True
        else:
            return False

    def delete_by_value(self, value):
        curr = self.get_head()
        did_delete_node = False
        while((curr)):
            if (curr.value == value):
                if (curr.next):
                    temp = curr.next
                    del curr
                    did_delete_node = True
                    curr = temp
        return did_delete_node
    
    def remove_duplicates(self):
        raise NotImplementedError
        curr = self.get_head()
        cache = set()
        while ((curr != None) and (curr.next != None)):
            if curr.next.value not in cache:
                cache.add(curr.value)
            else:
                temp = curr.next
                curr.next = curr.next.next
                del temp
            curr = curr.next
        return None

    # kth_to_last(k) returns the last element
    def kth_to_last(self, k):
        indexor = []
        curr = self.get_head()
        node_count = 0
        while (curr != None):
            node_count += 1
            curr = curr.next
        curr = self.get_head()
        for i in range(k):
            curr = curr.next
        return curr 

    def to_array(self):
        curr = self.get_head()
        array = []
        while(curr != None):
            array.append(curr)
            curr = curr.next
        return array

    def delete_middle_node(self):
        list_as_array = self.to_array()
        if (len(list_as_array) == 0):
            return None # should be equivalent to self.get_head()
        #delete the len(list)//2
        index_to_delete = int(len(list_as_array) // 2)
        
        #get prev
        #set prev.next = list_as_array[index_to_delete].next
        #case: deleting head
        if (index_to_delete == 0):
            # prev = None
            self.set_head(None)
            del list_as_array[index_to_delete]
        #case not deleting head
        else:
            #if index_to_delete > 0 -> len(list_as_array) >= 2
            prev = list_as_array[index_to_delete-1]
            prev.next = list_as_array[index_to_delete].next
            del list_as_array[index_to_delete]
        return self.get_head()

    def delete_middle_node_constant_space(self):
        curr = self.get_head()
        
        if (curr == None):
            return None
        if (curr.next == None):
            self.set_head(None)
            return self.get_head()

        fast_ptr = curr
        slow_ptr = curr
        prev = None

        while ((fast_ptr != None) and
                (fast_ptr.next != None)):
                fast_ptr = fast_ptr.next.next
                prev = slow_ptr
                slow_ptr = slow_ptr.next
        
        prev.next = slow_ptr.next
        del slow_ptr
        return self.get_head()
        

    def print_list(self):
        curr = self.get_head()
        while ((curr)):
            print(curr.value, end="->")
            curr = curr.next
        print("None")
        return None

if __name__=="__main__":
    test_list = LinkedList(0)
    import random
    random.seed(0)

    node_ids = [ test_list.insert(i) for i in range(1,10) ]
    test_list.print_list()
    test_list.delete_by_id(node_ids[3]) #deletes 3
    test_list.print_list()


    