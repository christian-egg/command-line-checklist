from pyfiglet import Figlet
from plumbum import cli
from plumbum.cmd import ls, cat
from questionary import prompt
import questionary
from checklist import get_list_items, get_file_text

def test_get_file_text():
    text = get_file_text("test_list_1.txt")
    assert text == "hello", "Retrieved text should be correct"

def test_get_file_text_file_doesnt_exist():
    text = get_file_text("fake_text_file.txt")

def test_get_file_text_file_is_empty():
    text = get_file_text("empty_test_list.txt")
    assert text == None, "Empty test file should return None"
    