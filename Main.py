from numpy import sin, pi, arange
from appJar import gui
import random
from time import strftime, gmtime
import matplotlib.pyplot as plt

count = 0


# Функция получения времени для Statusbar'a
def timeSt():
    t = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    app.setStatusbar(t)


# Функция загрузки имён полей
def downlColumNames():
    pass
    app.changeOptionBox('Таблица 1', newOptions, callFunction=False)
    app.changeOptionBox('Таблица 2', newOptions, callFunction=False)
    # Забираем имена полей из БД , парсим и вставляем их в changeOptionBox выбора полей для JOIN


# Функция загрузки списка таблиц
def downlTablesNames():
    pass
    conDb
    app.changeOptionBox("Поле таблицы 1", newOptions, callFunction=False)
    app.changeOptionBox("Поле таблицы 2", newOptions, callFunction=False)
    # Забираем имена доступных таблиц из БД, парсим и вставляем их в changeOptionBox выбора


# Функция соединения с БД
def connectToDb():
    db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
        'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    global conDb
    try:
        conDb = ''
        pass
    except:
        # Здесь к каждой ошибке создаём свое окно infoBox
        pass
    else:
        app.infoBox('Результат', 'Покдключение к БД установлено')
    downlTablesNames()
    downlColumNames()


# Функция вывода данных из БД в графики
def showGrafInfo():
    # Берёт инфу из JOIN выбранных колонн, парсит вставляет в параметры графика, создаёт график

    app.getOptionBox("Таблица 1")
    app.getOptionBox("Таблица 2")
    app.getOptionBox("Поле таблицы 1")
    app.getOptionBox("Поле таблицы 2")
    app.getOptionBox("Тип графика")


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
    # *getXY() will unpack the two return values
    # and pass them as separate parameters
    app.updatePlot("p1", *getXY())
    showLabels()


def showLabels():
    axes.legend(['The curve'])
    axes.set_xlabel("X Axes")
    axes.set_ylabel("Y Axes")
    app.refreshPlot("p1")


def press(button):
    if button == 'Подключиться к БД':
        connectToDb()
        app.hideSubWindow('Настройки подключения к БД')
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
            a,b = getXY()
            app.setPieChart(title="Pie", name="0", value=99)
            app.setPieChart(title="Pie", name="b", value=1)
            app.showSubWindow("График Pie")
    elif button == 'Выход':
        app.stop()
    elif button == 'Выход из настроек':
        app.hideSubWindow('Настройки подключения к БД')
    elif button == 'SETTINGS':
        app.showSubWindow('Настройки подключения к БД')
    elif button == "Зактрыть график":
        app.hideSubWindow("График")
    elif button == "Закрыть график Pie":
        app.hideSubWindow("График Pie")


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
app.addButtons(['Выход', 'Создать График'], press)
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

# Окно Графика тип Pie
app.startSubWindow("График Pie", "График Pie")

app.addPieChart("Pie", {"0": 50})
# Кнопки
app.addButtons(["Закрыть график Pie"], press)

# Устанавливает размер окна
app.stopSubWindow()
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
