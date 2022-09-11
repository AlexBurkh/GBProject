
from View import UserInterface
from Controller import Controller
import contact_book 

class Program:
    Book = contact_book.contact_book()
    ConPrint = UserInterface()
    _Control = Controller(Book, ConPrint)

    def Run(self):
        Do = True
        self._Control.StartLoad()
        #self.StartLoad()

        while Do:
            self.ConPrint.Print_Menu()
            #UserInterface.PrintMenu()
            Do = self.Do_Commands(self.ConPrint.Read_Line())

    def Do_Commands(self, id_command):
        if id_command == '0':
            return False
        elif id_command == '1':
            self._Control.Add_User()
        elif id_command == '2':
            self._Control.Print_Book()
        elif id_command == '3':
            self._Control.Delite()
        elif id_command == '4':
            self._Control.Search(1)
        elif id_command == '5':
            self._Control.Search(2)
        elif id_command == '6':
            self._Control.Load_Data()
        elif id_command == '7':
            self._Control.Load_Save()

        return True


pro =  Program()
pro.Run()