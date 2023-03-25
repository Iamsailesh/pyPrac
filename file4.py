#List 
#print("Hello world")
# lst=[1,2,"hello", "how", ["four",5,6,7,"eight"]]
# # print(lst[-1][0])
# # lst.append(100)
# # print(lst)
# # lst.insert(0,"zero")
# # print(lst)
# # lst.extend([1,"am","fine"])
# # print(lst)
# # lst.remove("hello")
# # print(lst)
# # lst.pop()
# # print(lst)
# # lst.clear()
# # print(lst)
# print(lst.index(2))
# print(len(lst))
# print(type(lst))
# print(lst[-1].index("eight"))
# if "eight" in lst[-1]:
#     print("yes")
# else: print("no")
# lst[1:3]=["fine","buddy"]
# print(lst)

# #pass by refernece
# #value of both list is changed
# lst2=[1,2,3,4,5,6,7,1,1,1,2,3,4,5,6,7,8,11,22,3,3]
# lst3=lst2
# #lst3[0]=100
# # print(lst3)
# # print(lst2)

# lst4 = lst2.copy()
# lst4[0]=101
# print(lst4)
# print(lst2)
# print(lst2.count(1))


lst=[1,3,4,7,9,2,3,5,6,8,-1,-2,0,10,13,2,6]
#lst.sort(reverse=True)
lst.reverse()
print(lst)


