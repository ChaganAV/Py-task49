import library as lib
# def append(file,mod,name,phone):
#     data = open(file,mod)
#     data.writelines(name+", "+phone)
#     data.close()


fin = "fileIn.txt" 
file = lib.File(fin,'w')
# file.Open()
# file.Add("ФИО,       телефон\n")
# file.Add('-----------------------------------\n')
# file.Close()

# file = lib.File(fin, 'a')
# file.Open()
# file.AddFioPhone("Петров Иван Иванович","8987456123")
# file.AddFioPhone("Сидоров Иннокентий Петровчи","8927456789")
# file.Close()

file = lib.File(fin,'r')
file.Open()
dictFio = []
while True:
    line = file.ReadLine()
    if not line:
        break
    else:
        dictFio.append(line.split(','))
file.Close()
for line in dictFio:
    print(line[0])