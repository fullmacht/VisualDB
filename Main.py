# from appJar import gui
# from datetime import tzinfo, timedelta, datetime, timezone
# import postgresql
# import matplotlib.pyplot as plt
#
# pieName = 0
# subWindowName = 0
# mess = ''
#
#
# class UTC025(tzinfo):
#     def __init__(self, offset=10800, name=None):
#         self.offset = timedelta(seconds=offset)
#         self.name = name or self.__class__.__name__
#
#     def utcoffset(self, dt):
#         return self.offset
#
#     def tzname(self, dt):
#         return self.name
#
#     def dst(self, dt):
#         return timedelta(0)
#
#
# # Функция получения времени для Statusbar'a
# def timeSt():
#     t = datetime.now(UTC025()).strftime('%a, %d %b %Y %H:%M:%S')
#     app.setStatusbar(t)
#
#
# # Функция соединения с БД
# def connectToDb():
#     pass
#     global db
#     global conDb
#     global db
#     db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
#     conDb = postgresql.open(db)
#     try:
#     db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
#             'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
#     except:
#         postgresql.exceptions.ConnectionRejectionError
#     # Здесь к каждой ошибке создаём свое окно infoBox
#         app.infoBox('Результат', 'Неверные данные подключения')
#
#     else:
#         app.infoBox('Результат', 'Покдключение к БД установлено')
#         app.hideSubWindow('Настройки подключения к БД')


# Функция загрузки имён полей
def downlColumNames(button):
    a1 = str(app.getOptionBox('Таблица Оси X'))
    b2 = str(app.getOptionBox('Таблица 2'))
    b3 = str(app.getOptionBox('Таблица 3'))
    с3 = str(app.getOptionBox('Таблица'))
    d4 = str(app.getOptionBox('Таблица для ввода'))
    a1 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + a1 + '\''
    b2 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + b2 + '\''
    b3 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + b3 + '\''
    с3 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + с3 + '\''
    d4 = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + d4 + '\''
    db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    conDb = postgresql.open(db)
    colum1List = conDb.prepare(a1)
    colum2List = conDb.prepare(b2)
    colum3List = conDb.prepare(с3)
    colum4List = conDb.prepare(d4)
    colum5List = conDb.prepare(b3)
    bes = ''
    for i in colum5List:
        bes += str(i)
        bes1 = bes.replace('(', '')
        bes2 = bes1.replace(')', '')
        bes3 = bes2.replace('\'', '')
        bes4 = bes3[:-1]
        bes5 = bes4.split(',')
    if button == 'Выбрать поле таблицы 3':
        app.changeOptionBox('Поле таблицы 3', bes5, callFunction=False)
    des = ''
    for i in colum4List:
        des += str(i)
        des1 = des.replace('(', '')
        des2 = des1.replace(')', '')
        des3 = des2.replace('\'', '')
        des4 = des3[:-1]
        des5 = des4.split(',')
    if button == 'показать столбец':
        app.changeOptionBox('Столбец для ввода', des5, callFunction=False)
    mes = ''
    for i in colum1List:
        mes += str(i)
        mes1 = mes.replace('(', '')
        mes2 = mes1.replace(')', '')
        mes3 = mes2.replace('\'', '')
        mes4 = mes3[:-1]
        mes5 = mes4.split(',')
    if button == 'Выбрать поле таблицы оси X':
        app.changeOptionBox('Поле таблицы оси X', mes5, callFunction=False)
    les = ''
    for i in colum3List:
        les += str(i)
        les1 = les.replace('(', '')
        les2 = les1.replace(')', '')
        les3 = les2.replace('\'', '')
        les4 = les3[:-1]
        les5 = les4.split(',')
    if button == 'Показать столбец':
        app.changeOptionBox('Столбец', les5, callFunction=False)
    nes = ''
    for i in colum2List:
        nes += str(i)
        nes1 = nes.replace('(', '')
        nes2 = nes1.replace(')', '')
        nes3 = nes2.replace('\'', '')
        nes4 = nes3[:-1]
        nes5 = nes4.split(',')
    if button == 'Выбрать поле таблицы 2':
        app.changeOptionBox('Поле таблицы 2', nes5, callFunction=False)


