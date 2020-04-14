from appJar import gui
import postgresql

def down(btn):
    global table_names, column_nmaes
    db = 'pq://' + 'postgres' + ':' + '1234' + '@' + 'localhost' + ':' + '5432' + '/' + 'postgres'
    conDb = postgresql.open(db)
    table_list = conDb.prepare("SELECT tablename FROM pg_catalog.pg_tables WHERE schemaname = 'public'")
    mes = ''
    list = []
    table_names = []
    for table_name in table_list:
        if type(table_name) is not type(None):
            mes = str(table_name)
            mes1 = mes.replace('(', '')
            mes2 = mes1.replace(')', '')
            mes3 = mes2.replace('\'', '')
            mes4 = mes3[:-1]
            column_list = 'SELECT' + ' ' + 'column_name FROM postgres.information_schema.columns where table_name=' + '\'' + str(mes4) + '\''
            column_list = conDb.prepare(column_list)
            bes = ''
            for i in column_list:
                bes += str(i)
                bes1 = bes.replace('(', '')
                bes2 = bes1.replace(')', '')
                bes3 = bes2.replace('\'', '')
                bes4 = bes3[:-1]
        list.append(bes4)
        table_names.append(mes4)
        print(table_names)
    column_names = []
    for i in list:
        if i.count(',') > 0:
            i = i.split(',')
            for x in i:
                column_names.append(x)
        else:
            column_names.append(i)
    if btn == 'down':
        app.changeOptionBox('column_names', column_names)


def sel():
    column_names = app.getOptionBox('column_names')
    for table_name in table_list:
        for column_name in dict:
            if column_name.values() == True:
                data = conDb.prepare('SELECT' + column_name + ' ' + 'FROM' + str(table_name))
#
# def show():
#     column_list = app.changeOptionBox('table_names', column_list)
#     a1 = 'select' + ' ' + str(app.getOptionBox('Поле таблицы оси X')) + ' ' + 'from' + ' ' + str(
#         app.getOptionBox('Таблица Оси X'))
#     table1Info = conDb.prepare(a1)


def push(btn):
    if btn == 'down':
        app.showSubWindow('choice')
        down(btn)
    elif btn == 'sel':
        sel()


app = gui()

app.addButton('down', push)
app.addButton('sel', push)

app.startSubWindow('choice', 'choice')
app.addTickOptionBox('column_names', ['lsdk'])
app.stopSubWindow()

app.go()