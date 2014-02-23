"""
Module containing all configuration functionality.

The supported schema for any lein configuraton file is as follows:

<task1>
  description: <description> (optional | default: '')
  command: <cmd1> (optional | default: [])
  folder: <folder> (optional | default: CWD)
<task2>
  description: <description>
  command:
    - <cmd1>
      <cmd2>
  folder: <folder>
"""

import os
import yaml
import inspect


class TaskConfig(object):
    ATTR_DESCRIPTION = 'description'
    ATTR_COMMANDS = 'commands'
    ATTR_FOLDER = 'folder'

    def __init__(self, config):
        """Representation of a task configuration.
        :param task_config: Default tasks
        :param project_config: Project specific tasks
        """
        if not isinstance(config, dict):
            raise ValueError('Task config should be instantiated with a dict.')

        self.config = config
        self.defaults = {self.ATTR_COMMANDS: [],
                         self.ATTR_DESCRIPTION: '',
                         self.ATTR_FOLDER: os.getcwd()}

    def __getattr__(self, item):
        """
        Gets attribute from config.
        :param item:
        """
        attr = self.config.get(item, self.defaults.get(item, None))
        if item == self.ATTR_COMMANDS and isinstance(attr, str):
            return [attr]

        return attr


class ConfigLoader(object):
    """
    Configuration load for Lein.
    """
    TASKS_CONFIG_FILE = 'tasks.yaml'
    PROJECT_CONFIG_FILE = '.lein.yaml'

    def get(self):
        """
        Get Lein Configuration by merging default tasks and project specific
        ones.
        """
        # loads default tasks
        current_file = inspect.getfile(inspect.currentframe())
        tasks_path = os.path.join(os.path.dirname(current_file),
                                  self.TASKS_CONFIG_FILE)
        task_config = ConfigLoader.load_yaml(tasks_path,
                                             error_on_missing=True)
        # loads project tasks
        project_path = os.path.join(os.getcwd(),
                                    self.PROJECT_CONFIG_FILE)
        project_config = ConfigLoader.load_yaml(project_path,
                                                error_on_missing=True)

        config = dict(task_config or {}, **project_config or {})

        return {k: TaskConfig(v) for k, v in config.iteritems()}

    @staticmethod
    def load_yaml(path, error_on_missing=False):
        """
        Load configuration from file
        :param path: path of the yaml file to load
        :param error_on_missing: if True raises error if the file isn't found
        """
        config = None

        if not os.path.isfile(path):
            if error_on_missing:
                raise RuntimeError('File "%s" is missing.' % path)
        else:
            with open(path, 'r') as f:
                config = yaml.safe_load(f)

        return config
