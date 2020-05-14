# # # # import matplotlib.pyplot as plt
# # # #
# # # #
# # # # # a = [10,20,30,40]
# # # #
# # # # # for i in a:
# # # # #     i+=i
# # # # #     print(i)
# # # #
# # # # # def a():
# # # # #     s=1
# # # # #     c=2
# # # # #     return s,c
# # # # #
# # # # # def b(c):
# # # # #     s,c = c
# # # # #     w=s+c
# # # # #     print(w)
# # # # #
# # # # # b(c=a())
# # # # # t = ['name1', 'name2']
# # # # # c = ['abc','def',"xyz"]
# # # # # t_index = range(len(t))
# # # # # c_index = range(len(c))
# # # # # for i in c_index:
# # # # #     q_name = c[i] + t[i]
# # # # #     # for c_name in c:
# # # # #     #     for name in t:
# # # #
# # # #
# # # #
# # # # # column_names_list= []
# # # # # list1= [ 'day table1', 'day,revenue table1', 'visitors table2', 'revenue table3', 'day table4', 'day,revenue table4', 'day,revenue,cost table4']
# # # # # for i in list1:
# # # # #     if i.count(',') > 0:
# # # # #         i = i.split(',')
# # # # #         column_names_list.append(i[-1])
# # # # #     else:
# # # # #         column_names_list.append(i)
# # # # # print(q_name)
# # # # # print(t[1:])
# # # #
# # # #             # print(c_name,name)
# # # #
# # # # # import numpy as np
# # # # #
# # # # # a = np.random.normal(size=(10, 1))
# # # # # b = np.random.normal(size=(1, 10))
# # # # #
# # # # # result = np.dot(a, b)
# # # # # print(result.shape)
# # # # #
# # # # #
# # # # # thisdict = {
# # # # #   "brand": [1,2,3,4],
# # # # #   "model": [1,2,3,4],
# # # # # }
# # # # # i = 0
# # # # # a = list(thisdict.values())
# # # # # for k in a:
# # # # #     # print('values',k)
# # # # #     if len(a[0]) == len(a[i]):
# # # # #         i = i+1
# # # # #         print(k)
# # # # #         print(len(k),len(k))
# # # # # #         print()
# # # # #
# # # # # from numpy import sin, pi, arange
# # # # # from appJar import gui
# # # # # import random
# # # # #
# # # # # def getXY():
# # # # #     x = arange(0.0, 3.0, 0.01)
# # # # #     y = sin(random.randint(1,10) * pi * x)
# # # # #     return x,y
# # # # #
# # # # # def generate(btn):
# # # # #     # *getXY() will unpack the two return values
# # # # #     # and pass them as separate parameters
# # # # #     app.updatePlot("p1", *getXY())
# # # # #     showLabels()
# # # # #
# # # # # def showLabels():
# # # # #     axes.legend(['The curve'])
# # # # #     axes.set_xlabel("X Axes")
# # # # #     axes.set_ylabel("Y Axes")
# # # # #     app.refreshPlot("p1")
# # # # #
# # # # # app = gui()
# # # # # axes = app.addPlot("p1", *getXY())
# # # # # showLabels()
# # # # # app.addButton("Generate", generate)
# # # # # app.go()
# # # #
# # # # # fig, ax = plt.subplots()
# # # # # fig, ax = plt.subplots(nrows=1, ncols=2,sharex=True,sharey=True)
# # # # # fig, axes = plt.subplots(subplot_kw=dict(polar=True))
# # # # # fig, axes = plt.subplots(3, 3, subplot_kw=dict(polar=True))
# # # # # axes[0, 0].plot(x, y)
# # # # # axes[1, 1].plot(x, z)
# # # # # axes[2, 2].plot(x, r)
# # # # # fig = plt.figure()
# # # # # fig.add_subplot()
# # # # # for ax in ax:
# # # # # ax.plot(x, y, 'b')
# # # # #     ax.set_xlabel('x')
# # # # #     ax.set_ylabel('y')
# # # # #     ax.set_title('Заголовок')
# # # # # fig.tight_layout()
# # # # # plt.tight_layout()
# # # # # plt.show()
# # # # # ax.plot(t, s)
# # # # #
# # # # # ax.set(xlabel='time (s)', ylabel='voltage (mV)',
# # # # #        title='About as simple as it gets, folks')
# # # # # ax.grid()
# # # # #C:\Users\pc\PycharmProjects\Project-X\# plt.show()
# # # # # def a():
# # # # #     x = [0,1,2,3]
# # # # #     y = [5,6,7,8]
# # # # #     r = [8,9,10,11]
# # # # #     z = [12,13,14,15]
# # # # #     d = {
# # # # #         1:x,
# # # # #         2:y,
# # # # #         3:r,
# # # # #     }
# # # # #     l = []
# # # # #     for k, v in d.items():
# # # # #         a = plt.plot(x,v)
# # # # #         plt.xlabel(k)
# # # # #         l.append(a)
# # # # #     # b=plt.plot(x, [88,99,99,00])
# # # # #
# # # # #     return
# # # # # a()
# # # # # plt.show()
# # # # # from appJar import gui
# # # # #
# # # # #
# # # # # app = gui()
# # # # # app.startLabelFrame("Simple", 0, 0)
# # # # # app.addImage("simple", "app.stopLabelFrame()
# # # # # app.go()
# # # #
# # # #
# # # # # class NotNumberException(Exception):
# # # # #
# # # # # import smtplib
# # # # #
# # # # # # And imghdr to find the types of our images
# # # # # import imghdr
# # # # #
# # # # # # Here are the email package modules we'll need
# # # # # from email.message import EmailMessage
# # # # #
# # # # # # Create the container email message.
# # # # # msg = EmailMessage()
# # # # # msg['Subject'] = 'Our family reunion'
# # # # # # me == the sender's email address
# # # # # # family = the list of all recipients' email addresses
# # # # # msg['From'] = me
# # # # # msg['To'] = ', '.join(family)
# # # # # msg.preamble = 'You will not see this in a MIME-aware mail reader.\n'
# # # # #
# # # # # # Open the files in binary mode.  Use imghdr to figure out the
# # # # # # MIME subtype for each specific image.
# # # # # for file in pngfiles:
# # # # #     with open(file, 'rb') as fp:
# # # # #         img_data = fp.read()
# # # # #     msg.add_attachment(img_data, maintype='image',
# # # # #                                  subtype=imghdr.what(None, img_data))
# # # # #
# # # # # # Send the email via our own SMTP server.
# # # # # with smtplib.SMTP('localhost') as s:
# # # # #     s.send_message(msg)
# # # #
# # # #
# # # # # plt.pie()
# # # # # plt.show()
# # # # #
# # # # # # Pie chart, where the slices will be ordered and plotted counter-clockwise:
# # # # # labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# # # # # sizes = [10, 30, 45, 10]
# # # # # explode = (0.1, 0.2, 0.3, 0.4)  # only "explode" the 2nd slice (i.e. 'Hogs')
# # # # #
# # # # # plt.subplots()
# # # # # plt.pie(sizes, explode=None, labels=labels, autopct='%1.1f%%',
# # # # #         shadow=True, startangle=90)
# # # # # plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
# # # # #
# # # # # # plt.show()
# # # # # a='a|b'
# # # # # b =a.split('|')
# # # # # print(b)
# # # #
# # # # import sys
# # # # sys.path.append("../")
# # # # from appJar import gui
# # # #
# # # # clicked = False
# # # # animated = True
# # # #
# # # #
# # # # photo="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"
# # # #
# # # # def changePic(btn):
# # # #     if btn == "clickme":
# # # #         global clicked
# # # #         if clicked: app.setImage("clickme", "test.ppm")
# # # #         else: app.setImage("clickme", "Pie.ppm")
# # # #         clicked = not clicked
# # # #     elif btn == "No reload":
# # # #         app.setImage("no_reload", "test.ppm")
# # # #     elif btn == "Reload":
# # # #         app.reloadImage("reload", "test.ppm")
# # # #     elif btn == "Stop":
# # # #         global animated
# # # #         if animated:
# # # #             app.stopAnimation("animated")
# # # #             app.setButton("Stop", "Start")
# # # #         else:
# # # #             app.startAnimation("animated")
# # # #             app.setButton("Stop", "Stop")
# # # #         animated = not animated
# # # #     elif btn == "Speed":
# # # #         app.setAnimationSpeed("animated", app.getScale("Speed"))
# # # #     elif btn == "Zoom":
# # # #         app.zoomImage("Zoom", int(app.getSpinBox("Zoom")))
# # # #     elif btn == "Open":
# # # #         imgPath = app.openBox(title="Open Image", dirName="images", fileTypes=[('images', '*.png'), ('images', '*.jpg'), ('images', '*.gif'), ('images', '*.jpeg'), ('all', '*')])
# # # #         if imgPath != "":
# # # #             try:
# # # #                 app.setImage("Open", imgPath)
# # # #             except:
# # # #                 app.errorBox("File error", "Unable to open image: " + str(imgPath))
# # # #
# # # # app=gui("Image Test")
# # # # # app.setImageLocation("images")
# # # #
# # # # app.startLabelFrame("Image Data", 0, 0)
# # # # app.addImageData("imgdata", photo)
# # # # app.stopLabelFrame()
# # # #
# # # # app.startLabelFrame("Compound Image", 1, 0)
# # # # app.addImage("cimage", "test.ppm", compound="top")
# # # # app.stopLabelFrame()
# # # #
# # # # def imgMap(pos):
# # # #     print(pos)
# # # #
# # # # app.startLabelFrame("ImageMap", 0, 1)
# # # # app.addImage("simple", "test.ppm")
# # # # mapData = {"Yellow": [15,52,77,138], "Red":[75,1,129,138], "White":[137,15,184,127]}
# # # # app.setImageMap("simple", imgMap, mapData)
# # # # app.stopLabelFrame()
# # # #
# # # # app.startLabelFrame("Mouse Over", 0, 2)
# # # # app.addImage("mo_1", "test.ppm")
# # # # app.setImageMouseOver("mo_1", "Pie.ppm")
# # # # app.stopLabelFrame()
# # # #
# # # # app.startLabelFrame("Click Me", 0, 3)
# # # # app.addImage("clickme", "test.ppm")
# # # # app.setImageSubmitFunction("clickme", changePic)
# # # # app.stopLabelFrame()
# # # #
# # # # app.startLabelFrame("Zoom", 0, 4)
# # # # app.setPadding([5,5])
# # # # app.setSticky("ew")
# # # # app.startScrollPane("sp")
# # # # app.addImage("Zoom", "test.ppm")
# # # # w, h = app.getImageDimensions("simple")
# # # # app.stopScrollPane()
# # # # #app.setScrollPaneWidth("sp", 150)
# # # # app.addLabelSpinBox("Zoom", [20,5, 4, 3, 2, 1, -2, -3, -4, -5, -6, -7, -8, -9])
# # # # app.setSpinBox("Zoom", 1)
# # # # app.setSpinBoxChangeFunction("Zoom", changePic)
# # # # app.stopLabelFrame()
# # # #
# # # # app.startLabelFrame("No reload", 1, 1)
# # # # app.setSticky("ew")
# # # # app.addImage("no_reload", "test.ppm")
# # # # app.addButton("No reload", changePic)
# # # # app.stopLabelFrame()
# # # #
# # # # app.startLabelFrame("Reload", 1, 2)
# # # # app.setSticky("ew")
# # # # app.addImage("reload", "test.ppm")
# # # # app.addButton("Reload", changePic)
# # # # app.stopLabelFrame()
# # # #
# # # # app.startLabelFrame("Animated", 1, 3)
# # # # app.setSticky("ew")
# # # # app.addImage("animated", "test.ppm")
# # # # app.addLabelScale("Speed")
# # # # app.showScaleValue("Speed")
# # # # app.showScaleIntervals("Speed", 50)
# # # # app.setScaleRange("Speed", 1, 200, 50)
# # # # app.setScaleChangeFunction("Speed", changePic)
# # # # app.addButton("Stop", changePic)
# # # # app.stopLabelFrame()
# # # #
# # # # app.startLabelFrame("Open", 1, 4)
# # # # app.setSticky("ew")
# # # # app.addImage("Open", "Plot.ppm")
# # # # app.addButton("Open", changePic)
# # # # app.stopLabelFrame()
# # # #
# # # # app.go()
# # #
# # # import sys
# # # sys.path.append("../")
# # # from appJar import gui
# # #
# # # clicked = False
# # # animated = True
# # #
# # #
# # # photo="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"
# # #
# # # def changePic(btn):
# # #     if btn == "clickme":
# # #         global clicked
# # #         if clicked: app.setImage("clickme", "balloons.gif")
# # #         else: app.setImage("clickme", "balloons2.png")
# # #         clicked = not clicked
# # #     elif btn == "No reload":
# # #         app.setImage("no_reload", "balloons.gif")
# # #     elif btn == "Reload":
# # #         app.reloadImage("reload", "balloons.gif")
# # #     elif btn == "Stop":
# # #         global animated
# # #         if animated:
# # #             app.stopAnimation("animated")
# # #             app.setButton("Stop", "Start")
# # #         else:
# # #             app.startAnimation("animated")
# # #             app.setButton("Stop", "Stop")
# # #         animated = not animated
# # #     elif btn == "Speed":
# # #         app.setAnimationSpeed("animated", app.getScale("Speed"))
# # #     elif btn == "Zoom":
# # #         app.zoomImage("Zoom", int(app.getSpinBox("Zoom")))
# # #     elif btn == "Open":
# # #         imgPath = app.openBox(title="Open Image", dirName="images", fileTypes=[('images', '*.png'), ('images', '*.jpg'), ('images', '*.gif'), ('images', '*.jpeg'), ('all', '*')])
# # #         if imgPath != "":
# # #             try:
# # #                 app.setImage("Open", imgPath)
# # #             except:
# # #                 app.errorBox("File error", "Unable to open image: " + str(imgPath))
# # #
# # # app=gui("Image Test")
# # # # app.setImageLocation("images")
# # #
# # # app.startLabelFrame("Image Data", 0, 0)
# # # app.addImageData("imgdata", photo)
# # # app.stopLabelFrame()
# # #
# # # app.startLabelFrame("Compound Image", 1, 0)
# # # app.addImage("cimage", "balloons.gif", compound="top")
# # # app.stopLabelFrame()
# # #
# # # def imgMap(pos):
# # #     print(pos)
# # #
# # # app.startLabelFrame("ImageMap", 0, 1)
# # # app.addImage("simple", "balloons.gif")
# # # mapData = {"Yellow": [15,52,77,138], "Red":[75,1,129,138], "White":[137,15,184,127]}
# # # app.setImageMap("simple", imgMap, mapData)
# # # app.stopLabelFrame()
# # #
# # # app.startLabelFrame("Mouse Over", 0, 2)
# # # app.addImage("mo_1", "balloons.gif")
# # # app.setImageMouseOver("mo_1", "balloons2.png")
# # # app.stopLabelFrame()
# # #
# # # app.startLabelFrame("Click Me", 0, 3)
# # # app.addImage("clickme", "balloons.gif")
# # # app.setImageSubmitFunction("clickme", changePic)
# # # app.stopLabelFrame()
# # #
# # # app.startLabelFrame("Zoom", 0, 4)
# # # app.setPadding([5,5])
# # # app.setSticky("ew")
# # # app.startScrollPane("sp")
# # # app.addImage("Zoom", "balloons.gif")
# # # w, h = app.getImageDimensions("simple")
# # # app.stopScrollPane()
# # # #app.setScrollPaneWidth("sp", 150)
# # # app.addLabelSpinBox("Zoom", [20,5, 4, 3, 2, 1, -2, -3, -4, -5, -6, -7, -8, -9])
# # # app.setSpinBox("Zoom", 1)
# # # app.setSpinBoxChangeFunction("Zoom", changePic)
# # # app.stopLabelFrame()
# # #
# # # app.startLabelFrame("No reload", 1, 1)
# # # app.setSticky("ew")
# # # app.addImage("no_reload", "balloons.gif")
# # # app.addButton("No reload", changePic)
# # # app.stopLabelFrame()
# # #
# # # app.startLabelFrame("Reload", 1, 2)
# # # app.setSticky("ew")
# # # app.addImage("reload", "balloons.gif")
# # # app.addButton("Reload", changePic)
# # # app.stopLabelFrame()
# # #
# # # app.startLabelFrame("Animated", 1, 3)
# # # app.setSticky("ew")
# # # app.addImage("animated", "animated_balloons.gif")
# # # app.addLabelScale("Speed")
# # # app.showScaleValue("Speed")
# # # app.showScaleIntervals("Speed", 50)
# # # app.setScaleRange("Speed", 1, 200, 50)
# # # app.setScaleChangeFunction("Speed", changePic)
# # # app.addButton("Stop", changePic)
# # # app.stopLabelFrame()
# # #
# # # app.startLabelFrame("Open", 1, 4)
# # # app.setSticky("ew")
# # # app.addImage("Open", "balloons3.jpg")
# # # app.addButton("Open", changePic)
# # # app.stopLabelFrame()
# # #
# # # app.go()
# #
# # import sys
# # sys.path.append("../")
# #
# # from appJar import gui
# #
# # def mIn(btn):
# #     print("Mouse in:", btn)
# #
# # def mOut(btn):
# #     print("Mouse out:", btn)
# #
# # def sDrag(btn):
# #     print("sDrag:", btn)
# #
# # def eDrag(btn):
# #     print("eDrag:", btn)
# #
# # app = gui("Event 2")
# # app.setFont(20)
# # app.addLabel("l1", "Label 1", 0, 0)
# # app.addLabel("l2", "Label 2", 0, 1)
# # app.addLabel("l3", "Label 3", 1, 0)
# # app.addLabel("l4", "Label 4", 1, 1)
# #
# #
# # app.setLabelOverFunction("l1", [mIn, mOut])
# # app.setLabelDragFunction("l1", [sDrag, eDrag])
# #
# # app.go()
#
# import sys
# sys.path.append("../")
#
# from appJar import gui
#
# def here(data):
#     print(data)
#     return("here")
#
# app=gui()
# app.addLabel("l1", "DnD")
#
# app.addEntry("dnd")
# app.setEntryDropTarget("dnd", None, replace=False)
#
# app.addListBox("l1", [])
# app.setListBoxDropTarget("l1")
#
# app.addMessage("m1", "lots of message text...")
# app.setMessageDragSource("m1", function=here)
#
# app.addTextArea("text")
# app.setTextAreaDropTarget("text", None)
#
# app.addScrolledTextArea("text2a")
# app.setTextAreaDropTarget("text2a", None)
#
# app.addImage("m1", "images/balloons.gif")
# app.setImageDropTarget("m1", None)
#
# app.addLabel("im1", "try here...")
# app.setLabelDropTarget("im1", None)
# app.go()

