lst=[1,2,3,4,5,6,0]
del lst[:] # You can clear all elements from a list

a=lst
lst[:]=[7,8,9] #replace all elements of a list without creating a new list object
b=lst[:] # create a (shallow) copy of a list
print(b)
