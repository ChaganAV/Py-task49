import library as lib
# def append(file,mod,name,phone):
#     data = open(file,mod)
#     data.writelines(name+", "+phone)
#     data.close()


fin = "fileIn.txt" 
# file = lib.File(fin,'w')
# file.Open()
# file.Add("ФИО,       телефон\n")
# file.Add('-----------------------------------\n')
# file.Close()

# file = lib.File(fin, 'a')
# file.Open()
# file.AddFioPhone("Петров Иван Иванович","8987456123")
# file.AddFioPhone("Сидоров Иннокентий Петровчи","8927456789")
# file.Close()
client = lib.Client("Васечкин", "Александр", "Петрович")
client.Phone = "+7945646321"
file = lib.File(fin,'a')
file.Open()
file.Add(client.Firstname,client.Secondname,client.Surname,client.Phone)
file.Close()

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

count = 0
for line in dictFio:
    count = count + 1
    if count != 2:
        print(f"{line[0]}, {line[1]}, {line[2]}, {line[3]}")
    else:
        print(line[0])