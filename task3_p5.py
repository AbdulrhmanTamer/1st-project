#define a function that checks if two lists are equal or not
def check_equal_lists(list1,list2):
    #check if the length of two lists are equal or not
    if len(list1) != len(list2):
        print('two lists from diff lenght')
        return False
    #squaring the elements of list1
    squared_list1=[i**2 for i in list1]
    #making for loop summing the elements of squared list1
    total1=0
    for num in squared_list1:
        total1+=num
        #squaring the elements of list2
    squared_list2=[i**2 for i in list2]
    #making a for loop summing the elements of squared list2
    total2=0
    for num in squared_list2:
        total2+=num
        #if the sum of squared list1 elements equals the sum of squared list2 elements so two lists are equal
    if total1==total2:
        print('two lists are equal')
        return True
    else :
        print('two lists arenot equal')
        return False
    #ask the user to input list1,2 elements separated by spaces
list1_elem=input('enter a list1 int elements separated by spaces :').split()
list2_elem=input('enter a list2 int elements separated by spaces :').split()
#turn the list1,2 elements to intgers
list1=[int(x) for x in list1_elem]
list2=[int(x) for x in list2_elem]
#call the function
check_equal_lists(list1,list2)











