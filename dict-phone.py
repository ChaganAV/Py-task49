import library as lib
# def append(file,mod,name,phone):
#     data = open(file,mod)
#     data.writelines(name+", "+phone)
#     data.close()
# fin = "filePhones.txt" 
fin = lib.fin

def InputClient():
    print("==Телефонный справочник==") 
    lib.SelectCommands()
    while True:
        res = int(input("Введите номер действия: \n> "))
        if res == 1: 
            lib.dictPrint(fin)
        elif res == 2:
            name = input("Введите фамилию: ")
            lib.FindFirstname(fin,name)
        elif res == 3:
            phone = input("Введите телефон: ")
            lib.FindPhone(fin,phone)
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
            lib.SelectCommands()

InputClient()
        
