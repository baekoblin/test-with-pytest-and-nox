#!/bin/bash

# Install all required plugins
pip install pytest-html pytest-benchmark pytest-rerunfailures pytest-randomly pytest-cov pytest-xdist pytest-env

# Run tests with HTML report
pytest --html=report.html --self-contained-html

# Run tests with benchmarking
pytest --benchmark-enable

# Run tests with reruns
pytest --reruns 3

# Run tests prioritizing failed tests
pytest --failed-first

# Run tests with specific random seed
pytest --randomly-seed=42

# Run tests and measure code coverage
pytest --cov=my_project

# Run tests in parallel with 4 workers
pytest -n 4

# Run tests and restart from last failed tests
pytest --lf

# Run tests with environment variable set
pytest
