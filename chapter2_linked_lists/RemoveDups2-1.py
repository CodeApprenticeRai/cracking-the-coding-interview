from LinkedList import LinkedList, LinkedListNode

class Solution:
    def remove_dups(self, linked_list):
        linked_list.remove_duplicates()



if __name__=="__main__":
    test_list = LinkedList(0)
    import random
    random.seed(0)

    node_ids = [ test_list.insert( int(random.random()*10) ) for i in range(1,10) ]
    test_list.insert(4)
    
    test_list.print_list()
    
    solver = Solution()
    solver.remove_dups(test_list)
    test_list.print_list()

