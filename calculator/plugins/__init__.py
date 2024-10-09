# calculator/plugins/__init__.py

import pkgutil
import importlib
from calculator.commands import CommandHandler
from calculator.commands import Command

class PluginLoader:
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def load_plugins(self):
        # Dynamically load all plugins in the plugins directory
        plugins_package = 'calculator.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:  # Ensure it's a package
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command):  # Assuming a Command base class exists
                            self.command_handler.register_command(plugin_name, item)
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore


