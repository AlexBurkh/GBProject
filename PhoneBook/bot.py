from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from Controller import Controller
from contact_book import contact_book
from View import UserInterface

class Bot():
    _Book = contact_book()
    _ConPrint = UserInterface()
    _Control = Controller(_Book, _ConPrint)

    __token = ""

    def __init__(self, token):
        self.__token = token

    def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._Book.import_contact_list(self._Control.StartLoad())
        self.menu(update, context)

    def menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._ConPrint.Print_Menu()

    def add_contact(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._Control.Add_User()

    def print_book(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._Control.Print_Book()

    def delete_contact(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._Control.Delete()

    def search_by_id(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._Control.Search(1)

    def search_by_surname(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._Control.Search(2)

    def import_contacts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._Book.import_contact_list(self._Control.Load_Data())

    def export_contacts(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        self._Control.Save_Data(self._Book.get_sorted())

    def run(self):
        app = ApplicationBuilder().token(self.__token).build()
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CommandHandler("menu", self.menu))
        app.add_handler(CommandHandler("add_contact", self.add_contact))
        app.add_handler(CommandHandler("print_book", self.print_book))
        app.add_handler(CommandHandler("delete_contact", self.delete_contact))
        app.add_handler(CommandHandler("search_by_id", self.search_by_id))
        app.add_handler(CommandHandler("import_contacts", self.import_contacts))
        app.add_handler(CommandHandler("export_contacts", self.export_contacts))
        app.run_polling()