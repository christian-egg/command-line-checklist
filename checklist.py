from plumbum.cli.switches import switch
from pyfiglet import Figlet
from plumbum import cli
from plumbum import local
from questionary import prompt
import questionary

LIST_FILE_NAME = "list.txt"

def print_banner(text):
    print(Figlet(font='doom').renderText(text))

def get_file_text(file_name):
    cat = local["cat"]
    return cat(file_name)

def get_list_items(list_text):
    if (len(list_text) == 0):
        return []
    
    list = list_text.strip()
    items = list.split("\n")
    
    return items

def create_menu_question(items):
    default_options = ["Add a new item", "Clear list", "Quit"]
    all_options = default_options + items

    return [{
        'type': 'rawselect',
        'name': 'items',
        'message': 'Choose an option below (choosing an item will remove it)',
        'choices': [{'name': item.strip(), 'value': index} for index, item in enumerate(all_options)],
    }]

def create_confirmation_question(message):
    return questionary.confirm(message, default=False)

class Checklist(cli.Application):
    VERSION = "1.0"
    NUM_DEFAULT_OPTIONS = 2
    items = []

    def main(self):
        print_banner("CLI Checklist")
        list_text = get_file_text(LIST_FILE_NAME)
        Checklist.items = get_list_items(list_text)

        Checklist.home_menu()

    def home_menu():
        question = create_menu_question(Checklist.items)
        answer = prompt(question)
        print(answer.get('items'))

        if (answer.get('items') == 0):
            Checklist.add_item()
        elif (answer.get('items') == 1):
            Checklist.clear_list
        elif (answer.get('items') == 2):
            return
        elif (answer.get('items') > 2):
            Checklist.del_item(answer.get('items') - Checklist.NUM_DEFAULT_OPTIONS)

        

    def add_item():
        return 1

    def clear_list():
        return

    def del_item(index):
        return

if __name__ == "__main__":
    Checklist()