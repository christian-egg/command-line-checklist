from pyfiglet import Figlet
from plumbum import cli
from plumbum.cmd import ls, cat
from questionary import prompt
import questionary

LIST_FILE_NAME = "list.txt"

def print_banner(text):
    print(Figlet(font='doom').renderText(text))

def get_file_text(file_name)
    return cat(file_name)

def get_list_items(list_text):
    if (len(list_text) == 0):
        return None
    
    list = list_text.strip()
    items = list.split("\n")
    
    return items

def create_menu_question(items):
    return questionary.rawselect(
        "Choose to edit an existing item or create a new one",
        choices=[{
            'name': item.strip()} for item in items, 
            "Add a new item",
            "Clear list",
            "Quit"
        ]
    )

def create_confirmation_question(message):
    return questionary.confirm(message, default=False)

class Checklist(cli.Application):
    VERSION = "1.0"
    

    def main(self):
        print_banner("CLI Checklist")
        items = get_list_items(list_text)
        if (items == None):


