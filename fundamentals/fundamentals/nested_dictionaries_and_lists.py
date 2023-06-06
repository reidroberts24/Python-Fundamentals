#1. Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
students[0]['last_name'] = "Bryant"
sports_directory['soccer'][0] = "Andres"
z[0]['y'] = 30

#-------------------------------------------------------------------------------------------------------------------------------------------------

#2. Iterate Through a List of Dictionaries
def iterateDictionary(some_list):
    for dict in some_list:
        first = dict['first_name']
        last = dict['last_name']
        print(f"first_name - {first}, last_name - {last}")
students = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
iterateDictionary(students) 

#-------------------------------------------------------------------------------------------------------------------------------------------------

#3. Get Values From a List of Dictionaries
def iterateDictionary2(key_name, some_list):
    for item in some_list:
        print(item[key_name])

iterateDictionary2('first_name', students) 
iterateDictionary2('last_name', students) 

#-------------------------------------------------------------------------------------------------------------------------------------------------

#4. Iterate Through a Dictionary with List Values
def printInfo(some_dict):
    for key in some_dict:
        print("\n")
        print(len(some_dict[key]), key)
        for item in some_dict[key]:
            print(item)
dojo = {
   'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)