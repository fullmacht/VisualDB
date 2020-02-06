from appJar import gui
from datetime import tzinfo, timedelta, datetime, timezone
import postgresql

table1Name = 'Таблица 1'
table2Name = 'Таблица 2'
pieName = 0
subWindowName = 0
mess = ['a','b']


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


# Функция соединения с БД
def connectToDb():
    pass
    # global db
    # global conDb
    # global db
    # db = 'pq://' + "postgres" + ':' + "1234" + '@' + "localhost" + ':' + "5432" + '/' + "postgres"
    # conDb = postgresql.open(db)
    # try:
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #         'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    # except:
    #     postgresql.exceptions.ConnectionRejectionError
    # # Здесь к каждой ошибке создаём свое окно infoBox
    #     app.infoBox('Результат', 'Неверные данные подключения')
    #
    # else:
    #     app.infoBox('Результат', 'Покдключение к БД установлено')
    #     app.hideSubWindow('Настройки подключения к БД')


# Функция загрузки имён полей
def downlColumNames():
    a1 = str(app.getOptionBox("Таблица 1"))
    b2 = str(app.getOptionBox("Таблица 2"))
    с3 = str(app.getOptionBox("Таблица"))
    d4 = str(app.getOptionBox("Таблица для ввода"))
    a1 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + a1 + '\''
    b2 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + b2 + '\''
    с3 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + с3 + '\''
    d4 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + d4 + '\''
    connectToDb
    db = 'pq://' + "postgres" + ':' + "1234" + '@' + "localhost" + ':' + "5432" + '/' + "postgres"
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    conDb = postgresql.open(db)
    colum1List = conDb.prepare(a1)
    colum2List = conDb.prepare(b2)
    colum3List = conDb.prepare(с3)
    colum4List = conDb.prepare(d4)
    des = ''
    for i in colum4List:
        des += str(i)
        des1 = des.replace("(", '')
        des2 = des1.replace(')', '')
        des3 = des2.replace("'", "")
        des4 = des3[:-1]
        des5 = des4.split(',')
        app.changeOptionBox("Столбец для ввода", sorted(des5), callFunction=False)
    mes = ''
    for i in colum1List:
        mes += str(i)
        mes1 = mes.replace("(", '')
        mes2 = mes1.replace(')', '')
        mes3 = mes2.replace("'", "")
        mes4 = mes3[:-1]
        mes5 = mes4.split(',')
        app.changeOptionBox('Поле таблицы 1', sorted(mes5), callFunction=False)
    les = ''
    for i in colum3List:
        les += str(i)
        les1 = les.replace("(", '')
        les2 = les1.replace(')', '')
        les3 = les2.replace("'", "")
        les4 = les3[:-1]
        les5 = les4.split(',')
        app.changeOptionBox('Столбец', sorted(les5), callFunction=False)
    nes = ''
    for i in colum2List:
        nes += str(i)
        nes1 = nes.replace("(", '')
        nes2 = nes1.replace(')', '')
        nes3 = nes2.replace("'", "")
        nes4 = nes3[:-1]
        nes5 = nes4.split(',')
        app.changeOptionBox('Поле таблицы 2', sorted(nes5), callFunction=False)


# Функция загрузки списка таблиц
def downlTablesNames():
    connectToDb
    db = 'pq://' + "postgres" + ':' + "1234" + '@' + "localhost" + ':' + "5432" + '/' + "postgres"
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    conDb = postgresql.open(db)
    tableList = conDb.prepare("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public'")
    mes = ''
    for i in tableList:
        if type(i) is not type(None):
            mes += str(i)
            mes1 = mes.replace("(", '')
            mes2 = mes1.replace(')', '')
            mes3 = mes2.replace("'", "")
            mes4 = mes3[:-1]
            mes5 = mes4.split(',')
            mes6 = sorted(mes5)
            app.changeOptionBox("Таблица 1", mes6, callFunction=False)
            app.changeOptionBox("Таблица 2", mes6, callFunction=False)
            app.changeOptionBox("Таблица", mes6, callFunction=False)
            app.changeOptionBox("Таблица для ввода", mes6, callFunction=False)


# Функция вывода данных из БД в графики
def showGrafInfo():
    global l
    global li
    connectToDb
    db = 'pq://' + "postgres" + ':' + "1234" + '@' + "localhost" + ':' + "5432" + '/' + "postgres"
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
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
        for p in mes6:
            if p != 'None':
                mes7 = int(p)
                l.append(mes7)
                print('l', l)
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
            if n != 'None':
                nes7 = int(n)
                li.append(nes7)
                print('li', li)
    if str(app.getOptionBox("Тип графика")) == "График":
        if len(l) == len(li):
            return l, li
        else:
            app.infoBox('Ошибка', 'Размерности')
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


