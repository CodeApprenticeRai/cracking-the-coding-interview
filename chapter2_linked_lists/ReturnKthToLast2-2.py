from LinkedList import LinkedList, LinkedListNode


if __name__=="__main__":
    test_list = LinkedList(0)
    import random
    random.seed(0)

    node_ids = [ test_list.insert( int(random.random()*10) ) for i in range(1,10) ]
    test_list.insert(4)
    
    test_list.print_list()

    print( test_list.kth_to_last(0).value )    
    print( test_list.kth_to_last(2).value )

    test_list.print_list()