# import sys
# # # sys.path.append("../")
# # #
# # # from appJar import gui
# # #
# # # def drag(widget):
# # #     print("Dragged from:", widget)
# # #
# # # def drop(widget):
# # #     print("Dropped on:", widget)
# # #
# # # app = gui("dnd Demo")
# # #
# # # app.setFont(20)
# # # app.setBg("SlateGrey")
# # # app.setFg("yellow")
# # #
# # # app.addLabel("dragLab", "Drag Me")
# # # app.addHorizontalSeparator()
# # # app.addLabel("dropLab", "Drop Here")
# # #
# # # app.setLabelDragFunction("dragLab", [drag, drop])
# # #
# # # app.go()

# from appJar import gui
#
# def press(btn):
#     if btn == "info": app.infoBox("Title Here", "Message here...")
#     if btn == "error": app.errorBox("Title Here", "Message here...")
#     if btn == "warning": app.warningBox("Title Here", "Message here...")
#     if btn == "yesno": app.yesNoBox("Title Here", "Message here...")
#     if btn == "question": app.questionBox("Title Here", "Message here...")
#     if btn == "ok": app.okBox("Title Here", "Message here...")
#     if btn == "retry": app.retryBox("Title Here", "Message here...")
#     if btn == "text": app.textBox("Title Here", "Message here...")
#     if btn == "number": app.numberBox("Title Here", "Message here...")
#
# app=gui()
# app.addButtons(["info", "error", "warning", "yesno", "question"], press)
# app.addButtons(["ok", "retry", "text", "number"], press)
# app.go()