def selectTableInfo():
    connectToDb
    db = 'pq://' + "postgres" + ':' + "1234" + '@' + "localhost" + ':' + "5432" + '/' + "postgres"
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    conDb = postgresql.open(db)
    a1 = str(app.getOptionBox("Таблица"))
    b2 = str(app.getOptionBox("Столбец"))
    a1 = 'SELECT' + ' ' + b2 + ' ' + 'FROM' ' ' + a1
    columnInfo = conDb.prepare(a1)
    mes = ''
    for i in columnInfo:
        mes += str(i)
        mes1 = mes.replace(")", "\n")
        mes2 = mes1.replace("(", "")
        mes3 = mes2.replace("Decimal", "")
        mes4 = mes3.replace(",", " ")
        mes5 = mes4.replace("'", "")
    mes6 = str(app.getOptionBox("Столбец")) + ':' + '\n' + '\n' + mes5
    app.setTextArea('Показать данные', mes6)


def insertInfo():
    db = 'pq://' + "postgres" + ':' + "1234" + '@' + "localhost" + ':' + "5432" + '/' + "postgres"
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    conDb = postgresql.open(db)
    d4 = str(app.getOptionBox("Таблица для ввода"))
    e5 = str(app.getOptionBox("Столбец для ввода"))
    f6 = str(app.getEntry('Данные'))
    a1 = 'INSERT INTO' + ' ' + d4 + '(' + e5 + ')' + ' ' + 'VALUES' + ' ' + '(' + f6 + ')'
    # try:
    conDb.execute(a1)

    print(a1)


def press(button):
    global table1Name
    global table2Name
    if button == 'Подключиться к БД':
        connectToDb()
        app.hideSubWindow('Настройки подключения к БД')
    elif button == "Показать таблицы":
        # try:
            downlTablesNames()
        # except:
        #     NameError
        #     app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == "Показать столбцы":
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
    elif button == 'Показать данные':
        app.showSubWindow(button)
    elif button == 'Показать таблицу':
        try:
            downlTablesNames()
        except:
            NameError
            app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'Показать столбец':
        try:
            downlColumNames()
        except:
            NameError
            app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'показать данные':
        selectTableInfo()
    elif button == "Зактрыть график":
        app.hideSubWindow("График")
    elif button == 'Окно ввода данных':
        app.showSubWindow(button)
    elif button == 'показать таблицу':
        try:
            downlTablesNames()
        except:
            NameError
            app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'показать столбец':
        downlColumNames()
    elif button == "показать столбцы":
        try:
            downlColumNames()
        except:
            NameError
            app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'Ввести данные':
        insertInfo()
    elif button == 'Закрыть':
        app.clearTextArea('Показать данные')
        app.hideSubWindow('Показать данные')
    elif button == 'Очистить окно':
        app.clearTextArea('Показать данные')
    elif button == 'Зактрыть окно':
        app.hideSubWindow('Окно ввода данных')


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
app = gui('VisualDB', 'Fullscreen')
# Временное окно входа в программу
app.showSplash("VisualDB", fill='blue', stripe='black', fg='white', font=44)
# Выпадающее меню графиков
app.addLabelOptionBox("Таблица 1", ["A", "Б"])
app.addLabelOptionBox("Таблица 2", ["Б", "S"])
app.addLabelOptionBox("Поле таблицы 1", ["1", '2'])
app.addLabelOptionBox("Поле таблицы 2", ["2", " 3"])
# app.addLabelOptionBox("Тип JOIN", ["FULL", "LEFT", "RIGHT", "INNER"])
app.addLabelOptionBox("Тип графика", ["Pie", "График"])
# Кнопки
app.addButtons(
    ['Показать таблицы', 'Показать столбцы', 'Создать График', 'Показать данные', 'Окно ввода данных', 'Выход', ],
    press)
app.addToolbarButton("SETTINGS", press, findIcon=True)
# Statusbar с локальным временем
app.addStatusbar()
app.registerEvent(timeSt)
# Окно настройки соединения
app.startSubWindow('Настройки подключения к БД', 'Настройки подключения к БД', modal=False, blocking=False,
                   transient=True,
                   grouped=True)
# Кнопки
app.addButtons(['Подключиться к БД', 'Очистить поля', 'Выход из настроек', ], press)
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
# подокно Показать данные
app.startSubWindow('Показать данные', 'Показать данные', modal=False, blocking=False, transient=True, )
app.addButtons(['Показать таблицу', 'Показать столбец', 'показать данные'], press)
app.setFont(20)
app.addLabelOptionBox("Таблица", mess)
app.addLabelOptionBox("Столбец", mess)
app.addTextArea(title='Показать данные', text=mess)
app.addButtons(['Очистить окно', "Закрыть"], press)
app.exitFullscreen()
app.stopSubWindow()
# окно ввода данных
app.startSubWindow('Окно ввода данных', 'Окно ввода данных')
app.addLabelEntry('Данные')
app.setEntryDefault('Данные', 'Введите данные')
app.setFocus('Данные')
app.addButtons(['Ввести данные', 'показать таблицу', 'показать столбец', 'Зактрыть окно'], press)
app.addLabelOptionBox("Таблица для ввода", mess)
app.addLabelOptionBox("Столбец для ввода", mess)
app.exitFullscreen()
app.stopSubWindow()
# Устанавливает размер окна
app.exitFullscreen()
app.go()