# Функция загрузки списка таблиц
def downlTablesNames(button):
    connectToDb
    db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    conDb = postgresql.open(db)
    tableList = conDb.prepare("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public'")
    mes = ''
    for i in tableList:
        if type(i) is not type(None):
            mes += str(i)
            mes1 = mes.replace('(', '')
            mes2 = mes1.replace(')', '')
            mes3 = mes2.replace('\'', '')
            mes4 = mes3[:-1]
            mes5 = mes4.split(',')
            mes6 = (mes5)
    if button == 'Выбрать таблицу оси X':
        app.changeOptionBox('Таблица Оси X', mes6, callFunction=False)
    elif button == 'Выбрать таблицу 2':
        app.changeOptionBox('Таблица 2', mes6, callFunction=False)
    elif button == 'Выбрать таблицу 3':
        app.changeOptionBox('Таблица 3', mes6, callFunction=False)
    elif button == 'Показать таблицу':
        app.changeOptionBox('Таблица', mes6, callFunction=False)
    elif button == 'показать таблицу':
        app.changeOptionBox('Таблица для ввода', mes6, callFunction=False)
    print(mes6)


# Функция вывода данных из БД в графики
def xAxe():
    global l
    db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    conDb = postgresql.open(db)
    a1 = 'select' + ' ' + str(app.getOptionBox('Поле таблицы оси X')) + ' ' + 'from' + ' ' + str(
        app.getOptionBox('Таблица Оси X'))
    table1Info = conDb.prepare(a1)
    mes = ''
    for i in table1Info:
        mes = mes + str(i)
        mes1 = mes.replace('(', '')
        mes2 = mes1.replace(')', '')
        mes3 = mes2.replace('\'', '')
        mes4 = mes3.replace('Decimal', '')
        mes5 = mes4[:-1]
        mes6 = mes5.split(',')
        l = []
        for p in mes6:
            if p != 'None':
                mes7 = int(p)
                l.append(mes7)
    return l


# def label1():
#     global li
#     db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
#     # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
#     #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
#     conDb = postgresql.open(db)
#     b2 = 'select' + ' ' + str(app.getOptionBox('Поле таблицы 2')) + ' ' + 'from' + ' ' + str(
#         app.getOptionBox('Таблица 2'))
#     table2Info = conDb.prepare(b2)
#     nes = ''
#     for i in table2Info:
#         nes = nes + str(i)
#         nes1 = nes.replace('(', '')
#         nes2 = nes1.replace(')', '')
#         nes3 = nes2.replace('\'', '')
#         nes4 = nes3.replace('Decimal', '')
#         nes5 = nes4[:-1]
#         nes6 = nes5.split(',')
#         li = []
#         for n in nes6:
#             if n != 'None':
#                 nes7 = int(n)
#                 li.append(nes7)
#     return li


# def label2():
#     global la
#     db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
#     # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
#     #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
#     conDb = postgresql.open(db)
#     b2 = 'select' + ' ' + str(app.getOptionBox('Поле таблицы 3')) + ' ' + 'from' + ' ' + str(
#         app.getOptionBox('Таблица 3'))
#     table2Info = conDb.prepare(b2)
#     nes = ''
#     for i in table2Info:
#         nes = nes + str(i)
#         nes1 = nes.replace('(', '')
#         nes2 = nes1.replace(')', '')
#         nes3 = nes2.replace('\'', '')
#         nes4 = nes3.replace('Decimal', '')
#         nes5 = nes4[:-1]
#         nes6 = nes5.split(',')
#         la = []
#         for n in nes6:
#             if n != 'None':
#                 nes7 = int(n)
#                 la.append(nes7)
#     return la


