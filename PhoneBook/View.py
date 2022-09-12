
from email import message
from os import lseek
from Console import Console


class UserInterface:
    con = Console()

    def Print_Menu(self):

        self.con.Clear()
        self.con.WriteLine('\n\t\tТелефонная книга')
        self.con.WriteLine('======================================================')
        self.con.WriteLine('\n\tКоманды:\n\t    1 - Добавить\n\t    2 - Вывести на экран список\
        \n\t    3 - Удалить\n\t    4 - Поиск по id\n\t    5 - Поиск по фамилии\n\t    6 - Загрузить\n\t    7 - Сохранить\n\t    0 - Выход')
    
    def Print_Menu_Load_Save(self, index):
        massage = ''
        if index == 1:
            message = 'Загрузить'
        else:
            message = 'Сохранить'
        self.con.WriteLine('\n\t\tТелефонная книга')
        self.con.WriteLine('======================================================')
        self.con.WriteLine('\n\t 1 - {} с помощью json    \n\t 2 - {} с помощью html'.format(message, message))

    def Read_Line(self, line = '\n\tВведите номер команды: '):
        con = Console()
        return con.ReadLine(line)
    
    def Print_List_Book(self, lisrUsers):
        self.con.Clear()
        self.con.WriteLine('\n\t\t Список контактов: \n')
        self.con.WriteLine('===================================================================================')
        
        for User in lisrUsers:

            self.con.WriteLine('\tid: {} name: {} patronymic: {} surname: {} number: {}'.format(
                User.id, User.name, User.patronymic, User.surname, User.number))
        self.Read_Line('')
        
    def Print_In_Display(self, line:str):
        self.con.WriteLine(line)
