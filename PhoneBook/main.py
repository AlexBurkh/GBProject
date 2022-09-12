
from View import UserInterface
from Controller import Controller
import contact_book 

class Program:
    _Book = contact_book.contact_book()
    _ConPrint = UserInterface()
    _Control = Controller(_Book, _ConPrint)

    def Run(self):
        Do = True
        
        #data = self._Control.StartLoad()
        self._Book.import_contact_list(self._Control.StartLoad())

        while Do:
            self._ConPrint.Print_Menu()
            Do = self.Do_Commands(self._ConPrint.Read_Line())

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
            self._Book.import_contact_list(self._Control.Load_Data())
        elif id_command == '7':
            self._Control.Save_Data(self._Book.get_sorted())

        return True


pro =  Program()
pro.Run()