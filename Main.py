from numpy import sin, pi, arange
from appJar import gui
import random
from datetime import tzinfo, timedelta, datetime, timezone
import postgresql
import matplotlib.pyplot as plt

table1Name = 'Таблица 1'
table2Name = 'Таблица 2'
pieName = 0
subWindowName = 0


class UTC025(tzinfo):
    def __init__(self, offset=10800, name=None):
        self.offset = timedelta(seconds=offset)
        self.name = name or self.__class__.__name__

    def utcoffset(self, dt):
        return self.offset

    def tzname(self, dt):
        return self.name

    def dst(self, dt):
        return timedelta(0)


# Функция получения времени для Statusbar'a
def timeSt():
    t = datetime.now(UTC025()).strftime("%a, %d %b %Y %H:%M:%S")
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
    for i in colum1List:
        mes += str(i)
        mes1 = mes.replace("(", '')
        mes2 = mes1.replace(')', '')
        mes3 = mes2.replace("'", "")
        mes4 = mes3[:-1]
        mes5 = mes4.split(',')
    app.changeOptionBox('Поле таблицы 1', mes5, callFunction=False)
    nes = ''
    for i in colum2List:
        nes += str(i)
        nes1 = nes.replace("(", '')
        nes2 = nes1.replace(')', '')
        nes3 = nes2.replace("'", "")
        nes4 = nes3[:-1]
        nes5 = nes4.split(',')
    app.changeOptionBox('Поле таблицы 2', nes5, callFunction=False)


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
        mes4 = mes3[:-1]
        mes5 = mes4.split(',')
    app.changeOptionBox("Таблица 1", mes5, callFunction=False)
    app.changeOptionBox("Таблица 2", mes5, callFunction=False)
    # Забираем имена доступных таблиц из БД, парсим и вставляем их в changeOptionBox выбора


# Функция соединения с БД
def connectToDb():
    global db

    db = 'pq://' + "postgres" + ':' + "123" + '@' + "localhost" + ':' + "5432" + '/' + "postgres"
    downlTablesNames()
    app.hideSubWindow('Настройки подключения к БД')
    # try:
    #     db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #         'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    #     downlTablesNames()
    # except:
    #     postgresql.exceptions.ConnectionRejectionError
    # # Здесь к каждой ошибке создаём свое окно infoBox
    #     app.infoBox('Результат', 'Неверные данные подключения')
    #
    # else:
    #     app.infoBox('Результат', 'Покдключение к БД установлено')
    #     app.hideSubWindow('Настройки подключения к БД')


# Функция вывода данных из БД в графики
def showGrafInfo():
    global l
    global li
    conDb = postgresql.open(db)
    a1 = 'select' + ' ' + str(app.getOptionBox("Поле таблицы 1")) + ' ' + 'from' + ' ' + str(
        app.getOptionBox("Таблица 1"))
    table1Info = conDb.prepare(a1)
    mes = ''
    for i in table1Info:
        mes = mes + str(i)
        mes1 = mes.replace("(", '')
        mes2 = mes1.replace(')', '')
        mes3 = mes2.replace("'", "")
        mes4 = mes3.replace("Decimal", '')
        mes5 = mes4[:-1]
        mes6 = mes5.split(',')
        l = []
        for n in mes6:
            mes7 = int(n)
            l.append(mes7)
    b2 = 'select' + ' ' + str(app.getOptionBox("Поле таблицы 2")) + ' ' + 'from' + ' ' + str(
        app.getOptionBox("Таблица 2"))
    table2Info = conDb.prepare(b2)
    nes = ''
    for i in table2Info:
        nes = nes + str(i)
        nes1 = nes.replace("(", '')
        nes2 = nes1.replace(')', '')
        nes3 = nes2.replace("'", "")
        nes4 = nes3.replace("Decimal", '')
        nes5 = nes4[:-1]
        nes6 = nes5.split(',')
        li = []
        for n in nes6:
            nes7 = int(n)
            li.append(nes7)
    if str(app.getOptionBox("Тип графика")) == "График":
        return l, li
    elif str(app.getOptionBox("Тип графика")) == "Pie":
        return sum(l), sum(li)


