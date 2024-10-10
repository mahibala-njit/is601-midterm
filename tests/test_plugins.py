"""Unit tests for the PluginLoader class in the calculator.plugins module."""

from unittest.mock import MagicMock 
import pytest 
from calculator.commands import CommandHandler
from calculator.plugins import PluginLoader

# Mock command classes
class ValidCommand:
    """A valid command for testing purposes."""
    # No methods or properties; empty class

class InvalidCommand:
    """An invalid command for testing purposes."""
    # No methods or properties; empty class

@pytest.fixture
def command_handler():
    """Create a mock command handler."""
    return CommandHandler()

@pytest.fixture
def plugin_loader(command_handler):
    """Create a plugin loader with a mock command handler."""
    return PluginLoader(command_handler)

def test_load_invalid_plugins(plugin_loader, monkeypatch):
    """Test that invalid plugins are ignored."""
    # Mock the import to return the InvalidCommand
    monkeypatch.setattr('importlib.import_module', lambda x: MagicMock(**{'InvalidCommand': InvalidCommand}))
    
    # Attempt to load plugins
    plugin_loader.load_plugins()
    
    # Check that no invalid command is registered
    assert 'invalid_command' not in plugin_loader.command_handler.commands

def test_load_command_with_no_class(plugin_loader, monkeypatch):
    """Test that items that are not classes are ignored."""
    # Mock the import to return an object instead of a command class
    monkeypatch.setattr('importlib.import_module', lambda x: MagicMock(**{'NotACommand': 'string'}))
    
    # Attempt to load plugins
    plugin_loader.load_plugins()
    
    # Check that no non-class is registered
    assert 'not_a_command' not in plugin_loader.command_handler.commands
