try:
    # def append(file,mod,name,phone):
    #     data = open(file,mod)
    #     data.writelines(name+", "+phone)
    #     data.close()
    # fin = "filePhones.txt" 

    fin = "Phones.txt"
    # класс для работы с файлом
    class File:
        def __init__(self,file, mod):
            self.file = file
            self.mod = mod
        def Open(self):
            self.data = open(self.file,self.mod)

        def Add(self,first,second,sur,phone):
            # self.data = open(self.file, self.mod)
            self.data.write(f"{first},{second},{sur},{phone}\n")

        def Close(self):
            self.data.close()

        def Read(self):
            return self.data.read()
        def ReadLine(self):
            return self.data.readline()
except:
    print("В модуле data, появилась проблема!")




    
