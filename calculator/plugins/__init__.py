import pkgutil
import importlib
import logging
from calculator.commands import CommandHandler
from calculator.commands import Command

# Set up logging for this module
logger = logging.getLogger(__name__)

class PluginLoader:
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler

    def load_plugins(self):
        """Dynamically load all plugins in the plugins directory."""
        plugins_package = 'calculator.plugins'
        logger.info("Loading plugins from package: %s", plugins_package)

        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg: 
                logger.debug("Loading plugin: %s", plugin_name)
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, Command): 
                            self.command_handler.register_command(plugin_name, item)
                            logger.info("Registered command: %s", plugin_name)
                    except TypeError:
                        logger.warning("Ignored item: %s (not a subclass of Command)", item_name)
                        continue  # If item is not a class or unrelated class, just ignore

        logger.info("Finished loading plugins.")
