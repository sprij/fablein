"""
Module containing all task related functionality
"""

from fabric.api import local, cd
from fabric.tasks import Task


class RunnerTask(Task):
    """
    Task to expose runner of a part of the project life-cycle.
    """
    def __init__(self, config,  *args, **kwargs):
        """
        Task for runner.
        :param config: Task configuration
        """
        super(RunnerTask, self).__init__(*args, **kwargs)
        self.config = config
        self.__doc__ = config.description

    def run(self, *args):
        """
        Lein task runner.
        :param args: additional arguments for the command
        """
        user_args = ' '.join(args)
        with cd(self.config.folder):
            for command in self.config.commands:
                local('{0} {1}'.format(command, user_args))


class HelpTask(Task):
    """
    Displays detailed help for lein tasks.
    """
    def __init__(self, config,  *args, **kwargs):
        """
        Task for runner.
        """
        super(HelpTask, self).__init__(*args, **kwargs)
        self.config = config

    def run(self):
        """
        Lein task helper.
        :param runner: runner name
        :param args: additional arguments for the command
        """
        for task_name, task_config in self.config.iteritems():
            print 'lein.{0}\t{1}'.format(task_name, task_config.description)
