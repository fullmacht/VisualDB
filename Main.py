from numpy import sin, pi, arange
from appJar import gui
import random
from time import strftime, gmtime
import postgresql
import matplotlib.pyplot as plt

table1Name = 'Таблица 1'
table2Name = 'Таблица 2'
pieName = 0
subWindowName = 0
# Функция получения времени для Statusbar'a
def timeSt():
    t = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    app.setStatusbar(t)


# Функция загрузки имён полей
def downlColumNames():
    a1 = str(app.getOptionBox("Таблица 1"))
    b2 = str(app.getOptionBox("Таблица 2"))
    a1 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + a1 + '\''
    b2 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + b2 + '\''
    conDb = postgresql.open(db)
    colum1List = conDb.prepare(a1)
    colum2List = conDb.prepare(b2)
    mes = ''
    # app.getOptionBox("Поле таблицы 1")
    # app.getOptionBox("Поле таблицы 2")
    # app.getOptionBox("Тип графика")
    for i in colum1List:
        mes += str(i)
        mes1 = mes.replace("(", '')
        mes2 = mes1.replace(')', '')
        mes3 = mes2.replace("'", "")
        # count = mes3.count(",")
        mes4 = mes3[:-1]
        mes5 = mes4.split(',')
    app.changeOptionBox('Поле таблицы 1', mes5, callFunction=False)
    nes = ''
    for i in colum2List:
        nes += str(i)
        nes1 = nes.replace("(", '')
        nes2 = nes1.replace(')', '')
        nes3 = nes2.replace("'", "")
        # count = mes3.count(",")
        nes4 = nes3[:-1]
        nes5 = nes4.split(',')
    app.changeOptionBox('Поле таблицы 2', nes5, callFunction=False)
    # Забираем имена полей из БД , парсим и вставляем их в changeOptionBox выбора полей для JOIN


# Функция загрузки списка таблиц
def downlTablesNames():
    conDb = postgresql.open(db)
    tableList = conDb.prepare("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public'")
    mes = ''
    for i in tableList:
        mes += str(i)
        mes1 = mes.replace("(", '')
        mes2 = mes1.replace(')', '')
        mes3 = mes2.replace("'", "")
        # count = mes3.count(",")
        mes4 = mes3[:-1]
        mes5 = mes4.split(',')
    app.changeOptionBox("Таблица 1", mes5, callFunction=False)
    app.changeOptionBox("Таблица 2", mes5, callFunction=False)
    # Забираем имена доступных таблиц из БД, парсим и вставляем их в changeOptionBox выбора


# Функция соединения с БД
def connectToDb():
    global db
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    db = 'pq://' + "postgres" + ':' + "1234" + '@' + "localhost" + ':' + "5432" + '/' + "postgres"
    downlTablesNames()
    # try:
    #     conDb = postgresql.open(db)

    # except:
        # Здесь к каждой ошибке создаём свое окно infoBox

    # else:
        # app.infoBox('Результат', 'Покдключение к БД установлено')
        # downlTablesNames()
    # downlColumNames()


# Функция вывода данных из БД в графики
def showGrafInfo():
    conDb = postgresql.open(db)
    a1 ='select' + ' ' + str(app.getOptionBox("Поле таблицы 1")) + ' ' + 'from' + ' ' + str(app.getOptionBox("Таблица 1"))
    table1Info = conDb.prepare(a1)
    mes = ''
    for i in table1Info:
        mes = mes + str(i)
        mes1 = mes.replace("(", '')
        mes2 = mes1.replace(')', '')
        mes3 = mes2.replace("'", "")
        mes4 = mes3.replace("Decimal", '')
        # count = mes3.count(",")
        mes5 = mes4[:-1]
        mes6 = mes5.split(',')
        l = []
        for n in mes6:
            mes7 = int(n)
            l.append(mes7)
            print(l)
    # Берёт инфу из JOIN выбранных колонн, парсит вставляет в параметры графика, создаёт график



#Здесь будут браться значения из таблиц для вывода в графики
def getXY():
    x = arange(0.0, 3.0, 0.01)
    y = sin(random.randint(1, 10) * pi * x)
    if str(app.getOptionBox("Тип графика")) == "График":
        return x, y
    if str(app.getOptionBox("Тип графика")) == "Pie":
        global a
        global b
        a = 55
        b = 99
        return a, b


def generate():
    app.updatePlot("p1", *getXY())
    showLabels()


def showLabels():
    axes.legend(['The curve'])
    axes.set_xlabel("X Axes")
    axes.set_ylabel("Y Axes")
    app.refreshPlot("p1")