# import sys
# # sys.path.append("../")
# #
# #
# # from appJar import gui
# # print(gui.SHOW_VERSION())
# #
# # #from numpy import arange, sin, pi
# #
# # app=gui()
# # #app.setFg("blue")
# # #app.setBg("orange")
# # app.setLogLevel("INFO")
# #
# # app.addCheckBox("cb1", column=0)
# # app.addNamedCheckBox("cb2", "cb2", column=0)
# # app.addScale("s1", column=0)
# # app.addLabelScale("ls1", column=0)
# # app.addOptionBox("o1", ["a", "b"], column=0)
# # app.addTickOptionBox("to1", ["a", "b"], column=0)
# # app.addLabelTickOptionBox("lto1", ["a", "b"], column=0)
# # app.addLabelOptionBox("lo1", ["a", "b"], column=0)
# # app.addLabels(["a", "b", "c", "d"])
# # app.addProperties("p1", {"a": True, "b": False}, row=0, column=1)
# # app.addSpinBox("sb1",["a", "b"], row=1, column=1)
# # app.addLabelSpinBox("sb2",["a", "b"], row=2, column=1)
# # app.addSpinBoxRange("sb3", 5, 11, row=3, column=1)
# # app.addListBox("lb1",["a", "b"], row=4, column=1, rowspan=3)
# # app.addLabelSpinBoxRange("sb4", 5, 11, row=7, column=1)
# # #app.addAnimatedImage(
# # #app.addImageData(name, imageData)
# # #app.addImage(
# # app.addRadioButton("rb1", "rb1", row=8, column=1)
# # app.addRadioButton("rb1", "rb2", row=9, column=1)
# # app.addNamedButton("b1", "b1", None, row=0, column=2)
# # app.addButton("b2", None, row=1, column=2)
# # #app.addImageButton("b2", None, imgFile)
# # app.addButtons(["b3", "b4", "b5",], None, row=2, column=2)
# # app.addWebLink("web", "http://www.google.com", row=3, column=2)
# # app.addDatePicker("dp", row=4, column=2, rowspan=3)
# # app.addTrashBin("tb", row=6, column=2)
# # app.addLink("link", None, row=7, column=2)
# # app.addFlashLabel("fl1", "flash", row=8, column=2)
# # app.addGrip(row=9, column=2)
# # app.addSelectableLabel("sl1", "selectable", row=0, column=3)
# # app.addLabel("l1", "label", row=1, column=3)
# # app.addEmptyLabel("el1", row=2, column=3)
# # app.addMessage("mess", "mess", row=3, column=3)
# # app.addTextArea("ta", row=4, column=3, rowspan=2)
# # app.addEmptyMessage("mess2", row=6, column=3)
# # app.addEntry("e1", row=7, column=3)
# # app.addFileEntry("fe1", row=8, column=3)
# # app.addDirectoryEntry("de1", row=9, column=3)
# # app.addValidationEntry("ve1", row=10, column=3)
# # app.addLabelValidationEntry("lve1", row=11, column=3)
# # app.setEntryValid("ve1")
# # app.setEntryInvalid("lve1")
# #
# # app.addTree("t1",
# #     """<people>
# #     <person><name>Fred</name><age>45</age><gender>Male</gender></person>
# #     <person><name>Tina</name><age>37</age><gender>Female</gender></person>
# #     <person><name>CLive</name><age>28</age><gender>Male</gender></person>
# #     <person><name>Betty</name><age>51</age><gender>Female</gender></person>
# #     </people>""", column=7, row=0, rowspan=5)
# # app.addScrolledTextArea("ta2", row=5, column=7, rowspan=1)
# # #app.addGoogleMap("gm1", column=7, row=1)
# # app.addMicroBit("mb", row=6, column=7, rowspan=7)
# # #t = arange(0.0, 3.0, 0.01)
# # #s = sin(2*pi*t)
# # #app.addPlot("p1", t, s)
# # #app.addGrid("grid", [["A","B","C"], [3,4,5,6,7,8], [2,4,6,8]], action=None, addRow=True)
# #
# # app.addAutoEntry("ae", ["a", "b"], row=0, column=5)
# # app.addLabelAutoEntry("lae1", ["a", "b"], row=1, column=5)
# # app.addNumericEntry("ne1", row=2, column=5)
# # app.addLabelNumericEntry("lne1", row=3, column=5)
# # app.addNumericLabelEntry("lne2", row=4, column=5)
# # app.addSecretEntry("se", row=5, column=5)
# # app.addLabelEntry("le", row=6, column=5)
# # app.addLabelSecretEntry("lse1", row=7, column=5)
# # app.addSecretLabelEntry("lse2", row=8, column=5)
# # app.addMeter("m1", row=0, column=4)
# # app.addSplitMeter("m2", row=1, column=4)
# # app.addDualMeter("m3", row=2, column=4)
# # app.addSeparator(row=3, column=4)
# # app.addHorizontalSeparator(row=4, column=4)
# # app.addVerticalSeparator(row=5, column=4, rowspan=4)
# # #app.addPieChart("p1")
# # app.addProperties("prop", row=6, column=5)
# # def changeFg(btn):
# #     app.setFg(app.colourBox(),
# #         app.getCheckBox("OVER") or app.getMenuCheckBox("Colours", "Override")
# #     )
# #
# # def changeBg(btn):
# #     app.setBg(app.colourBox(),
# #         app.getCheckBox("OVER") or app.getMenuCheckBox("Colours", "Override"),
# #         app.getCheckBox("TINT") or app.getMenuCheckBox("Colours", "Tint")
# #     )
# #
# # app.addButton("FG COL", changeFg, row=9, column=5)
# # app.addButton("BG COL", changeBg, row=10, column=5)
# # app.addCheckBox("OVER", row=11, column=5)
# # app.addCheckBox("TINT", row=12, column=5)
# # app.addMenuList("Colours", ["FG Col", "BG Col"], [changeFg, changeBg])
# # app.addMenuSeparator("Colours")
# # app.addMenuCheckBox("Colours", "Override")
# # app.addMenuCheckBox("Colours", "Tint")
# # app.addMenuSeparator("Colours")
# # app.addMenuItem("Colours", "Quit", app.stop)
# #
# # app.addMenuEdit()
# # app.go()

