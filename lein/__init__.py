"""
Automation tasks with Fabric.

$ fab lein new [TEMPLATE] NAME # generate a new project skeleton *

$ fab lein.test

$ fab lein.package

$ fab lein.style

* TO BE IMPLEMENTED
"""
from .task import RunnerTask, HelpTask
from .configuration import ConfigLoader

config_loader = ConfigLoader()
config = config_loader.get()
for task_name, task_config in config.iteritems():
    globals()[task_name] = RunnerTask(task_config)
globals()['help'] = HelpTask(config)
