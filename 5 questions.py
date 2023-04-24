#problem 1
from subprocess import list2cmdline


def hello_name(user_name):
    print("hello_" + user_name.upper() + "!")
hello_name("username")
#hello_USERNAME!
#hello_username
hello_name = "hello_username!"
print(hello_name)
 
#problem 2
def first_odds() :
    for number in range(1, 101) :
        if (number % 2 == 1) :
            print(number)
#the answer is 1,0,1,0,1,0,1,0,1,0,1,0,1 and on and on

#problem 3
def max_num_in_list(a_list) :
    max = a_list[0]
    for i in a_list:
        if i > max:
            max = i
    return max 

list = [3,2,1000,4,5,6,200,30,26] 
max = max_num_in_list(list) 
print(max)

#problem 4
def is_leap_year(a_year) :
    if (a_year % 4 == 0) :
        return False    
    if (a_year % 400 == 0) :
        return False
    if (a_year % 100 == 0) :
        return False
    return True

#problem 5
def is_consecutive(a_list) :
    startNumber = a_list[0]
    for i in a_list:
        if startNumber != i:
            return False
        startNumber = startNumber + 1
        return True
    list1 = [2,3,4,5]
    list2 = [1,2,4,5]

    print(is_consecutive(list1))
    print(is_consecutive(list2))
    


