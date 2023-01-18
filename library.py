class File:
    def __init__(self,file, mod):
        self.file = file
        self.mod = mod
    def Open(self):
        self.data = open(self.file,self.mod)

    def AddFioPhone(self,fio,phone):
        # self.data = open(self.file, self.mod)
        self.data.writelines(fio+", "+phone+'\n')

    def Add(self,name):
        # self.data = open(self.file, self.mod)
        self.data.writelines(name)

    def Close(self):
        self.data.close()

    def Read(self):
        return self.data.read()
    def ReadLine(self):
        return self.data.readline()
class Client:
    def __init__(self, firstname, secondname, surname):
        self.Firstname = firstname
        self.Secondname = secondname
        self.Surname = surname
    def AddPhone(self, phone):
        self.Phone = phone


    
