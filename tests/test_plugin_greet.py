import pytest
from app import App

def test_app_greet_command(capfd, monkeypatch):
    '''Tests that the read, execute, print, and loop
    correctly handles the 'greet' command and outputs 'Hello, World!.'''
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert e.value.code == 0, "The app did not exit as expected"
    out, err = capfd.readouterr()

    assert "Hello, World!" in out, "The 'greet' command did not provide the expected output."
