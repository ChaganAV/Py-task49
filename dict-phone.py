import library as lib
# def append(file,mod,name,phone):
#     data = open(file,mod)
#     data.writelines(name+", "+phone)
#     data.close()
# fin = "filePhones.txt" 
fin = lib.fin

def inputClient():
    print("==Телефонный справочник==") 
    lib.selectCommands()
    while True:
        res = int(input("Введите номер действия: \n> "))
        if res == 1:
            
            lib.dictPrint(fin)
        elif res == 2:
            break
        elif res == 3:

            break
        elif res == 4:
            firstname = input("Введите фамилию: ")
            secondname = input("Введите имя: ")
            surname = input("Введите отчество: ")
            phone = input("Введите телефон: ")
            lib.appendRow(firstname=firstname,secondname=secondname,surname=surname,phone=phone)
        elif res == 5:
            break
        elif res == 6:
            break
        elif res == 7:
            break
        else:
            lib.selectCommands()

inputClient()
        


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



# lib.dictPrint(fin)
