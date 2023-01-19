import data as d
import model as m

# вывод списка команд
def SelectCommands():
    commands = "Список команд:\n\
            1 - Показать все записи\n\
            2 - Найти запись по вхождению частей имени\n\
            3 - Найти запись по телефону\n\
            4 - Добавить новый контакт\n\
            5 - Удалить контакт\n\
            6 - Изменить номер телефона у контакта\n\
            7 - Выход\n\
            8 - Список команд\n"
    print(commands)

# вывод в список
def FileToList(file):
    file = d.File(file,'r')
    file.Open()
    listFio = []
    while True:
        line = file.ReadLine()
        if not line:
            break
        else:
            listFio.append(line.split(','))
    file.Close()
    return listFio

# вывод на печать
def DictPrint(file):
    listFio = FileToList(file)
    for line in listFio:
        if len(line[0])>1:
            print(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}")

# добавление записи в справочник
def AppendRow(firstname,secondname,surname,phone):
    client = m.Client(firstname,secondname,surname,phone)
    file = d.File(d.fin,'a')
    file.Open()
    file.Add(client.Firstname,client.Secondname,client.Surname,client.Phone)
    file.Close()

def AppendRows(clients,mod):
    file = d.File(d.fin,mod)
    file.Open()
    for client in clients:
        if len(client.Firstname.strip())>1:
            file.Add(client.Firstname,client.Secondname,client.Surname,client.Phone)
    file.Close()

# поиск записи
def FindPhonePrint(file,phone):
    line = FindPhone(file,phone)
    if len(line)>0:
        print(*line)
    else:
        print(f"Нет записи с телефоном: {phone}")

def FindPhone(file,phone):
    listFio = FileToList(file)
    res = ""
    lineOut = []
    for line in listFio:
        res = list(filter(lambda ph: ph.strip() == phone,line))
        if len(res)>0:
            lineOut = line
    return lineOut

# поиск по фамилии
def FindFirstname(file,name):
    listFio = FileToList(file)
    res = ""
    lineOut = []
    for line in listFio:
        res = list(filter(lambda f: f.strip() == name, line))
        if len(res)>0:
            lineOut.append(line)
            
    if len(lineOut)>0:
        for line in lineOut:
            print(*line)
    else:
        print(f"Нет такой фамилии: {name}")

# удаление контакта по номеру телефона
def DeleteRow(file,phone):
    listFio = FileToList(file)
    res = ""
    count = 0
    listClients = []
    for line in listFio:
        # if len(line)>1:
        #     print(f"'{line[3].strip()}' == '{phone.strip()}'")
        res = list(filter(lambda ph: ph.strip() == phone.strip(), line))

        if len(res)>0:
            count = count + 1
        else:
            if len(line)>1:
                client = m.Client(line[0],line[1],line[2],line[3])
                listClients.append(client)
    if count>0:
        AppendRows(listClients,'w')
    return count
    
