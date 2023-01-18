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

class Client:
    def __init__(self):
        pass
    def __init__(self, firstname, secondname, surname):
        self.Firstname = firstname
        self.Secondname = secondname
        self.Surname = surname
    def AddFirstname(self, name):
        self.Firstname = name
    def AddSecondname(self, name):
        self.Secondname = name
    def AddSurname(self,name):
        self.Surname = name
    def AddPhone(self, phone):
        self.Phone = phone


    
