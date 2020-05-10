import socket
import postgresql
import matplotlib.pyplot as plt
from PIL import Image
import imghdr
from email.message import EmailMessage
from appJar import gui
import smtplib
from datetime import tzinfo, timedelta, datetime, timezone


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
    t = datetime.now(UTC025()).strftime('%a, %d %b %Y %H:%M:%S')
    app.setStatusbar(t)


# def connect_to_db():
def connect_to_db():
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
    db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
    con_db = postgresql.open(db)
    return con_db


def download_table_names_list():
    con_db = connect_to_db()
    table_list = con_db.prepare("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public'")
    table_names_list = []
    for table_name in table_list:
        if type(table_name) is not type(None):
            mes = str(table_name)
            mes1 = mes.replace('(', '')
            mes2 = mes1.replace(')', '')
            mes3 = mes2.replace('\'', '')
            mes4 = mes3[:-1]
        table_names_list.append(mes4)
        table_names_list.sort()
    return table_names_list


def download_column_names_list(btn):
    con_db = connect_to_db()
    table_names_list = download_table_names_list()
    list_for_optionbox = []
    for table_name in table_names_list:
        column_list = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + str(table_name) + '\''
        column_list = con_db.prepare(column_list)
        bes = ''
        for i in column_list:
            if type(i) is not type(None):
                bes += str(i)
                bes1 = bes.replace('(', '')
                bes2 = bes1.replace(')', '')
                bes3 = bes2.replace('\'', '')
                bes4 = bes3[:-1]
                bes5 = '{} | {}'.format(bes4,table_name)
                list_for_optionbox.append(bes5)
    column_names_list = []
    for i in list_for_optionbox:
        if i.count(',') > 0:
            i = i.split(',')
            column_names_list.append(i[-1])
        else:
            column_names_list.append(i)
    if btn == 'start':
        app.changeOptionBox('Список колонн X', column_names_list)
        app.changeOptionBox('Список колонн Y', column_names_list)
        app.changeOptionBox('Список колонн Z', column_names_list)
    elif btn == 'Выбрать данные для графика X':
        app.changeOptionBox('Список колонн X', column_names_list)
    elif btn == 'Выбрать данные для графика Y':
        app.changeOptionBox('Список колонн Y', column_names_list)
    elif btn == 'Выбрать данные для графика Z':
        app.changeOptionBox('Список колонн Z', column_names_list)
    elif btn == 'Показать данные':
        app.changeOptionBox('Список колонн', column_names_list)
    elif btn == 'Окно ввода данных':
        app.changeOptionBox('Список колонн для ввода', column_names_list)




def download_column_names_info(option_box):
    con_db = connect_to_db()
    column_names = app.getOptionBox(option_box)
    true_column_list = []
    for key,value in column_names.items():
        if value == True:
            true_column_list.append(key)
    list_for_download = []
    for i in true_column_list:
        i = i.split(' | ')
        list_for_download.append(i)
    info_for_graf = {}
    for name in list_for_download:
        list_name = name[0]
        table_name = name[1]
        sql_code = 'select' + ' ' + list_name + ' ' + 'from' + ' ' + table_name
        info = con_db.prepare(sql_code)
        nes = ''
        for i in info:
            # Добавить счётчик количества строк в колонне
            # добавить чтобы None заменялся на 0
            nes = nes + str(i)
            nes1 = nes.replace('(', '')
            nes2 = nes1.replace(')', '')
            nes3 = nes2.replace('\'', '')
            nes4 = nes3.replace('Decimal', '')
            nes5 = nes4[:-1]
            nes6 = nes5.split(',')
            numbers = []
            for n in nes6:
                if n != 'None':
                    #добавить чтобы None заменялся на 0
                   nes7 = int(n)
                   numbers.append(nes7)
        graf_name =  '{} | {}'.format(list_name,table_name)
        info_for_graf[graf_name]=numbers
    return info_for_graf


def pie_plot(option_box_x):
    info = download_column_names_info(option_box=option_box_x)
    value_list = []
    name_list = []
    for name, value in info.items():
        value = sum(value)
        value_list.append(value)
        name_list.append(name)
    plt.subplots()
    plt.pie(value_list, explode=None, labels=name_list, autopct='%1.1f%%',
                shadow=True, startangle=90)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(app.getOptionBox('Тип графика'))
    plt.legend()
    plt.savefig(app.getOptionBox('Тип графика') + '.png')
    im = Image.open(app.getOptionBox('Тип графика') + '.png')
    im.save(app.getOptionBox('Тип графика') + '.ppm')
    app.reloadImage("grafik", app.getOptionBox('Тип графика') + '.ppm')


