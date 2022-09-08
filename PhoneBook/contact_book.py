from contact import contact

class contact_book:
    _free_ids = []
    _next_id : int = 0
    _contacts = []

    def add_contact(self, name       : str, 
                          patronymic : str, 
                          surname    : str, 
                          number     : str):
        id = None
        if len(self._free_ids) != 0:
            id = self._free_ids[0]
            self._free_ids.remove(id)
        else:
            id = self._next_id
            self._next_id += 1
        self._contacts.append(contact(id, name, patronymic, surname, number))
        
    
    def get_by_id(self, id : int):
        for item in self._contacts:
            if item.id == id:
                return item

    def get_by_surname(self, surname : str):
        result = []
        for item in self._contacts:
            if item.surname == surname:
                result.append(item)
        return result

    def edit_contact(self, id         : int, 
                           name       : str = None, 
                           patronymic : str = None, 
                           surname    : str = None, 
                           number     : str = None):
        item = self.get_by_id(id)
        item.edit(name, patronymic, surname, number)

    def delete_contact(self, id : int):
        for item in self._contacts:
            if item.id == id:
                self._free_ids.append(item.id)
                self._contacts.remove(item)
    
    def get_sorted(self):
        return sorted([item for item in self._contacts], key = lambda row: (row.surname,
                                                                            row.name,
                                                                            row.patronymic))

    def get_unsorted(self):
        return self._contacts