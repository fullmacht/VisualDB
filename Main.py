from appJar import gui
from time import strftime, gmtime
import matplotlib.pyplot as plt


# Функция получения времени для Statusbar'a
def timeSt():
    t = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
    app.setStatusbar(t)


# Функция соединения с БД
def connectToDb():
    db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
        'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    global conDb
    try:
        pass
    except:
        pass
    else:
        app.infoBox('Результат', 'Покдключение к БД установлено')


# Функция извлечения данных из БД в графики
def showTableInfo():
    app.changeOptionBox('Список результатов')


def press(button):
    if button == 'Подключиться к БД':
        connectDb()
        app.hideSubWindow('Настройки подключения к БД')
    elif button == 'Очистить поля':
        app.clearEntry("Пользователь")
        app.clearEntry("Пароль")
    elif button == 'Создать График':
        selectTableInfo()
        app.showSubWindow("Графики")
    elif button == 'Выход':
        app.stop()
    elif button == 'Выход из настроек':
        app.hideSubWindow('Настройки подключения к БД')
    elif button == 'SETTINGS':
        app.showSubWindow('Настройки подключения к БД')


# Основное окно
app = gui('Project-X', 'Fullscreen')

# Выпадающее меню графиков
app.addLabelOptionBox("Типы графиков", options={1: "Pie"})

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

# Устанавливает курсор на строке ввода
app.setFocus('Пользователь')

# Устанавливает размер окна
app.setSize("Fullscreen")

app.stopSubWindow()

app.go()