def plot(option_box_x, option_box_y):
    info_x = download_column_names_info(option_box=option_box_x)
    info_y= download_column_names_info(option_box=option_box_y)
    # x = [1,2,3,4,5,6,7]
    l = []
    for name_x,value_x in info_x.items():
        for name_y,value_y in info_y.items():
            a = plt.plot(value_x, value_y,label=name_y)
            plt.xlabel(name_x)
            plt.title('Histogram of IQ')
            plt.grid(True)
            plt.legend()
            l.append(a)
    plt.savefig(app.getOptionBox('Тип графика') + '.png')
    im = Image.open(app.getOptionBox('Тип графика') + '.png')
    im.save(app.getOptionBox('Тип графика') + '.ppm')
    app.reloadImage("grafik", app.getOptionBox('Тип графика') + '.ppm')


def send(f_name):
    msg = EmailMessage()
    msg['Subject'] = app.getEntry('Тема письма')
    msg['From'] = app.getEntry('От кого')
    msg['To'] = app.getEntry('Кому')
    msg.get_filename()
    try:
        msg.set_content(app.getTextArea('сообщение'))
        with open(f_name, 'rb') as fp:
            img_data = fp.read()
            msg.add_attachment(img_data, maintype='image', subtype=imghdr.what(None, img_data),filename=f_name)
            server_address = app.getEntry('От кого')
            server_address = server_address.split('@')[1]
        with smtplib.SMTP(host='smtp.{}'.format(server_address), port=587) as s:
            s.starttls()
            s.login(user=app.getEntry('От кого'), password=app.getEntry('Пароль от почты'))
            s.send_message(msg)
    except smtplib.SMTPAuthenticationError:
        app.infoBox('Ошибка!', 'Пароль не подходит! Возможно Вам необходимо создать пароль для этого приложения на Вашей электронной почте.')
    except socket.gaierror:
        app.infoBox('Ошибка!', 'Неправильно написана почта отправителя или программа не поддерживает отправку с Вашей почты!')
    except FileNotFoundError:
        app.infoBox('Ошибка!', 'Не найден файл графика!')
    except IndexError:
        app.infoBox('Ошибка!', 'Вы не ввели данные отправителя!')


def clear_plot():
    plt.cla()
    plt.clf()
    plt.close()

def clear_message_window():
    app.clearTextArea('сообщение')
    app.clearEntry('Тема письма')
    app.clearEntry('От кого')
    app.clearEntry('Кому')
    app.clearEntry('Пароль от почты')

def insertInfo():
    db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
    # db = 'pq://' + app.getEntry('Имя пользователя') + ':' + app.getEntry('Пароль') + '@' + app.getEntry(
    #     'IP') + ':' + app.getEntry('Port') + '/' + app.getEntry('Название БД')
    conDb = postgresql.open(db)
    d4 = str(app.getOptionBox('Таблица для ввода'))
    e5 = str(app.getOptionBox('Столбец для ввода'))
    f6 = str(app.getEntry('Данные'))
    a1 = 'INSERT INTO' + ' ' + d4 + '(' + e5 + ')' + ' ' + 'VALUES' + ' ' + '(' + f6 + ')'
    conDb.execute(a1)


def clear_DB_settings_window():
    app.clearEntry('Имя пользователя')
    app.clearEntry('Пароль')
    app.clearEntry('IP')
    app.clearEntry('Port')
    app.clearEntry('Название БД')
    app.setFocus('Имя пользователя')


def select_table_info(option_box_text_area):
    info = download_column_names_info(option_box=option_box_text_area)
    for name,value in info.items():
        message = str(app.getOptionBox(option_box_text_area)) + ':' + '\n' + '\n' + value
    app.setTextArea('Показать данные', message)


def push(btn):
    if btn == 'Выбрать данные для графика X':
        app.showSubWindow('choice')
        download_column_names_list(btn)
    elif btn == 'Выбрать данные для графика Y':
        app.showSubWindow('choice')
        download_column_names_list(btn)
    elif btn == 'Выбрать данные для графика Z':
        app.showSubWindow('choice')
        download_column_names_list(btn)
    elif btn == 'Построить график':
        if app.getOptionBox('Тип графика') == "Plot":
            try:
                plot(option_box_x='Список колонн X',option_box_y='Список колонн Y')
                app.showSubWindow('grafik')
            except ValueError:
                app.infoBox('Ошибка!', 'Размерность данных для графика не совпадает!')
        elif app.getOptionBox('Тип графика') == 'Pie':
            pie_plot(option_box_x='Список колонн X')
            app.showSubWindow('grafik')
    elif btn == 'close':
        clear_plot()
        app.hideSubWindow('grafik')
    elif btn == 'close window send':
        clear_message_window()
        app.hideSubWindow('Send')
    elif btn == 'send':
        app.showSubWindow('Send')
    elif btn == 'uploud':
        send(f_name= app.getOptionBox('Тип графика') + '.png')
    elif btn == 'SETTINGS':
        app.showSubWindow('Настройки подключения к БД')
    elif btn == 'Подключиться к БД':
        connect_to_db()
        clear_DB_settings_window()
        app.hideSubWindow('Настройки подключения к БД')
    elif btn == 'Выход из настроек':
        app.hideSubWindow('Настройки подключения к БД')
    # elif btn == 'Очистить поля':
    #     clear_DB_settings_window()
    elif btn == 'Выход':
        app.stop()
    elif btn == 'Вывод данных':
        select_table_info(option_box_text_area='Список колонн')
    elif btn == 'Показать данные':
        download_column_names_list(btn)
        app.showSubWindow(btn)
    elif btn == 'Очистить окно':
        app.clearTextArea('Показать данные')
    elif btn == 'Закрыть':
        app.clearTextArea('Показать данные')
        app.hideSubWindow('Показать данные')
    elif btn == 'Ввести данные':
        insertInfo()
    elif btn == 'Окно ввода данных':
        download_column_names_list(btn)
        app.showSubWindow(btn)
    elif btn == 'Зактрыть окно':
        app.clearEntry('Данные')
        app.hideSubWindow('Окно ввода данных')