def showLabels():
    axes.legend([app.getOptionBox("Таблица 1") + " " + app.getOptionBox("Таблица 2")])
    axes.set_xlabel(str(app.getOptionBox("Поле таблицы 1")))
    axes.set_ylabel(str(app.getOptionBox("Поле таблицы 2")))
    app.refreshPlot("p1")


def subWindPie():
    global subWindowName
    global pieName
    a, b = showGrafInfo()
    subWindowName += 1
    pieName += 1
    subWindowName = str(subWindowName)
    pieName = str(pieName)
    # Окно Графика тип Pie
    app.startSubWindow("График Pie" + " " + "№" + subWindowName, "График Pie" + " " + "№" + subWindowName)
    app.addPieChart("График Pie" + " " + "№" + pieName, {table1Name: a, table2Name: b})
    # Кнопки
    app.addButtons(["Закрыть график Pie" + " " + "№" + pieName], push)
    app.stopSubWindow()
    app.showSubWindow("График Pie" + " " + "№" + subWindowName)
    pieName = int(pieName)
    subWindowName = int(subWindowName)


def subWindGrafik():
    app.updatePlot("p1", *showGrafInfo())
    showLabels()
    app.showSubWindow("График")


def clear():
    app.clearEntry("Имя пользователя")
    app.clearEntry("Пароль")
    app.setFocus('Имя пользователя')


def press(button):
    global table1Name
    global table2Name
    if button == 'Подключиться к БД':
        connectToDb()
    elif button == "Выбрать таблицы":
        try:
            downlColumNames()
        except:
            NameError
            app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'Очистить поля':
        clear()
    elif button == 'Создать График':
        if str(app.getOptionBox("Тип графика")) == "График":
            try:
                subWindGrafik()
            except:
                NameError
                app.infoBox('Результат', 'Сначала подключитесь к БД')
        if str(app.getOptionBox("Тип графика")) == "Pie":
            try:
                subWindPie()
            except:
                NameError
                app.infoBox('Результат', 'Сначала подключитесь к БД')
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
# app.showSplash("VisualDB", fill='blue', stripe='black', fg='white', font=44)
# Выпадающее меню графиков
app.addLabelOptionBox("Таблица 1", ["A", "Б"])
app.addLabelOptionBox("Таблица 2", ["Б", "S"])
app.addLabelOptionBox("Поле таблицы 1", ["1", '2'])
app.addLabelOptionBox("Поле таблицы 2", ["2", " 3"])
# app.addLabelOptionBox("Тип JOIN", ["FULL", "LEFT", "RIGHT", "INNER"])
app.addLabelOptionBox("Тип графика", ["Pie", "График"])
# Кнопки
app.addButtons(['Выход', 'Создать График', 'Выбрать таблицы'], press)
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
app.addLabelEntry('Имя пользователя')
app.addLabelSecretEntry('Пароль')
app.addLabelEntry('IP')
app.addLabelEntry('Port')
app.addLabelEntry('Название БД')
# Подписывает действие внутри строки
app.setEntryDefault('Имя пользователя', 'Введите имя пользователя')
app.setEntryDefault('Пароль', 'Введите пароль')
app.setEntryDefault('IP', 'Введите IP')
app.setEntryDefault('Port', 'Введите PORT')
app.setEntryDefault('Название БД', 'Введите название БД')
# Устанавливает курсор на строке ввода
app.setFocus('Имя пользователя')
# Устанавливает размер окна
app.setSize("Fullscreen")
app.exitFullscreen()
app.stopSubWindow()
# Окно показа графика
app.startSubWindow("График", "График")
axes = app.addPlot('p1', [1, 2], [3, 4])
showLabels()
# Кнопки
app.addButtons(["Зактрыть график"], press)
app.stopSubWindow()
# Устанавливает размер окна
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
