from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}
    
    def register_command(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, *args):
        try:
            self.commands[command_name].execute(*args)
        except KeyError:
            print(f"Command '{command_name}' not found.")
    
    def get_avaliable_commands(self):
        return list(self.commands.keys())
