'''
For and for with range loops <---
WHILE LOOPS
different variables
if statements with operators and, or, not,<=, >=, <, +, ==, !=

'''


'''
Python lists



we say a python list is a data structure in python

a data structure is a datatype that allows us to 

hold multiple values under one variable name

because of this, lists and other similar data structures are very powerful

datastructures are how we are able to store any big data in python


in this class we will look at all the other datastructures

and we will look at matplotlib, a python big data tool 

that helps us visualize data
'''



 

'''
# There are multiple ways to store information in programming

# the ways in wich we store this information are what we call data structures

#  for example, when we want to store multiple different values under one name
#  we may use the list data structure

# there are many different types of data structures

# Listed below are the most popular and useful data structures

'''

# list

# Key points include :

# 1. A list is mutable meaning we can change its values and also add new values 

''' for example'''

mylist = ["hello",5,100,3.14,True]


list1 = [1,2,3,6,8,4]  # we create a list by seperating values using comma's 
                       # inside of square brackets 

list1.append(453682)  # the append function is a built in python function 
                      # this append funciton allows us to add a value to the end 
                      # of the list

list3 = list1 + [1,4,6] # <--- this will add 3,4,5,6 to the end of list1

print(list3)


# the syntax to add a value to the end of a list is :

# list_you_want_to_add_to.append(value_you_want_to_add)
  
'''

In order to delete an item from a list we will use the built in pop method

it works like this 

listname.pop(index_of_item_to_remove)


List INDEXING 


items in a list are indexed (ordered) using a numerical representation of the item's 
position in a list... indexes start from 0 to n-1  where n = total num of items in list


mylist = [2,4,6,8,10,12]
index     0,1,2


the item 2 has an index and position of 0
the item 4 has an index and position of 1
the item 6 has an index/position of 2
'''



print(mylist," this is the print")

#let's say I want to access the fourth item in this list..
# with practice you quickly realize that the fourth item has an index of 3 in the list
#to access it, I write

print(mylist[3],"this is the example")


# list.pop(index) is a built in function that will delete an element from a list

# you must specify the INDEX of the element you want to remove, not it's value

# for example lets say i want to delete the second item from a list...

mylist.pop(1) # we remove the item with index 1, wich is the item in position 2





'''
we want to remember every element in a list has a number value associated with it

called an index. This index is a number that represents the position of the item

within the list.  Where the first item will have an index of 0, second will have an index of 1

to access a specific item in a list we will write the list name down followed by the

index of the item you want to access in square brackets

'''

#for example, given the following list:


anyname = [4,6,8,8,8,8,10,13,5,7]


# to print the second item in this list, I need to access it using it's index like so:

print(anyname[1])


# to remove the third item from the first list, I would run the following command
name = [1,2,3,4,5,6,7,10,13,111,"strings",False]

del(name[2]) 
name.pop(2) # this is the code to do so

print(name)

# this works because python pop function works like so:

#name_of_list_to_delete_from.pop(index_of_value_you_want_to_delete)


# append is a built in python function that allows you to insert data into the end list


# we implement it like so


#list_name.append(value_to_be_appended)

list1.append(4)

print(list1)

# adding 4 to the end of the list

# 1. A list is changeable
# 2. A list is a sequence meaning it is ordered
# 3. Lists allow duplicate values. 



# to add an item at a specific index in a list, we use the insert method/function

# it works like so :

#list_you_want_to_add_to.insert(index_of_where_you_want_to_add,value_you_want_to_add)

# for example, add 5 at the second position in the following list.

mylist = [1,4,5,6,7]

mylist.insert(1,5) #this inserts the number 5 into the second position of the list


alist = [1,3,4,5,67]



# the len(a_list) function is a function that returns the number of items in a list


#len()   # <=== this is a function that will return the number of items in a list

# meaning.... 

# so given 

a_list = [1,3,4,5,6,7]

print(len(a_list))

#len(a_list) will return 6 

#example


a_list = [1,4,5,6,7,8,9,1000,103,5,5,6,8]

print(len(a_list))


a_list.pop(len(a_list)-1)