left = 25
def percentComplete():
    global left
    left += 25
    return left


def updateMeter():
    app.setMeter('Загрузка', percentComplete())

# app = gui('Программа', )
# Основное окно
app = gui('VisualDB',useTtk=True)
app.setTtkTheme("elegance")

# Временное окно входа в программу
# app.showSplash('VisualDB', fill='blue', stripe='black', fg='white', font=44)
app.addMeter('Загрузка')
app.setMeterFill('Загрузка', 'green')
app.registerEvent(updateMeter)

app.addStatusbar()
app.registerEvent(timeSt)

app.addTickOptionBox('Список колонн X', ['Данные не загрузились'])
app.addTickOptionBox('Список колонн Y', ['Данные не загрузились'])
app.addTickOptionBox('Список колонн Z', ['Данные не загрузились'])

app.addLabelOptionBox('Тип графика', ['Plot','Pie','3D' ])

download_column_names_list(btn='start')

app.addButtons(['Построить график','Показать данные', 'Окно ввода данных', 'Выход',], push)
# app.addButton('Выбрать данные для графика', push)

app.setButtonTooltip('Построить график',"Создайте график в отдельном окне")
app.setButtonTooltip('Показать данные',"Посмотрите данные из таблицы в этом окне")
app.setButtonTooltip('Окно ввода данных',"Дополните таблицу информацией")
app.setButtonTooltip('Выход',"Выйти из программы")

app.setOptionBoxTooltip('Тип графика',
                        "Нажмите, чтобы выбрать подходящий график. Для графика 'Pie' выберите таблицы 2 и 3. Они будут использоваться для построения графика 'Pie'")
app.addToolbarButton('SETTINGS', push, findIcon=True)

app.startSubWindow('grafik')
# app.setSize('Fullscreen')
app.addImage("grafik", "test.ppm")

app.addButtons(['close','send'],push)

app.setButtonTooltip('close', 'Закрыть окно с графиком')
app.setButtonTooltip('send', 'Отправить график по Email')

app.stopSubWindow()

# app.startSubWindow('choice', 'choice')
# # app.setSize('Fullscreen')
# app.addTickOptionBox('Список колонн', ['Данные не загрузились'])
# app.addButton('Построить график', push)
# app.stopSubWindow()

# Окно отправки графика
app.startSubWindow('Send')
# app.setSize('Fullscreen')
app.addLabel('l1', 'Отправка на Gmail, Yandex и Mail почты')
app.addLabelEntry('Тема письма')
app.addLabelEntry('От кого')
app.addLabelEntry('Кому')
app.addLabelEntry('Пароль от почты')
app.addLabel('l2', 'Текст сообщения')
app.addTextArea('сообщение')
app.addButtons(['uploud','close window send'],push)
app.stopSubWindow()

# Окно настройки подключения к БД
app.startSubWindow('Настройки подключения к БД', 'Настройки подключения к БД', modal=False, blocking=False,
                   transient=True,
                   grouped=True)
# Кнопки
app.addButtons(['Подключиться к БД', 'Очистить поля', 'Выход из настроек', ], push)
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

# Окно показа данных
app.startSubWindow('Показать данные', 'Показать данные', modal=False, blocking=False, transient=True, )
# app.setSize('Fullscreen')
app.addButtons(['Вывод данных'], push)
app.setFont(20)
app.addLabelOptionBox('Список колонн', 'Данные не загрузились')
# app.addLabelOptionBox('Столбец', mess)
app.addTextArea(title='Показать данные', text='Здесь появятся данные')
app.addButtons(['Очистить окно', 'Закрыть'], push)
#app.exitFullscreen()
app.stopSubWindow()

# Окно ввода данных
app.startSubWindow('Окно ввода данных', 'Окно ввода данных')
# app.setSize('Fullscreen')
app.addLabelEntry('Данные')
app.setEntryDefault('Данные', 'Введите данные')
app.setFocus('Данные')
app.addButtons(['Ввести данные', 'Зактрыть окно'], push)
app.addLabelOptionBox('Список колонн для ввода', 'Данные не загрузились')
# app.addLabelOptionBox('Столбец для ввода', mess)
#app.exitFullscreen()
app.stopSubWindow()

app.go()





















