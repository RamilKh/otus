name: Run python test

on: [push]

jobs:
    tests:
        runs-on: ubuntu-latest
        steps:
            - uses: actions/checkout@v2

            - name: Setup python 3.8
            uses: actions/setup-python@v1
            with:
                python - version: 3.8

            - name: Lint with flake8
                run: |
                    pip install flake8
                    flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                    flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

            - name: Install dependencies
                run: |
                    pip install pipenv
                    pipenv install --ignore-pipfile --system

            - name: Run pytest
                run: pytest -s -vv