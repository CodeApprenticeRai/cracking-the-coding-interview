from LinkedList import LinkedList

class Solution:
    def delete_middle_node(self, linked_list):
        linked_list.delete_middle_node_constant_space()

if __name__=="__main__":
    test_list = LinkedList(0)
    import random
    random.seed(0)

    node_ids = [ test_list.insert( int(random.random()*10) ) for i in range(1,10) ]
    test_list.insert(4)
    
    test_list.print_list()
    
    solver = Solution()
    solver.delete_middle_node(test_list)
    test_list.print_list()