"""
Tests for RunnerTask
"""

import unittest
from lein.task import RunnerTask
from mock import patch, call


class RunnerTaskTest(unittest.TestCase):

    # static variable(s) with path location for patching
    cd = 'lein.task.cd'
    local = 'lein.task.local'

    @patch(cd)
    @patch(local)
    def test_run_no_commands(self, local, cd):
        task_config = type('object', (object,),
                           {'description': 'description1',
                            'folder': 'src',
                            'commands': []})

        task = RunnerTask(task_config)
        task.run()

        cd.assert_called_with(task_config.folder)
        self.assertFalse(local.called)

    @patch(cd)
    @patch(local)
    def test_run_command(self, local, cd):
        task_config = type('object', (object,),
                           {'description': 'description1',
                            'folder': 'src',
                            'commands': ['ls']})

        task = RunnerTask(task_config)
        task.run()

        cd.assert_called_with(task_config.folder)
        local.assert_called_with('ls ')

    @patch(cd)
    @patch(local)
    def test_run_command_with_args(self, local, cd):
        task_config = type('object', (object,),
                           {'description': 'description1',
                            'folder': 'src',
                            'commands': ['ls']})

        task = RunnerTask(task_config)
        task.run('-l')

        cd.assert_called_with(task_config.folder)
        local.assert_called_with('ls -l')

    @patch(cd)
    @patch(local)
    def test_run_commands(self, local, cd):
        task_config = type('object', (object,),
                           {'description': 'description1',
                            'folder': 'src',
                            'commands': ['ls', 'ps']})

        task = RunnerTask(task_config)
        task.run()

        cd.assert_called_with(task_config.folder)
        self.assertEqual([call('ls '), call('ps ')], local.call_args_list)

    @patch(cd)
    @patch(local)
    def test_run_commands_with_args(self, local, cd):
        task_config = type('object', (object,),
                           {'description': 'description1',
                            'folder': 'src',
                            'commands': ['ls', 'ps']})

        task = RunnerTask(task_config)
        task.run('-l')

        cd.assert_called_with(task_config.folder)
        self.assertEqual([call('ls -l'), call('ps -l')], local.call_args_list)
