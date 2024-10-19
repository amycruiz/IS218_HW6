'''Tests for the commands in the App'''
import pytest
from app import App
# from app.plugins.greet import GreetCommand
# from app.plugins.menu import MenuCommand
# from app.plugins.add import AddCommand
# from app.plugins.subtract import SubtractCommand
# from app.plugins.multiply import MultiplyCommand
# from app.plugins.divide import DivideCommand

def test_app_greet_command(capfd, monkeypatch):
    '''Greet command test'''
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0, "The app did not exit as expected"

def test_app_menu_command(capfd, monkeypatch):
    '''Menu command test'''
    inputs = iter(['menu', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0, "The app did not exit as expected"

def test_app_add_command(capfd, monkeypatch):
    '''Add command test'''
    inputs = iter(['add 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0, "The app did not exit as expected"

def test_app_subtract_command(capfd, monkeypatch):
    '''Subtract command test'''
    inputs = iter(['subtract 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0, "The app did not exit as expected"

def test_app_multiply_command(capfd, monkeypatch):
    '''Multiply command test'''
    inputs = iter(['multiply 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0, "The app did not exit as expected"

def test_app_divide_command(capfd, monkeypatch):
    '''Divide command test'''
    inputs = iter(['divide 10 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0, "The app did not exit as expected"
