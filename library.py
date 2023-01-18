fin = "filePhones.txt"
# класс для работы с файлом
class File:
    def __init__(self,file, mod):
        self.file = file
        self.mod = mod
    def Open(self):
        self.data = open(self.file,self.mod)

    def Add(self,first,second,sur,phone):
        # self.data = open(self.file, self.mod)
        self.data.writelines(f"{first},{second},{sur},{phone}\n")

    def Close(self):
        self.data.close()

    def Read(self):
        return self.data.read()
    def ReadLine(self):
        return self.data.readline()

# класс записи справочника
class Client:
    def __init__(self):
        pass
    def __init__(self, firstname, secondname, surname, phone):
        self.Firstname = firstname
        self.Secondname = secondname
        self.Surname = surname
        self.Phone = phone

# вывод в список
def FileToList(file):
    file = File(file,'r')
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
def dictPrint(file):
    listFio = FileToList(file)

    count = 0
    for line in listFio:
        count = count + 1
        if count != 2:
            print(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}")
        else:
            print(line[0])
# поиск записи
def FindPhone(file,phone):
    listFio = FileToList(file)
    res = ""
    lineOut = []
    for line in listFio:
        res = list(filter(lambda ph: ph.strip() == phone,line))
        if len(res)>0:
            lineOut = line
    return lineOut

def FindFirstname(file,name):
    listFio = FileToList(file)
    res = ""
    lineOut = []
    for line in listFio:
        res = list(filter(lambda f: f.strip() == name, line))
        if len(res)>0:
            lineOut = line
    return lineOut
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

# добавление записи в справочник
def appendRow(firstname,secondname,surname,phone):
    client = Client(firstname,secondname,surname,phone)
    file = File(fin,'a')
    file.Open()
    file.Add(client.Firstname,client.Secondname,client.Surname,client.Phone)
    file.Close()

    
