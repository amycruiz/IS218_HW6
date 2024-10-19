'''Testing application commands'''
import pytest

from app import App

def test_app_get_environment_variable():
    '''Testing enviromental variables'''
    app = App()
    current_env = app.get_environment_variable('ENVIRONMENT')
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(capfd, monkeypatch):
    '''Testing that the read, execute, print, and 
    loop exits correctly with 'exit' command.'''
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.value.code == 0

def test_app_start_unknown_command(capfd, monkeypatch):
    '''Tests how the read, execute, print, and loop
    handles an unknown command before exiting'''
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit):
        app.start()
    captured = capfd.readouterr()
    assert "Command 'unknown_command' not found." in captured.out
