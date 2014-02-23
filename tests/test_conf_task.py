"""
Tests for TaskConfig
"""
import unittest
from mock import patch

from lein.configuration import TaskConfig


class TaskConfigTest(unittest.TestCase):

    # static variable(s) with path location for patching
    getcwd_path = 'lein.configuration.os.getcwd'

    def test_init_without_dict(self):
        self.assertRaises(ValueError, TaskConfig, None)

    def test_getattr_commands_default(self):
        task_config = TaskConfig({})

        commands = getattr(task_config, TaskConfig.ATTR_COMMANDS)

        expected_commands = []
        self.assertEqual(expected_commands, commands)

    def test_getattr_commands_single_string(self):
        commands_config = 'ls'
        task_config = TaskConfig({TaskConfig.ATTR_COMMANDS: commands_config})

        commands = getattr(task_config, TaskConfig.ATTR_COMMANDS)

        expected_commands = [commands_config]
        self.assertEqual(expected_commands, commands)

    def test_getattr_commands_multiple_string(self):
        command_list = ['ls', 'pep8']
        task_config = TaskConfig({TaskConfig.ATTR_COMMANDS: command_list})

        commands = getattr(task_config, TaskConfig.ATTR_COMMANDS)

        expected_commands = command_list
        self.assertEqual(expected_commands, commands)

    def test_getattr_description_default(self):
        task_config = TaskConfig({})

        description = getattr(task_config, TaskConfig.ATTR_DESCRIPTION)

        expected_description = ''
        self.assertEqual(expected_description, description)

    def test_getattr_description_string(self):
        description_config = 'task that does stuff'
        task_config = TaskConfig({TaskConfig.ATTR_DESCRIPTION:
                                  description_config})

        description = getattr(task_config, TaskConfig.ATTR_DESCRIPTION)

        expected_description = description_config
        self.assertEqual(expected_description, description)

    @patch(getcwd_path)
    def test_getattr_folder_default(self, getcwd):
        cwd = '/home/test/'

        getcwd.return_value = cwd
        task_config = TaskConfig({})

        folder = getattr(task_config, TaskConfig.ATTR_FOLDER)

        expected_folder = cwd
        self.assertEqual(expected_folder, folder)
        self.assertTrue(getcwd.called)

    @patch(getcwd_path)
    def test_getattr_folder_default(self, getcwd):
        cwd = '/home/test/'
        folder_config = '/tmp/'

        getcwd.return_value = cwd
        task_config = TaskConfig({TaskConfig.ATTR_FOLDER: folder_config})

        folder = getattr(task_config, TaskConfig.ATTR_FOLDER)

        expected_folder = folder_config
        self.assertEqual(expected_folder, folder)
        self.assertTrue(getcwd.called)
