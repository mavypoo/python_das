

#General purpose 
#Most widely used data structure
#Grow and shrink size as needed 
#Sequence type
#Sortable 

#Constructors - creating a new list 

x = list() #empty list
y = ['a', 25, 'dog', 8.43]
tuple1 = (10,20)
z = list(tuple1)

#list comprehension 
a = [m for m in range(8)]
print(a)
#output [0, 1, 2, 3, 4, 5, 6, 7]

b = [i**2 for i in range(10) if i>4]  #if i is > 4, 5 to the power of 2 = 25
print(b)
#output [25, 36, 49, 64, 81]

b = [i**3 for i in range(10) if i>4]  #if i is > 4, 5 to the power of 3 = 125
print(b)
#output [125, 216, 343, 512, 729]


#delete - delete a list or an item in a list 
x = [5, 3, 8, 6]
del(x[1])
print(x)
#output [5, 8, 6]
del(x) # list x no longer exist


#append - append an item to a list - adding an item to a list 
#adds it to the end of the list
x = [5, 3, 8, 6]
x.append(7)
print(x)
#output [5, 3, 8, 6, 7]


#Extend - append a sequence to a list 
x = [5, 3, 8, 6]
y = [12, 13]
x.extend(y)
print(x)
#output [5, 3, 8, 6, 12, 13]


#insert - insert an item at a given index
x = [5, 3, 8, 6]
x.insert(1,7) #inserting 7 at index 1
print(x)
x.insert(1, ['a', 'm']) #inserting a, m in index 1 
print(x)
#output [5, 7, 3, 8, 6]
#output [5, ['a', 'm'], 7, 3, 8, 6]

#pop - pops last item off list and returns item
x = [5, 3, 8, 6]
x.pop() #pop off the 6
print(x)
print(x.pop()) #returns 8
#output [5, 3, 8]
# 8 


#remove - remove first instance of an item
x = [5, 3, 8, 6, 3]
x.remove(3) #removes the first 3 out of the list. python will start at the beginning of the list that matches and will end once it finds it
print(x)
#output [5, 8, 6, 3]

#Reverse - reverse the order of the list. It is an in-place sort, meaning it changes the original list
x = [5, 3, 8, 6]
x.reverse()
print(x)
#output [6, 8, 3, 5]


#Sort - sort the list in place
#Note: Sorted(x) returns a new sorted list without changing the original x.sort() puts the items of x in sorted order (sorts in place). 
x = [5, 3, 8, 6]
x.sort()
print(x)
#output [3, 5, 6, 8]

# Reverse sort - sort items descending. Use reverse = True parameter to the sort function
x = [5, 3, 8, 6]
x.sort(reverse=True)
print(x)
#output [8, 6, 5, 3]
