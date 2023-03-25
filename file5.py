# #Tuple
# #once state can't be changed
# tpl=(1,2,3,4,5)
# #tpl[0]=100 #this is not possible
# #but if there exists list inside tuple then we can make changes
# tpl=(1,2,3,[4,5,6])
# tpl[-1][0]=40
# #print(tpl)

# #-----------------------------------------
# #Set
# st1={1,2,3,4,5,6}
# st2={1,2,3,4,5,1,2,3} 
# print(st1)
# print(st2) # whether the elements are repeated or not...set always return every element uniq
# print(st1.union(st2)) #this wil provide the union of two sets
# print(st1-st2)

#______________________________________________
#Dictionary
# person = {"name":"Sailesh", "age":23, "address":"kathmandu"}
# #print(person["name"])
# for i in person:
#     print(person[i])

# print(person.keys())
# print(person.values())

# #______________________________________________


# #exercise

# #1)python program to interchange first and last elements in a list
# arr=[1,2,3,4,5]
# arr[0],arr[-1]=arr[-1],arr[0] #this will work as swap in the array 
# print(arr)
# temp=arr[0]
# arr[0]=arr[-1]
# arr[-1]=temp
# print (arr)

#2)python program to reverse the list by different way
# lst.reverse()
# lst.sort(reverse=True)

#2)python program to reverse the list using for loop




# lst=[1,2,3,4,5,6]
# reversed_array=[]
# for i in range(len(lst)-1,-1,-1):
#     reversed_array.append(lst[i])
# print(reversed_array)

#using while loop
# start=0
# end=len(lst)-1
# while start<end:
#     lst[start],lst[end]= lst[end], lst[start]
#     start +=1
#     end -=1
# print(lst)









