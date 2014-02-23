"""
Tests for HelpTask
"""
import unittest
import sys
from lein.task import HelpTask

from mock import Mock
from StringIO import StringIO


class HelpTaskTest(unittest.TestCase):
    def setUp(self):
        self.held, sys.stdout = sys.stdout, StringIO()

    def test_run_no_tasks(self):
        task = HelpTask({})
        task.run()
        self.assertEqual(sys.stdout.getvalue().strip(), '')

    def test_run_one_task(self):
        task_config = type('object', (object,),
                           {'description': 'description1'})
        config = {'task1': task_config}

        task = HelpTask(config)
        task.run()
        self.assertEqual(sys.stdout.getvalue().strip(),
                         'lein.task1\tdescription1')

    def test_run_multi_task(self):
        task1_config = type('object', (object,),
                            {'description': 'description1'})
        task2_config = type('object', (object,),
                            {'description': 'description2'})
        config = Mock()
        config.iteritems = Mock(return_value=iter([('task1', task1_config),
                                                   ('task2', task2_config)]))

        task = HelpTask(config)
        task.run()
        self.assertEqual(
            sys.stdout.getvalue(),
            'lein.task1\tdescription1\nlein.task2\tdescription2\n')
