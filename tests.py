from pyfiglet import Figlet
from plumbum import cli
from plumbum.cmd import ls, cat
from questionary import prompt
import questionary
from checklist import get_list_items, get_file_text
import pytest

# Tests for get_file_text()

def test_get_file_text():
    text = get_file_text("test_list_1.txt")
    assert text == "hello", "Retrieved text should be correct"

def test_get_file_text_file_doesnt_exist():
    """Test that exception is raised when file does not exist"""
    with pytest.raises(Exception):
        get_file_text("fake_text_file.txt")

def test_get_file_text_file_is_empty():
    text = get_file_text("empty_test_list.txt")
    assert text == "", "Empty test file should return empty string"
    
# Tests for get_list_items()

def test_get_list_items():
    text = "Bread\nMeat\nCheese\nLettuce\nTomato "
    items = get_list_items(text)
    assert len(items) == 5, "List of items should have correct size"
    assert items[0] == "Bread", "Contents of list should be from the passed text"
    assert items[4] == "Tomato", "Trailing whitespace should be ignored"

def test_get_list_items_empty():
    text = ""
    assert get_list_items(text) == [], "Empty string returns empty list"