# def subWindPie():
#     # global table1Name
#     # global table2Name
#     global subWindowName
#     global pieName
#     table1Name = app.getOptionBox('Поле таблицы 2')
#     table2Name = app.getOptionBox('Поле таблицы 3')
#     print(table1Name,table2Name)
#     a, b = sum(label1()), sum(label2())
#     subWindowName += 1
#     pieName += 1
#     subWindowName = str(subWindowName)
#     pieName = str(pieName)
#     # Окно Графика тип Pie
#     app.startSubWindow('График Pie' + ' ' + '№' + subWindowName, 'График Pie' + ' ' + '№' + subWindowName)
#     app.addPieChart('График Pie' + ' ' + '№' + pieName, {table1Name: a,table2Name: b})
#     # Кнопки
#     app.addButtons(['Закрыть график Pie' + ' ' + '№' + pieName], push)
#     app.stopSubWindow()
#     app.showSubWindow('График Pie' + ' ' + '№' + subWindowName)
#     pieName = int(pieName)
#     subWindowName = int(subWindowName)


# def subWindGrafik():
#     x = xAxe()
#     y = label1()
#     z = label2()
#     if str(app.getOptionBox('Тип графика')) == 'График':
#         if len(y) == len(x) == len(z):
#             ax.plot(x, y, label=app.getOptionBox('Поле таблицы 2'))
#             ax.plot(x, z, label=app.getOptionBox('Поле таблицы 3'))
#             ax.set_xlabel(app.getOptionBox('Поле таблицы оси X'))
#             ax.set_ylabel('Ось Y')
#             ax.legend()
#             plt.show()
#             app.showSubWindow('График')
#         else:
#             app.infoBox('Ошибка', 'Ошибка размерности')

#
# def clear():
#     app.clearEntry('Имя пользователя')
#     app.clearEntry('Пароль')
#     app.clearEntry('IP')
#     app.clearEntry('Port')
#     app.clearEntry('Название БД')
#     app.setFocus('Имя пользователя')


def selectTableInfo():
    db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    conDb = postgresql.open(db)
    a1 = str(app.getOptionBox('Таблица'))
    b2 = str(app.getOptionBox('Столбец'))
    a1 = 'SELECT' + ' ' + b2 + ' ' + 'FROM' ' ' + a1
    columnInfo = conDb.prepare(a1)
    mes = ''
    for i in columnInfo:
        mes += str(i)
        mes1 = mes.replace(')', '\n')
        mes2 = mes1.replace('(', '')
        mes3 = mes2.replace('Decimal', '')
        mes4 = mes3.replace(',', ' ')
        mes5 = mes4.replace('\'', '')
    mes6 = str(app.getOptionBox('Столбец')) + ':' + '\n' + '\n' + mes5
    app.setTextArea('Показать данные', mes6)

#
# def insertInfo():
#     db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
#     # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
#     #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
#     conDb = postgresql.open(db)
#     d4 = str(app.getOptionBox('Таблица для ввода'))
#     e5 = str(app.getOptionBox('Столбец для ввода'))
#     f6 = str(app.getEntry('Данные'))
#     a1 = 'INSERT INTO' + ' ' + d4 + '(' + e5 + ')' + ' ' + 'VALUES' + ' ' + '(' + f6 + ')'
#     conDb.execute(a1)


