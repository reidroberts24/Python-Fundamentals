#1. Countdown
def countdown(num):
    lst = []
    for i in range(num,0,-1):
        lst.append(i)
    return lst
print(countdown(5))

#2. Print and Return
def print_and_return(lst):
    print(lst[0])
    return lst[1]
print(print_and_return([1,2]))

#3. First Plus Length
def first_plus_length(lst):
    return lst[0] + len(lst)
print(first_plus_length([1,2,3,4,5]))

#4. Values Greater than Second
def values_greater_than_second(lst):
    if len(lst) < 2:
        return False
    new_lst = []
    for i in range(len(lst)):
        if lst[i] > lst[1]:
            new_lst.append(lst[i])
    print(len(new_lst))
    return new_lst

print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

#5. This Length, That Value
def length_and_value(size, value):
    return [value] * size

print(length_and_value(4,7))
print(length_and_value(6,2))