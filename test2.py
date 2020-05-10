import matplotlib.pyplot as plt


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
#
#
# thisdict = {
#   "brand": [1,2,3,4],
#   "model": [1,2,3,4],
# }
# i = 0
# a = list(thisdict.values())
# for k in a:
#     # print('values',k)
#     if len(a[0]) == len(a[i]):
#         i = i+1
#         print(k)
#         print(len(k),len(k))
# #         print()
#
# from numpy import sin, pi, arange
# from appJar import gui
# import random
#
# def getXY():
#     x = arange(0.0, 3.0, 0.01)
#     y = sin(random.randint(1,10) * pi * x)
#     return x,y
#
# def generate(btn):
#     # *getXY() will unpack the two return values
#     # and pass them as separate parameters
#     app.updatePlot("p1", *getXY())
#     showLabels()
#
# def showLabels():
#     axes.legend(['The curve'])
#     axes.set_xlabel("X Axes")
#     axes.set_ylabel("Y Axes")
#     app.refreshPlot("p1")
#
# app = gui()
# axes = app.addPlot("p1", *getXY())
# showLabels()
# app.addButton("Generate", generate)
# app.go()

# fig, ax = plt.subplots()
# fig, ax = plt.subplots(nrows=1, ncols=2,sharex=True,sharey=True)
# fig, axes = plt.subplots(subplot_kw=dict(polar=True))
# fig, axes = plt.subplots(3, 3, subplot_kw=dict(polar=True))
# axes[0, 0].plot(x, y)
# axes[1, 1].plot(x, z)
# axes[2, 2].plot(x, r)
# fig = plt.figure()
# fig.add_subplot()
# for ax in ax:
# ax.plot(x, y, 'b')
#     ax.set_xlabel('x')
#     ax.set_ylabel('y')
#     ax.set_title('Заголовок')
# fig.tight_layout()
# plt.tight_layout()
# plt.show()
# ax.plot(t, s)
#
# ax.set(xlabel='time (s)', ylabel='voltage (mV)',
#        title='About as simple as it gets, folks')
# ax.grid()
#C:\Users\pc\PycharmProjects\Project-X\# plt.show()
# def a():
#     x = [0,1,2,3]
#     y = [5,6,7,8]
#     r = [8,9,10,11]
#     z = [12,13,14,15]
#     d = {
#         1:x,
#         2:y,
#         3:r,
#     }
#     l = []
#     for k, v in d.items():
#         a = plt.plot(x,v)
#         plt.xlabel(k)
#         l.append(a)
#     # b=plt.plot(x, [88,99,99,00])
#
#     return
# a()
# plt.show()
# from appJar import gui
#
#
# app = gui()
# app.startLabelFrame("Simple", 0, 0)
# app.addImage("simple", "app.stopLabelFrame()
# app.go()


# class NotNumberException(Exception):
#
# import smtplib
#
# # And imghdr to find the types of our images
# import imghdr
#
# # Here are the email package modules we'll need
# from email.message import EmailMessage
#
# # Create the container email message.
# msg = EmailMessage()
# msg['Subject'] = 'Our family reunion'
# # me == the sender's email address
# # family = the list of all recipients' email addresses
# msg['From'] = me
# msg['To'] = ', '.join(family)
# msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
#
# # Open the files in binary mode.  Use imghdr to figure out the
# # MIME subtype for each specific image.
# for file in pngfiles:
#     with open(file, 'rb') as fp:
#         img_data = fp.read()
#     msg.add_attachment(img_data, maintype='image',
#                                  subtype=imghdr.what(None, img_data))
#
# # Send the email via our own SMTP server.
# with smtplib.SMTP('localhost') as s:
#     s.send_message(msg)


# plt.pie()
# plt.show()
#
# # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [10, 30, 45, 10]
# explode = (0.1, 0.2, 0.3, 0.4)  # only "explode" the 2nd slice (i.e. 'Hogs')
#
# plt.subplots()
# plt.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
#         shadow=True, startangle=90)
# plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
#
# plt.show()
a='a|b'
b =a.split('|')
print(b)