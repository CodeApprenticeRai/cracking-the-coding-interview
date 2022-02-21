from cgi import test


class LinkedListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head_value=None):
        self.head = None
        self.tail = None
        if (head_value != None):
            self.head = LinkedListNode(head_value)
            self.tail = self.head

    def get_head(self):
        return self.head    
    
    def insert(self, value):
        curr = self.get_head()
        while ((curr) and (curr.next != None)):
            curr = curr.next
        if (curr==None):
            curr = LinkedListNode(value)
            self.tail = curr
        else:
            curr.next = LinkedListNode(value)
            self.tail = curr.next
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


    