This directory contains the files used to complet ethe 0x0A. Configuration management project on ALX.
# Configuration Management with Puppet

In this project, I used Puppet for configuration management. I worked on creating Puppet manifest files to perform tasks like creating a file, installing a package, and executing a command.

## Tasks:

### Task 0: Create a File
- [0-create_a_file.pp](./0-create_a_file.pp): This Puppet manifest file creates a file named `school` in the `/tmp` directory.
  - File permissions: `0744`.
  - File group: `www-data`.
  - File owner: `www-data`.
  - File content: `I love Puppet`.

### Task 1: Install a Package
- [1-install_a_package.pp](./1-install_a_package.pp): This Puppet manifest file installs the `flask` package from pip3.

### Task 2: Execute a Command
- [2-execute_a_command.pp](./2-execute_a_command.pp): This Puppet manifest file kills the process named `killmenow`.