# import sys
# sys.path.append("../")
# from appJar import gui
#
# def closePop():
#     POP_UP = app.getPopUp()
#     print("closing:", app.getPopUp())
#     if POP_UP is not None: POP_UP.cancel()
#
# def popUp(btn):
#     val = app.getOptionBox("choice")
#     print(val)
#     if val == "info": app.infoBox("a", "a", parent="sub1")
#     elif val == "error": app.errorBox("a", "a", parent="sub1")
#     elif val == "warn": app.warningBox("a", "a", parent="sub1")
#     elif val == "yesno": app.yesNoBox("a", "a", parent="sub1")
#     elif val == "question": app.questionBox("a", "a", parent="sub1")
#     elif val == "ok": app.okBox("a", "a", parent="sub1")
#     elif val == "retry": app.retryBox("a", "a", parent="sub1")
#     elif val == "text": app.textBox("a", "a", parent="sub1")
#     elif val == "number": app.numberBox("a", "a", parent="sub1")
#     elif val == "open": app.openBox("open", parent="sub1")
#     elif val == "save": app.saveBox("save", parent="sub1")
#     elif val == "directory": app.directoryBox("directory", parent="sub1")
#     elif val == "colour": app.colourBox(app.getEntry("colour"), parent="sub1")
#     print("here")
#
# with gui(startWindow="sub1", language="FRENCH") as app:
#     with app.subWindow("sub1"):
#         app.addOptionBox("choice", ["info", "error", "warn", "yesno", "question", "ok", "text", "number", "open", "save", "directory", "colour"])
#         app.addButton("PRESS", popUp)
#         app.addEntry("colour")
#         app.setStopFunction(app.stop)
#
#     app.registerEvent(closePop)
#     app.setPollTime(1000)

