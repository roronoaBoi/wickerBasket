# Keep it clean!
This repository contains several fundamental examples for using Python. The repo is set up with pylint to ensure code is clean. Please use `pylint` prior to making contributions.

## Installing pylint
Install `pylint` by running the following command:
```bash
pip install pylint
```
OR
```bash
brew install pylint
```

For Debian-based distributions (Ubuntu), you can install `pylint` with the package manager:
```bash
sudo apt-get install pylint
```

## Running pylint
Prior to creating a pull request, run the following command locally to lint the code:
```bash
pylint <script>.py
```
Continue making changes until script is good quality.

## Disabling messages
The following is an example of a disable line that can be pasted into a script to bypass a message.
`# pylint: disable=invalid-name`
