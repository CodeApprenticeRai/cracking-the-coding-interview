from os import O_TEMPORARY
from chapter2_linked_lists.LinkedList import LinkedList


form LinkedList import LinkedList

'''
You have two numbers represented by a linked ist, 
where each node contains a single digit. 
The digits are stored in reverse order, such that the 1s
digit is at the head of the list. 
Write a function that adds two number and returns the sum as a linked list. 
'''

def add_numbers(head1, head2):
    output = LinkedList(None)

    curr = [head1, head2, output.get_head()]
    carry = 0

    while ((curr[0]!=None) or (curr[1]!=None)):
        #add the two numbers
        _sum = 0
        if ((curr1!=None) and (curr2!=None)):
            _sum = curr[0].value + curr[1].value
            _sum += carry
            if (_sum > 9):
                carry += _sum - 9
                _sum -= carry
        curr[2].value = _sum
        for i in range(len(curr)):
            curr.
            

if __name__=="__main__":
    list1 = LinkedList()
    list2 = LinkedList()
    list3 = LinkedList()
    
    for num in [7,1,6]: 
        list1.insert(num)
    for num in [2,9,7]: 
        list2.insert(num)
    
    test_list.print_list()
    
    solver = Solution()
    solver.add_numbers(
        list1.get_head(),
        list2.get_head(),
        list3.get_head()
    )
    list3.print_list()

