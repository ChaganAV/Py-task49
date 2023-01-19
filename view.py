import data as d
import controller as c

try:
    fin = d.fin

    def InputClient():
        print("==Телефонный справочник==") 
        c.SelectCommands()
        while True:
            res = int(input("Введите номер действия: \n> "))
            if res == 1: 
                c.DictPrint(fin)
            elif res == 2:
                name = input("Введите фамилию: ")
                c.FindFirstname(fin,name)
            elif res == 3:
                phone = input("Введите телефон: ")
                c.FindPhonePrint(fin,phone)
            elif res == 4:
                firstname = input("Введите фамилию: ")
                secondname = input("Введите имя: ")
                surname = input("Введите отчество: ")
                phone = input("Введите телефон: ")
                c.AppendRow(firstname=firstname,secondname=secondname,surname=surname,phone=phone)
            elif res == 5:
                phone = input("Для удаления записи, введите телефон: ")
                res = c.DeleteRow(fin,phone)
                if res>0:
                    print(f"Найдено {res} записей с телефоном: {phone}. Все удалены!")
                else:
                    print(f"Запись с телефоном: {phone} не найдена")
            elif res == 6:   
                phoneOld = input("Введите старый телефон: ")
                phoneNew = input("Введите новый телефон: ")
                count = c.UpdatePhone(fin,phoneOld,phoneNew)
                if count>0:
                    print(f"Изменили телефон: {phoneOld} на {phoneNew}")
                else:
                    print(f"К сожалению, телефон: {phoneOld} мы не нашли в телефонном справочнике!")
            elif res == 7:
                break
            else:
                c.SelectCommands()
except:
    print("В модуле view, появилась проблема!")