'''


How do we access certain items in a list? we use what is called an index

so lists order thier items by indexing them from   0 - [(number of items)-1]


every item in a list, has a number associated with it called an index
that describes its position within the list

an index of 0 means that this is the first item in the list

an index of 3 means that this is the fourth item in the list

how can we use indexes to access a specific item?


for example in a list that looks like this :

mylist = [1,2,3,4,5]

the index of the first item is 0

therefore the index of 1  is 0
the index of #2 is 1

how do we access singular items in a list using the indexes. Well,
 when accessing a certain item, we want to specify it's index

the syntax is as follows:




print(list_name[index_value_of_item_you_want_to_access])

in order to print the number 3 in our code, we write

'''
mylist = [1,2,3,4,5]

print(mylist[2])


mylist = [10,20,30,40]   


print(mylist[3])


list1 = [100,45,778,2,20000]

#how to remove an item from a list

'''
to remove an item from a list, we will use the pop method

this is another built in python function and it works like so

list_you_want_to_remove_from.pop(index_of_item_you_want_to_remove)

'''
list1.pop(0)  # removes the first item from the list

list1 = [100,45,778,2,20000]


list1.pop(3)  # removed the number 2 from the list

list2 = [1,3,4,5,6,7,8]


list3 = list1+list2  #adding 2 lists together

list4 = list3 +[3]

print(list4)

print(list1)
print(list1[-1])  

list = [1,4,6,6,8,10]

# delete 3rd item

list.pop(2)



print(list," this is a print statement on line 142")

'''
list1.pop(index of the item you would like to remove)
'''




# Tuple 

# 1. A tuple is similar to a list because it is also a sequential data structure
# 2. Meaning its elements are ordered with index , from 0 to (n-1)  n = # of items
# 3. Tuples allow duplicate values. 
# 4. Tuples are immutuble meaning unchangable, meaning we cannot use the append function, 
# we cannot add to a tuple, also cannot delete



# we declare a tuple as such :

mytuple = (1,2,3,4,5,6) # <-- round bracket

# because a tuple is unchangeable we cannot do : 

#mytuple.append(2)

#mytuple[1] = 2

# we cannot assign new values to a tuple, we cannot append to a tuple

# The only way to add tuples together is to create a new tuple comprised of the 2 you want to combine

tuple1 = (1,2,2,3)
tuple2 = (5,6,7)

tuple3 = tuple1 + (1,2) # this would make : (1,2,2,3,1,2)


tuple3 = tuple2+tuple1  # this would make : (5,6,7,1,2,2,3)

print(tuple3[3])

# however, we can access any item in a tuple the same way we access items in a list

print(tuple1[2])

# tuple is meant to not be changed/tampered with.. working with tuples does not give us a lot of room to play
# that is by design.. tuples are more secure this way 

# In conclusion : A tuple is an ordered sequence that allows duplicate values however tuples are unchangable/immutable'
# you can only combine mutliple tuples together by adding them to each other 

tuple3 = tuple1+tuple2

# Set

#Set items are:

# 1. unordered,  
# 2. do not allow duplicate values.
# 3. changeable/ mutable

# pro's of using a set is :
# accessing an item in a set is much more effecient speed and memory wise than accessing an item in a list 

# con's 

# it is literally unordered, you cant specifically acess an item at a certain location
# meaning sets have no indexes 

# we initialize a set by using curly brackets

myset = {1,2,3,3,3,3,3,3,3,3,4,5,6} 

print(myset)


alist = [2,3,4,4,4,4,4,45,6,False,7]
myset2 = set(alist)


print(myset)

if (6 in myset):  #<---- strong application
    print("6 is in the set")


# we use sets as a very effecient way to store data 
# that is not meant to be repeated 

# the value in storing it in a set 
# is that checking if an item is in a set
# is much faster than checking if an item is in a list

# you can imagine if you have 10 million datapoints
# that dont repeat and you always just want to check 
# if a certain value is in the set
# then we would use set

 

#Once a set is created, you cannot change its items, but you can remove items and add new items.

myset = {"hello",2,3,True,4,5,6}



myset.add(7)     #  myset.add(value you want to remove)
myset.remove("hello")  #  myset.remove(value you want to remove)

mylist = [4,5,6,7,8]

print(myset)

# dictionary/map/hashmap

# Dictionaries are used to store data values in key:value pairs.

# 1. Dictionaries are changeable
# 2. Dictionaries are ordered by key.. 
# 3. Dictionaries can have duplicate values BUT
#    CANNOT have duplicate keys..

