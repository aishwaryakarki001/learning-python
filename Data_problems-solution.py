# 1  
'''
Initialize a stack, add 7 items to it then remove 3
everytime you remove, print the value you have just removed

#HINT the pop method returns the item it just removed

what makes a stack different from a regular list?
'''
# we can sace the value we just removed by writing:

mystack= [1,2,3,4,5,6,7]
for i in range(3):
    print(mystack.pop(len(mystack)-1))

'''
Stack follows the Last in First Out(LIFO) order ie. the most recently added items if the first one to be removed from the items whereas a regular list doesnot follow any specific order when adding or removing any items from the items'''
#2

'''
Initialize a queue

add 4 items to it 
remove 3 items from it 


 What is the difference between a stack and a queue? what are the applications of a queue
'''
myqueue=[5,6,7,8]
for i in range(3):
    print(myqueue.pop(0))

'''
Stack is the data structure that follows the Last in First Out (LIFO) principle ie. the most recently added items if the first one to be removed from the items whereas queue is a data structure that follows First In First Out(FIFO) principle when adding or removing any items from the items. 

Queue play a vital role in managing and controlling the flow of the data, tasks as their FIFO nature helps in maintaining the order of items.
'''
#3


'''

Initialize/ create a set of 10 numbers

check if the number 5 is in the set, if it is print "5 is here"

What is a set? what makes a set special and different from other structures ?

'''
myset = [1,2,3,4,5,6,7,8]
if (5 in myset):
    print("5 is here")

'''
Set is one of the data type in Python which is the collection of unordered, unindexed items.

Following reason makes the set special and different from other data types:

1. Do not allow duplicate values.
2. Accessing the item in a set is more efficient in speed and memory 
3. Support mathematical set operations(Intersection, union )
'''
#  4 

'''
Initialize/ create 2 different tuples

combine the 2 tuples together to make one larger tuple

what is a tuple? what makes a tuple special/ different from other structures?

'''
firsttuple= (1,2,3,4)
secondtuple=(5,6,7,8,9)

thirdtuple= firsttuple +secondtuple
print(thirdtuple)

'''
Tuple is a data type in python used to store collection of data which are ordered, unchangeable and also allows duplicate values.

Following reason makes the tuple diiferent from other data types:
1. Allows duplicate values
2. Are indexed
3. Unchangeable
'''

#5 initialize and create 2 different dictionaries

'''
one dictionary should represent a humans physical features with the keys being

height, weight, age, eye color

and the other dictionary 

having names of items as keys and thier respective price as thier value pair


access 2 different values from each dicitonary and print them

What is a dictionary? what makes a dictionary different from the other data structures? what makes it usefull?

# what are the applications of a dicitonary?


'''
physicalfeat= {
    "height": 140,
    "weight":120,
    "age":13,
    "eyecolor":"blue"
    }

goods={
    "items":"coffee",
    "price":120
}

print(physicalfeat["height"])
print(goods["items"])


'''
Dictionary is the collection of data which are ordered and stored in key value pair.
1. Dictionaries are ordered by key
2. Dictionaries have duplicate values but no duplicate keys
3. Helps in managing and organizing data efficiently
'''

# Final section


'''
#List Manipulation: Given a list mylist, write a Python program to remove all duplicate elements from the list while preserving the original order.
'''
mylist= [1,2,3,4,5,5,5,6,7,7]
noduplist= []
for i in mylist:
    if i not in noduplist:
        noduplist.append(i)
print(noduplist)
'''
Tuple Operations: Create a tuple called student_data containing information about a student, such as name, age, and subjects. Use tuple indexing to access and print the student's age.

'''

student_data = ("Christie",37, ["English", "Sociology"] )
age=student_data[1]

print(age)
'''
Set Operations: Create two sets, set1 and set2, each containing some elements. Write a Python program to find and print the intersection of these two sets (common elements in both sets).
'''
set1 ={1,2,3,4,5,6,7,8}
set2= {7,8,9,10,11,12}
commonele= set1.intersection(set2)
print(commonele)

'''
Dictionary Manipulation: You have a dictionary student_grades that stores students' names as keys and their grades as values. Write a function that takes this dictionary as input and returns the name of the student with the highest grade.
'''
student_grades= {
    "Kyle": 70,
    "Chris": 83,
    "Joseph":67,
    "Rylie": 91
}
hgradestudent= None
highest_grade= -1
for student, grade in student_grades.items():
    if grade >highest_grade:
        highest_grade= grade
        hgradestudent=student
print(hgradestudent)
'''
Stack Implementation: Implement a stack class in Python that supports the push() and pop() operations. Test your stack class by pushing and popping elements to/from it.

'''
class Stack():
    def __init__(self):
        self.item= []
    
    def push(self, item):
        self.item.append(item)

    def pop(self):
        if not self.is_empty():
            return self.item.pop()
        else:
            print("Stack is empty")
    def is_empty(self):
        return len(self.item)==0
    
stack = Stack()

stack.push(2)
stack.push(5)
stack.push(10)
stack.push(15)

print("Stack popped", stack.pop())


'''
Queue Implementation: Implement a queue class in Python that supports the enqueue() and dequeue() operations. Test your queue class by adding and removing elements from it.

'''
class Queue:
    def __init__(self):
        self.items= []

    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
            
        else:
            print("Queue is empty")


queue_list = Queue()

queue_list.enqueue(1)
queue_list.enqueue(2)
queue_list.enqueue(3)
queue_list.enqueue(4)

print("Enqueued queue", queue_list.items)

dequeued_item = queue_list.dequeue()
print("Dequeued item", dequeued_item)
print("Queue after dequeue", queue_list.items)
'''


List Sorting: Write a Python program to sort a list of tuples based on the second element of each tuple in ascending order.



List Comprehension: Create a list of all prime numbers less than 100 using list comprehension and a helper function that checks for prime numbers.
'''


 
'''
Dictionary Comprehension: Given a list of words, create a dictionary where the keys are words, and the values are the lengths of the words. Use dictionary comprehension to achieve this.
'''
list_words= ["box", "bottle", "glass", "spoon", "icecream"]
length_words= {words: len(words) for words in list_words}

print(length_words)
'''


'''
