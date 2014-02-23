#Fablein
--------------------
[![Build Status](https://travis-ci.org/sprij/fablein.png)](https://travis-ci.org/sprij/fablein)

#Overview
---
Fablein is a Leiningen-inspired project automation for python.

# Install
---
TODO

# Usage 
---
## Creating new projects 
TODO

## Tasks
TODO

## The project file
To include new tasks you'll need to add a **.lein.yaml** file at the root of your project.

**Schema**
```yaml
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
```

**Example**
```yaml
test:
  description: Run all tests.
  folder: tests
  commands: 
  - python -m unittest discover
```

## Help

All lein tasks will be shown with other fabric tasks:
```shell
fab -l
```
A task lein.help is always included to display the lein tasks only:
```shell
fab lein.help
```