def press(button):
    if button == 'Подключиться к БД':
        connectToDb()
        app.hideSubWindow('Настройки подключения к БД')
    elif button == 'Выбрать таблицу оси X':
        app.showSubWindow('Таблица оси X')
        # try:
        downlTablesNames(button)
        # except:
        #     NameError
        #     app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'Выбрать таблицу 2':
        app.showSubWindow('Таблица 2')
        # try:
        downlTablesNames(button)
        # except:
        #     NameError
        #     app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'Выбрать таблицу 3':
        app.showSubWindow('Таблица 3')
        # try:
        downlTablesNames(button)
        # except:
        #     NameError
        #     app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'выбрать поле таблицы оси X':
        app.hideSubWindow('Поле таблицы оси X')
    elif button == 'выбрать поле таблицы 2':
        app.hideSubWindow('Поле таблицы 2')
    elif button == 'выбрать поле таблицы 3':
        # try:
        downlColumNames(button)
        # except:
        #     NameError
        #     app.infoBox('Результат', 'Сначала подключитесь к БД')
        app.hideSubWindow('Поле таблицы 3')
    elif button == 'Выбрать поле таблицы оси X':
        downlColumNames(button)
        app.hideSubWindow('Таблица оси X')
        app.showSubWindow('Поле таблицы оси X')
    elif button == 'Выбрать поле таблицы 2':
        downlColumNames(button)
        app.hideSubWindow('Таблица 2')
        app.showSubWindow('Поле таблицы 2')
    elif button == 'Выбрать поле таблицы 3':
        downlColumNames(button)
        app.hideSubWindow('Таблица 3')
        app.showSubWindow('Поле таблицы 3')
    elif button == 'Очистить поля':
        clear()
    # elif button == 'Создать График':
    #     if str(app.getOptionBox('Тип графика')) == 'График':
    #         # try:
    #             subWindGrafik()
    #         # except:
    #         #     NameError
    #         #     app.infoBox('Результат', 'Сначала подключитесь к БД')
    #     if str(app.getOptionBox('Тип графика')) == 'Pie':
    #         # try:
    #             subWindPie()
    #         # except:
    #         #     NameError
    #         #     app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'Выход':
        app.stop()
    elif button == 'Выход из настроек':
        app.hideSubWindow('Настройки подключения к БД')
    elif button == 'SETTINGS':
        app.showSubWindow('Настройки подключения к БД')
    elif button == 'Показать данные':
        app.showSubWindow(button)
    elif button == 'показать данные':
        selectTableInfo()
    elif button == 'Зактрыть график':
        app.hideSubWindow('График')
    elif button == 'Окно ввода данных':
        app.showSubWindow(button)
    elif button == 'показать таблицу':
        try:
            downlTablesNames(button)
        except:
            NameError
            app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'Показать таблицу':
        try:
            downlTablesNames(button)
        except:
            NameError
            app.infoBox('Результат', 'Сначала подключитесь к БД')
    elif button == 'показать столбец':
        downlColumNames(button)
    elif button == 'Показать столбец':
        downlColumNames(button)
    elif button == 'Ввести данные':
        insertInfo()
    elif button == 'Закрыть':
        app.clearTextArea('Показать данные')
        app.hideSubWindow('Показать данные')
    elif button == 'Очистить окно':
        app.clearTextArea('Показать данные')
    elif button == 'Зактрыть окно':
        app.hideSubWindow('Окно ввода данных')


# def push(btn):
#     global subWindowName
#     global pieName
#     if type(subWindowName) is int:
#         if type(pieName) is int:
#             subWindowName = str(subWindowName)
#             pieName = str(pieName)
#             if btn == 'Закрыть график Pie' + ' ' + '№' + pieName:
#                 app.removePieChart('График Pie' + ' ' + '№' + pieName)
#                 app.destroySubWindow('График Pie' + ' ' + '№' + subWindowName)
#                 subWindowName = int(subWindowName)
#                 pieName = int(pieName)
# left = 25
# def percentComplete():
#     global left
#     left += 25
#     return left
#
#
# def updateMeter():
#     app.setMeter('Загрузка', percentComplete())
#

# Основное окно
# app = gui('VisualDB', 'Fullscreen',useTtk=True)
# app.setTtkTheme("elegance")
# Временное окно входа в программу
# app.showSplash('VisualDB', fill='blue', stripe='black', fg='white', font=44)
# app.addMeter('Загрузка')
# app.setMeterFill('Загрузка', 'green')
# app.registerEvent(updateMeter)
# Выпадающее меню выбора графиков
# app.addLabelOptionBox('Тип графика', ['Pie', 'График'])
# Кнопки
app.addButtons(
    ['Выбрать таблицу оси X', 'Выбрать таблицу 2','Выбрать таблицу 3', 'Создать График', 'Показать данные', 'Окно ввода данных', 'Выход', ],
    press)
app.setButtonTooltip('Выбрать таблицу оси X',"Выберите таблицу из БД для создания графика")
app.setButtonTooltip('Выбрать таблицу 2',"Выберите таблицу из БД для создания графика")
app.setButtonTooltip('Выбрать таблицу 3',"Выберите таблицу из БД для создания графика")
app.setButtonTooltip('Создать График',"Создайте график в отдельном окне")
app.setButtonTooltip('Показать данные',"Посмотрите данные из таблицы в этом окне")
app.setButtonTooltip('Окно ввода данных',"Дополните таблицу информацией")
app.setButtonTooltip('Выход',"Выйти из программы")
app.setOptionBoxTooltip('Тип графика',
                        "Нажмите, чтобы выбрать подходящий график. Для графика 'Pie' выберите таблицы 2 и 3. Они будут использоваться для построения графика 'Pie'")
