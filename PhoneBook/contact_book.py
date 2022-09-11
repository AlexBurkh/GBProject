from contact import contact

class contact_book:
    __next_id : int = 0
    __contacts = []

    def _current_max_id(self):
        max_id = 0
        for item in self.__contacts:
            if item.id > max_id:
                max_id = item.id
        return max_id

    def add_contact(self, name       : str, 
                          patronymic : str, 
                          surname    : str, 
                          number     : str):
        self.__contacts.append(contact(self.__next_id, name, patronymic, surname, number))
        self.__next_id += 1
    
    def _import_contact(self, id : str, 
                             name : str, 
                             patronymic : str, 
                             surname : str, 
                             number : str):
        self.__contacts.append(contact(id, name, patronymic, surname, number))
        self.__next_id = id + 1

    def import_contact_list(self, contact_list):
        self.__contacts = []
        self.__next_id = 0
        for contact in contact_list:
            self._import_contact(contact.id, contact.name, contact.patronymic, contact.surname, contact.number)
    
    def get_by_id(self, id : int):
        result = []
        for item in self.__contacts:
            if item.id == id:
                result.append(item)
        return result

    def get_by_surname(self, surname : str):
        result = []
        for item in self.__contacts:
            if item.surname == surname:
                result.append(item)
        return result

    def edit_contact(self, id         : int, 
                           name       : str = None, 
                           patronymic : str = None, 
                           surname    : str = None, 
                           number     : str = None):
        item = self.get_by_id(id)[0]
        item.edit(name, patronymic, surname, number)

    def delete_contact(self, id : int):
        flag = False
        for item in self.__contacts:
            if item.id == id:
                self.__contacts.remove(item)
                flag = True
        for item in self.__contacts[id:]:
            item.id -= 1
        if len(self.__contacts) != 0:
            self.__next_id = self._current_max_id() + 1
        else:
            self.__next_id = 0
        return flag
    
    def get_sorted(self):
        return sorted([item for item in self.__contacts], key = lambda row: (row.surname,
                                                                            row.name,
                                                                            row.patronymic))

    def get_unsorted(self):
        return self.__contacts