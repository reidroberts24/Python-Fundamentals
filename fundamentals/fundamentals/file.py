num1 = 42 #variable declaration, initialize number
num2 = 2.3 #variable declaration, initialize number
boolean = True #variable declaration, initialize boolean
string = 'Hello World' #variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, initialize tuple
print(type(fruit)) #log statement, type check
print(pizza_toppings[1]) #log statement, access list value
pizza_toppings.append('Mushrooms') #add list value
print(person['name']) #log statement, access dictionary value
person['name'] = 'George' #access and change dictionary value
person['eye_color'] = 'blue' #initialize dictionary value
print(fruit[2]) #log statement, access tuple value

if num1 > 45: #if statement
    print("It's greater") #log statement
else: #else statement
    print("It's lower") #log statement

if len(string) < 5: #if statement, length check
    print("It's a short word!") #log statement
elif len(string) > 15: #else if statement, length check
    print("It's a long word!") #log statement
else: #else statement
    print("Just right!") #log statement

for x in range(5): #for loop start
    print(x) #log statement
for x in range(2,5): #for loop start
    print(x) #log statement
for x in range(2,10,3): #for loop start
    print(x) #log statement
x = 0 #variable declaration, initialize number
while(x < 5): #while loop start
    print(x) #log statement
    x += 1 #while loop increment

pizza_toppings.pop() #delete list value, access last value in list 
pizza_toppings.pop(1) #delete list value, access list value at specified index

print(person) #log statement
person.pop('eye_color') #delete dictionary value, access dictionary value
print(person) #log statement

for topping in pizza_toppings: #for loop start
    if topping == 'Pepperoni': #if statement
        continue #continue statement
    print('After 1st if statement') #log statement
    if topping == 'Olives': #if statement
        break #break statement

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop start
        print('Hello') #log statement

print_hello_ten_times() #log statement

def print_hello_x_times(x): #function declaration, paramater
    for num in range(x): #for loop start
        print('Hello') #log statement

print_hello_x_times(4) #function call, argument

def print_hello_x_or_ten_times(x = 10): #function declaration, parameter with default value
    for num in range(x): #for loop start
        print('Hello') #log statement

print_hello_x_or_ten_times() #function call
print_hello_x_or_ten_times(4) #function call, argument


"""
Bonus section
"""

# print(num3) --- log statement, NameError
# num3 = 72 --- variable declaration, initialize number
# fruit[0] = 'cranberry' --- access list value, change value
# print(person['favorite_team']) --- log statement, KeyError
# print(pizza_toppings[7]) --- IndexError: list index out of range
#   print(boolean) --- log statement
# fruit.append('raspberry') --- add list value
# fruit.pop(1) --- access list value, delete value