# import sys
# sys.path.append("../")
#
# from appJar import gui
#
# def login(btn):
#     app.hideSubWindow("Login")
#     app.show()
#
# def stopSub(btn=None):
#     return False
#
# app = gui()
# app.addLabel("la", "la")
#
# app.startSubWindow("Login")
# app.setStopFunction(stopSub)
# app.addLabel("l2", "Login Window")
# app.addButton("SUBMIT", login)
# app.stopSubWindow()
#
# app.startSubWindow("Other")
# app.addLabel("l3", "Other Window")
# app.stopSubWindow()
#
# app.addButton("Other", app.showSubWindow)
#
# app.go(startWindow="Login")

# import sys
# sys.path.append("../")
# from appJar import gui
#
# def press():
#     print(1)
#     app.check("Apples", True, bg="pink")
#
# with gui(font=20, bg="yellow") as app:
#
#     app.check("Apples", width=10)
#     app.check("Pears", bg="green", fg="red", font=40)
#     app.check("Oranges", True)
#     app.check("Kiwis", change=press, width=40)
#     app.button("PRESS", press)

# import sys
# sys.path.append("../")
# from appJar import gui
#
# left = -40
# right = 5
#
# def mover():
#     global left, right
#     left -=5
#     right += 5
#
#     if left < -100: left = 0
#     if right > 100: right = 0
#
#     if left > right: text = "red"
#     else: text = "green"
#     app.setMeter("progress", [left, right], text)
#
# app=gui()
# app.setGeometry("200x50")
# app.setFont(20)
# app.addDualMeter("progress")
# app.setMeterFill("progress", ["red", "green"])
# app.setMeter("progress", [70, 30])
# app.registerEvent(mover)
# app.go()

