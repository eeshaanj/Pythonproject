# Python program to remove multiple 
# elements from a list  
  
# creating a list 
list1 = [11, 5, 17, 18, 23, 50]  
  
# will create a new list,  
# excluding all even numbers 
list1 = [ elem for elem in list1 if elem % 2 != 0] 
  
print(*list1)

#  Let’s say we want to delete each element in the list which is 
# divisible by 2 or all the even numbers.

# Python program to remove multiple 
# elements from a list  
  
# creating a list 
list1 = [11, 5, 17, 18, 23, 50]  
  
# Iterate each element in list 
# and add them in variale total 
for ele in list1: 
    if ele % 2 == 0: 
        list1.remove(ele) 
  
# printing modified list 
print("New list after removing all even numbers: ", list1)  
