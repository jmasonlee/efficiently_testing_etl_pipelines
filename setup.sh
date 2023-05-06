#!/bin/bash
pyenv install 3.8
pyenv local 3.8
poetry env use python3.8
poetry install
poetry shell