# import sys
# sys.path.append("../")
# from appJar import gui
#
# val = 0
# dualVal = [-75, 30]
#
# def update():
#     global val, dualVal
#     val += 5
#     dualVal[0] = dualVal[0] - 5
#     dualVal[1] = dualVal[1] + 5
#     app.setMeter("p1", val)
#     app.setMeter("p11", val, str(val))
#     app.setMeter("p2", val, "bigger")
#     app.setMeter("p3", dualVal)
#     if val == 120: val = 0
#     if dualVal[0] < -100: dualVal[0] = 0
#     if dualVal[1] > 100: dualVal[1] = 0
#
# def show():
#     print("P1:", app.getMeter("p1"))
#     print("P2:", app.getMeter("p2"))
#     print("P3:", app.getMeter("p3"))
#
# app=gui()
# #app.setGeometry("200x150")
# app.setFont(20)
#
# app.addLabel("l1", "Meter - default set")
# app.addMeter("p1")
# app.addLabel("l2", "Meter - string set")
# app.addMeter("p11")
# app.addLabel("l3", "Split Meter 2 vals")
# app.addSplitMeter("p2")
# app.addLabel("l4", "Dual Meter")
# app.addDualMeter("p3")
#
# app.setMeterFill("p1", "pink")
# app.setMeterFill("p11", "black")
# app.setMeterFill("p2", ["green", "red"])
# app.setMeterFill("p3", ["orange", "purple"])
#
# app.setMeterBg("p1", "grey")
# app.setMeterBg("p11", "grey")
# app.setMeterBg("p2", "grey")
# app.setMeterBg("p3", "grey")
#
# app.setMeterFg("p1", "orange")
# app.setMeterFg("p11", "yellow")
# app.setMeterFg("p2", "grey")
# app.setMeterFg("p3", "lightblue")
#
# app.registerEvent(update)
# app.registerEvent(show)
#
# app.go()
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# import matplotlib.pyplot as plt
# # # # fig = plt.figure()
# # # # ax = fig.gca(projection='3d')
# # # #
# # # # ax.plot_trisurf(x, y, z, linewidth=0.2, antialiased=True)
# # # #
# # # # plt.show()
#
# import matplotlib.pyplot as plt
# import numpy as np
#
#
# def f(t):
#     return np.cos(2*np.pi*t) * np.exp(-t)
#
#
# # Set up a figure twice as tall as it is wide
# fig = plt.figure(figsize=plt.figaspect(2.))
# fig.suptitle('A tale of 2 subplots')
#
# # First subplot
# ax = fig.add_subplot(2, 1, 1)
#
# t1 = np.arange(0.0, 5.0, 0.1)
# t2 = np.arange(0.0, 5.0, 0.02)
# t3 = np.arange(0.0, 2.0, 0.01)
#
# ax.plot(t1, f(t1), 'bo',
#         t2, f(t2), 'k--', markerfacecolor='green')
# ax.grid(True)
# ax.set_ylabel('Damped oscillation')
#
# # Second subplot
# ax = fig.add_subplot(2, 1, 2, projection='3d')
#
# X = np.arange(-5, 5, 0.25)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
#
# surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                        linewidth=0, antialiased=False)
# ax.set_zlim(-1, 1)
#
# plt.show()

a = {'a': [1,2,3],'b': [1,2,3]}
# a = list(a.values())[0]
#
i = ''
# print(len(a),)
for name,value in a.items():
    i +=name
    print(i)