import logging
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
        logging.info(f"Registered command: {command_name}")

    def execute_command(self, command_name: str, *args):
        try:
            logging.info(f"Executing command: {command_name} with arguments: {args}")
            self.commands[command_name].execute(*args)
        except KeyError:
            logging.error(f"Command '{command_name}' not found.")
            print(f"Command '{command_name}' not found.")
    
    def get_avaliable_commands(self):
        logging.info("Retrieving list of avaliable commands")
        return list(self.commands.keys())
