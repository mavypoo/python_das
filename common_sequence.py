# Indexing - access any item in the sequence using its index. Index starts with 0 for the first element. 

x = 'frog'
print(x[3])
#output: g


#list 
x = ['pig' 'cow', 'horse']
print(x[1])
#output: cow 

#tuple 
x = ('kevin', 'niklas', 'jenny', 'craig')
print(x[0])
#output kevin 

# Slicing - slice out substrings, sublists, subtuples using indexes. 
# [start: end+1 :step]

x = 'computer'
print(x[1:4]) #since we did not include the 3rd step. that step is assumed to be 1. thats the default
#output omp; start at o, don't include u - (stop ats u)

print(x[1:6:2]) 
#output opt; start at 0. skip by 2; don't include e(stops at e)

print(x[3:]) #default the empty is end of string. so  everything from index 3 and on 
#output puter 

print(x[:5]) # don't declare a start, so you start at the  very beginning, end at index 5(dont include)
#output  compu 

print(x[-1]) #-1 counts from the right side of the string. last element of the string
#output r 

print(x[-3:])
#output ter 

print(x[:-2])
#output comput #dont include the last  2 elements 




# Adding/Concatenating - combine 2 sequences of the same type by using +
#string 
x = 'horse' + 'shoe'
print(x)
#output horseshoe 

x = 'horse' ,'shoe'
print(x)
#output ('horse','shoe')

#list 
y = ['pig', 'cow'] + ['horse']
print(y)
#output ['pig', 'cow', 'horse']

#tuple
z = ('kevin', 'niklas', 'jenny') + ('craig',)
print(z)
#output ('kevin', 'niklas', 'jenny', 'craig')


# Multiplying - multiply a sequence using * 

#string 
x = 'bug' * 3
print (x)
#output bugbugbug

#list 
y=[8, 5] * 3
print(y)
#output [8, 5, 8, 5, 8, 5]

#tuples 
z = (2, 4) * 3
print(z)
#output (2, 4, 2, 4, 2, 4)


#Checking membership - test whether an item is or is not in a sequence - BOOLEAN - can only have 2 values: True or False 
#string
x = 'bug'
print('u' in x)
#output True

#list 
y = ['pig', 'cow', 'horse']
print('cow' not in y )
#output False 

#tuples 
z = ('kevin', 'niklas', 'jenny', 'craig')
print('niklas' in z)
#output True 


#Iterating - iterating through the items in a sequence 
#item
x = [7,8,3]
for item in x:
    print(item)
#output
# 7
# 8
# 3

# index & item - the enumerate will return both the index and the item 
y = [7,8,3]
for index, item in enumerate(y):
    print(index, item)
#output 
#0 7
#1 8
#2 3



#number of items - count the number of items in a sequence. 
#len function - will get the count or the number of items in a sequence 
#string 
x = 'bug'
print(len(x))
#output 3

#list
y = ['pig', 'cow', 'horse']
print(len(y))
#output 3

#tuples 
z = ('kevin', 'niklas', 'jenny', 'craig')
print(len(z))
#output 4


# Minimum - find the minimum item in a sequence lexicographically. Alpha or numeric types, but cannot mix types.Will print out the first letter in the word in alphabetical order
#string
x = 'bug'
print(min(x))
#output: b

#list 
y = ['pig', 'cow', 'horse']
print(min(y))
#output cow

#tuple
z = ('kevin', 'niklas', 'jenny', 'craig')
print(min(z))
#output craig 

#Maximum - find the maximum item in a sequence lexicographically. Alpha or numeric types but cannot mix types. Will print out the last letter in the world or the last word in alphabetical order
#string
x = 'bug'
print(max(x))
#output u

#list 
y = ['pig', 'cow', 'horse']
print(max(y))
#output pig

#tuple
z = ('kevin', 'niklas', 'jenny', 'craig')
print(max(z))
#output niklas

#Sum - find the sum of items in a sequence. Entire sequence must be numeric
#string -> error
x = [5,7, 'bug']
print(sum(x)) #generates an error
#output error 

#list 
y = [2,5,8,12]
print(sum(y))
print(sum(y[-2:]))
#output 
#27
#20   (8+12 = 20)

#tuple
z = (50,4,7,19)
print(sum(z))
#output
#80


#Sorting - returns a new list of items in sorted order. Does not change the original list.
#string 
x = 'bug'
print(sorted(x))
#output ['b', 'g', 'u']

#list
y = ['pig', 'cow', 'horse']
print(sorted(y))
#output ['cow', 'horse', 'pig']

#tuple
z = ('kevin', 'niklas', 'jenny', 'craig')
print(sorted(z))
#output ['craig', 'jenny', 'kevin', 'niklas']


#Sorting - sort by second letter 
#Add a key parameter and a lambda function to return the second character (the word key here is defined parameter name, k is an arbitrary variable name)
z = ('kevin', 'niklas', 'jenny', 'craig')
print(sorted(z, key=lambda i: i[1]))
#output ['kevin', 'jenny', 'niklas', 'craig']

#Count(item) - returns count of an item 
#string 
x = 'hippo'
print(x.count('p'))
#output 2

#list 
y=['pig', 'cow', 'horse', 'cow']
print(y.count('cow'))
#output 2

#tuples 
z = ('kevin', 'niklas', 'jenny', 'craig')
print(z.count('kevin'))
#output 1


#Index(item) - returns the index of the first occurrence of an item 
#it stops looking after it finds  the first item that it matches in the sequence 
#string 
x = 'hippo'
print(x.index('p'))
#output 2

#list
y = ['pig', 'cow', 'horse', 'cow']
print(y.index('cow'))
#output 1

#tuples
z = ('kevin', 'niklas', 'jenny', 'craig')
print(z.index('jenny'))
#output 2


#Unpacking - unpack the n items of a sequence into n variables.
x = ['pig', 'cow', 'horse']
a, b, c = x
print(a, b, c)
#output pig cow horse 