mydict = {
    "Height":{180,149,150,180,1111}, #get's over written
    "Height": 30,
    "Weight":(165,10),
    "age":"xjioo",
    1:1000,
    2:"hello",
    0:"zero"
}


mystudents = {
"weight":[120,150,200,170,100],
"height":[180,180,170,160,165],
"age":[18,18,19,18]
}




print(mydict["Height"])
print(mydict[0])
print(mydict["age"])



print(mydict[2])

print(mydict["age"])

print(mydict)


mydict = {
    'a':180,
    2:165,
    3:300
}

print(mydict[3])

# NOTE in some languages, 
# 
# keys are only alloud to be strings, unlike python 

# A dictionary is a collection which is
# changeable and do not allow duplicate keys, 
# but does have duplicate vals.

# the point of a dictionary is, 
# is that items are not ordered by index 
# from 0-len(list)-1 it is actually ordered by it's keys

# meaning to access any value in a dictionary, 
# in the index section of the dictionary we will 
# write our key value


# so we no longer acess items in a dictionary by index,
#  we access by key

mydict1 = {
    "Height":180,
    "Weight":165,
    "age":300,
}

mydict2 = {

    1:[180,18,1888],
    3:300
}

print(mydict1["Weight"])

print(mydict2[1][1]) # this prints 18 because

#mydict2[1] = [180,18]

# therefore mydict2[1][1] = 18


#to add to a dicitonary, you will simply create a new key value pair
#by writing the following

mydict["newkey"] = "newvalue"

mydict[10000] = 10  # in this line of code, 
                    # we have created a new key value pair

# 10000:10


# to delete items from a dictionary we will use the del() keyword as such



del (mydict["newkey"])


# this line of code will delete the key value pair

#"newkey":"newvalue"

# in this line of code, we have created the new key value pair

#"newkey":"newvalue" onto the dictionary


# There are no duplicates, this is because every key must be unique. We cannot have 2 of the same key.
# Hoewever, we can have 2 same values


# stack  (form of list)

mystack = [1,2,3,4,5,6]

# a stack is actually just a list but with 2 rules.

# 1. you are only alloud to add/remove items from the END of the list or FRONT
#    you may only pick one side per stack/queue
# 2. YOU MUST REMOVE FROM THE SAME LOCATION YOU ADD TO..  <---

# this means, if whenever you remove an item, it is from the end of the list, 
# you must make sure that you only remove and add from the end of the list as well



# why? 

#the whole point of a stack is that it is a special list data structure where :

# the item that has most recently been added will be the first to be removed

# we call this structure  LIFO  last in, first out 

# this structure is used a lot in graph traversal algorithms and in a lot of
# recursion simulation...

# to create a stack we simply create a list

mystack = [1,3,4,5,6,7,8]

# what makes a stack a stack is how you add/remove from it

mystack.pop(len(mystack)-1) # I can only remove from this location

mystack.append(4)  #I can only add to the end 


# queue  (form of list)

# A queue follows similar philosophy, only we call it FIFO  first in, first out

# The best way to describe a Queue is that a queue is modelled after a line to any store

# the person in the front of the line is the first to finish and go (be removed from the queue)
# the person last in line needs to wait until everyone in front of them has left

# The whole point about queues is that, similarly to stacks, they follow 2 specific rules


# 1. you are only allowed to add at the end or front (you must pick one) (same as rule #1 for stack) 
#  meaning only allowed to append or remove from either the last item or first item in the list


# 2. YOU MUST REMOVE FROM THE OPPOSITE LOCATION THAT YOU ADD TO 

# meaning, if whenever I add an item, I use append.. meaning I add to the end of the list
# for the rest of the queue's existence, you MUST CONTINUE TO ADD TO THE BACK OF THE LIST
# AND ONLY REMOVE FROM THE FRONT

["person1","person2","person3","person4"]

# why is this relevant? # why do we use queues ?   

# this perfecty models people in line  <---- 


["person6","person7"]

# programmers use queues to code people waiting on a phone line 

# automated messages when you call the bank they say :

# estimated wait time 40 mins, there are 25 people ahead of you 

# to add an item to the end of a list

numlist = [1111,3]
numlist.append(6)  #  (to add 6 to the list "numlist")


# to remove an item  we use the pop method

#to remove the first item in numlist, we write

numlist.pop(0)


mylist = [1,3,5,6]

mylist.insert(7)
print