app.addToolbarButton('SETTINGS', press, findIcon=True)
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
app.setLabelTooltip('IP',"Введите здесь IP Базы Данных")
app.addLabelEntry('Port')
app.addLabelEntry('Название БД')
# Подписывает действие внутри строки
app.setEntryTooltip('IP',"Введите здесь Ip Базы Данных")
app.setEntryDefault('Имя пользователя', 'Введите имя пользователя')
app.setEntryDefault('Пароль', 'Введите пароль')
app.setEntryDefault('IP', 'Введите IP')
app.setEntryDefault('Port', 'Введите PORT')
app.setEntryDefault('Название БД', 'Введите название БД')
# Устанавливает курсор на строке ввода
app.setFocus('Имя пользователя')
# Устанавливает размер окна
app.setSize('Fullscreen')
#app.exitFullscreen()
app.stopSubWindow()
# Окно показа графика
app.startSubWindow('График', 'График')
fig = app.addPlotFig('p1')
ax = fig.subplots()
# Кнопки
app.addButtons(['Зактрыть график'], press)
app.setButtonTooltip('Зактрыть график', 'Закрыть окно с графиком')
app.stopSubWindow()
# подокно Показать данные
app.startSubWindow('Показать данные', 'Показать данные', modal=False, blocking=False, transient=True, )
app.setSize('Fullscreen')
app.addButtons(['Показать таблицу', 'Показать столбец', 'показать данные'], press)
app.setFont(20)
app.addLabelOptionBox('Таблица', mess)
app.addLabelOptionBox('Столбец', mess)
app.addTextArea(title='Показать данные', text=mess)
app.addButtons(['Очистить окно', 'Закрыть'], press)
#app.exitFullscreen()
app.stopSubWindow()
# окно ввода данных
app.startSubWindow('Окно ввода данных', 'Окно ввода данных')
app.setSize('Fullscreen')
app.addLabelEntry('Данные')
app.setEntryDefault('Данные', 'Введите данные')
app.setFocus('Данные')
app.addButtons(['Ввести данные', 'показать таблицу', 'показать столбец', 'Зактрыть окно'], press)
app.addLabelOptionBox('Таблица для ввода', mess)
app.addLabelOptionBox('Столбец для ввода', mess)
#app.exitFullscreen()
app.stopSubWindow()
# подокно Таблица оси X
app.startSubWindow('Таблица оси X')
app.addLabelOptionBox('Таблица Оси X', ['Выберите таблицу 1'])
app.addButton('Выбрать поле таблицы оси X', press)
app.stopSubWindow()
# Подокно таблица 2
app.startSubWindow('Таблица 2')
app.addLabelOptionBox('Таблица 2', ['Выберите таблицу 2'])
app.addButtons(['Выбрать поле таблицы 2'], press)
app.stopSubWindow()
# подокно таблица 3
app.startSubWindow('Таблица 3')
app.addLabelOptionBox('Таблица 3', ['Выберите таблицу 3'])
app.addButtons(['Выбрать поле таблицы 3'], press)
app.stopSubWindow()
# Подокно поле таблицы оси X
app.startSubWindow('Поле таблицы оси X')
app.addLabelOptionBox('Поле таблицы оси X', ['Выберите столбец 3'])
app.addButtons(['выбрать поле таблицы оси X'], press)
app.stopSubWindow()
# Подокно выбора таблицы 2
app.startSubWindow('Поле таблицы 2')
app.addLabelOptionBox('Поле таблицы 2', ['Выберите столбец 2'])
app.addButtons(['выбрать поле таблицы 2'], press)
app.stopSubWindow()
# Подокно выбора таблицы 3
app.startSubWindow('Поле таблицы 3')
app.addLabelOptionBox('Поле таблицы 3', ['Выберите столбец 3'])
app.addButtons(['выбрать поле таблицы 3'], press)
app.stopSubWindow()
# Устанавливает размер окна
#app.exitFullscreen()
app.go()
