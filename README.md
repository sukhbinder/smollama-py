# smollama-py

[![PyPI](https://img.shields.io/pypi/v/smollama-py.svg)](https://pypi.org/project/smollama-py/)
[![Changelog](https://img.shields.io/github/v/release/sukhbinder/smollama-py?include_prereleases&label=changelog)](https://github.com/sukhbinder/smollama-py/releases)
[![Tests](https://github.com/sukhbinder/smollama-py/actions/workflows/test.yml/badge.svg)](https://github.com/sukhbinder/smollama-py/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/sukhbinder/smollama-py/blob/master/LICENSE)

A python app to serve smOllama

## Installation

Install this tool using `pip`:
```bash
pip install smollama-py
```
## Usage

For help, run:
```bash
smOllama-py --help
```
You can also use:
```bash
python -m smOllama-py --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd smollama-py
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
