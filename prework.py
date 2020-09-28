# Write a function to print "hello_USERNAME!" USERNAME is the input of the function.
def hello_name(user_name):
    print("Hello" + user_name.upper() + "!")

hello_name('Angelica')

# Print first 100 odd numbers in Python.
def odd_numbers():
    for i in range(0,101,2):
        print(i)

odd_numbers()

# Please write a Python function, max_num_in_list to return the max number of a given list. 
# def max_num_in_list(a_list):
def max_num_in_list(a_list):
    max_num = max(a_list)
    return max_num
test = max_num_in_list([2,3,5,8,9])
print(max_num_in_list([2,3,5,8,9]))

# 
def is_leap_year(a_year):
    if a_year % 4 == 0 and a_year % 100 !=0:
        print(f'{a_year} is a leap year ')
    elif a_year % 400 == 0:
        print(f'{a_year} is a leap year ')
    else: 
        a_year = False
        print(f'{a_year}')

# solution 1.b
    def is_leap_year(a_year):
        if a_year % 4 == 0 and (a_year % 400 == 0 or a_year % 100 != 0):
            print(True)
        else:
            print(False)
is_leap_year(2020)


# 5
def is_consecutive(a_list):
    i = 0
    status = True
    while i < len(a_list) - 1:
        if a_list[i] + 1 == a_list[i + 1]:
            i += 1
        else: 
            status = False
            break
        print(status)