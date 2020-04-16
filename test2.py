# a = [10,20,30,40]
# for i in a:
#     i+=i
#     print(i)

# def a():
#     s=1
#     c=2
#     return s,c
#
# def b(c):
#     s,c = c
#     w=s+c
#     print(w)
#
# b(c=a())
# t = ['name1', 'name2']
# c = ['abc','def',"xyz"]
# t_index = range(len(t))
# c_index = range(len(c))
# for i in c_index:
#     q_name = c[i] + t[i]
#     # for c_name in c:
#     #     for name in t:



# column_names_list= []
# list1= [ 'day table1', 'day,revenue table1', 'visitors table2', 'revenue table3', 'day table4', 'day,revenue table4', 'day,revenue,cost table4']
# for i in list1:
#     if i.count(',') > 0:
#         i = i.split(',')
#         column_names_list.append(i[-1])
#     else:
#         column_names_list.append(i)
# print(q_name)
# print(t[1:])

            # print(c_name,name)

# import numpy as np
#
# a = np.random.normal(size=(10, 1))
# b = np.random.normal(size=(1, 10))
#
# result = np.dot(a, b)
# print(result.shape)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
thisdict["car"] = "blue"
print(thisdict)