def press(button):

    global table1Name
    global table2Name
    global subWindowName
    global pieName

    if button == 'Подключиться к БД':
        connectToDb()
        app.hideSubWindow('Настройки подключения к БД')
    elif button == "Выбрать таблицы":
        downlColumNames()
    elif button == 'Очистить поля':
        app.clearEntry("Пользователь")
        app.clearEntry("Пароль")
    elif button == 'Создать График':
        if str(app.getOptionBox("Тип графика")) == "График":
            showGrafInfo()
            # Здесь будет функция получния данных из таблиц вместо getXY
            app.updatePlot("p1", *getXY())
            showLabels()
            app.showSubWindow("График")
        if str(app.getOptionBox("Тип графика")) == "Pie":
            a, b = getXY()
            subWindowName += 1
            pieName += 1
            subWindowName = str(subWindowName)
            pieName = str(pieName)
            # Окно Графика тип Pie
            app.startSubWindow("График Pie" + " " + "№" + subWindowName, "График Pie" + " " + "№" + subWindowName)

            app.addPieChart("График Pie" + " " + "№" + pieName, {table1Name: a, table2Name: b})
            # Кнопки
            app.addButtons(["Закрыть график Pie" + " " + "№" + pieName], push)

            # Устанавливает размер окна
            app.stopSubWindow()
            # app.setPieChart(title="График Pie" + " " + pieName, name=table1Name, value=a)
            # app.setPieChart(title="График Pie" + " " + pieName, name=table2Name, value=b)
            app.showSubWindow("График Pie" + " " + "№" + subWindowName)
            pieName = int(pieName)
            subWindowName = int(subWindowName)
    elif button == 'Выход':
        app.stop()
    elif button == 'Выход из настроек':
        app.hideSubWindow('Настройки подключения к БД')
    elif button == 'SETTINGS':
        app.showSubWindow('Настройки подключения к БД')
    elif button == "Зактрыть график":
        app.hideSubWindow("График")


def push(btn):
    global subWindowName
    global pieName
    if type(subWindowName) is int:
        if type(pieName) is int:
            subWindowName = str(subWindowName)
            pieName = str(pieName)
            if btn == "Закрыть график Pie" + ' ' + "№" + pieName:
                app.removePieChart("График Pie" + " " + "№" + pieName)
                app.destroySubWindow("График Pie" + " " + "№" + subWindowName)
                subWindowName = int(subWindowName)
                pieName = int(pieName)
# Основное окно
app = gui('Project-X', 'Fullscreen')

# Временное окно входа в программу
# app.showSplash("Project-X", fill='blue', stripe='black', fg='white', font=44)

# Выпадающее меню графиков
app.addLabelOptionBox("Таблица 1", ["A", "Б"])
app.addLabelOptionBox("Таблица 2", ["Б", "S"])
app.addLabelOptionBox("Поле таблицы 1", ["1", '2'])
app.addLabelOptionBox("Поле таблицы 2", ["2", " 3"])
app.addLabelOptionBox("Тип JOIN", ["FULL", "LEFT", "RIGHT", "INNER"])
app.addLabelOptionBox("Тип графика", ["Pie", "График"])

# Кнопки
app.addButtons(['Выход', 'Создать График','Выбрать таблицы'], press)
app.addToolbarButton("SETTINGS", press, findIcon=True)

# Statusbar с локальным временем
app.addStatusbar()
app.registerEvent(timeSt)

# Окно настройки соединения
app.startSubWindow('Настройки подключения к БД', 'Настройки подключения к БД', modal=False, blocking=False,
                   transient=True,
                   grouped=True)

# Кнопки
app.addButtons(['Выход из настроек', 'Подключиться к БД', 'Очистить поля', ], press)

# Названия строк
app.addLabelEntry('Пользователь')
app.addLabelSecretEntry('Пароль')
app.addLabelEntry('IP')
app.addLabelEntry('Port')
app.addLabelEntry('Название БД')

# Подписывает действие внутри строки
app.setEntryDefault('Пользователь', 'Введите имя пользователя')
app.setEntryDefault('Пароль', 'Введите пароль')
app.setEntryDefault('IP', 'Введите IP')
app.setEntryDefault('Port', 'Введите PORT')
app.setEntryDefault('Название БД', 'Введите название БД')

# Устанавливает курсор на строке ввода
app.setFocus('Пользователь')

# Устанавливает размер окна
app.setSize("Fullscreen")
app.exitFullscreen()
app.stopSubWindow()

# Окно показа графика
app.startSubWindow("График", "График")

axes = app.addPlot('p1', [1,2],[3,4])

showLabels()

# app.addButton("Generate", generate)

# Кнопки
app.addButtons(["Зактрыть график"], press)

# Устанавливает размер окна

app.stopSubWindow()

# # Окно Графика тип Pie
# app.startSubWindow("График Pie", "График Pie")
#
# app.addPieChart("Pie", {table1Name: 50})
# # Кнопки
# app.addButtons(["Закрыть график Pie"], press)
#
# # Устанавливает размер окна
# app.stopSubWindow()
app.exitFullscreen()

app.go()

# Пример окна со скроллингом
# app = gui("appJar Testing")
# #app.setStretch("none")
# #app.setFont(15)
# #app.setGeometry("600x400")
#
# app.startScrollPane("sp1")
# for x in range(0,40):
#     label_name = "l" + str(x)
#     app.addLabel(label_name, "This is inside scroll pane.")
# app.stopScrollPane()
#
# app.go()
