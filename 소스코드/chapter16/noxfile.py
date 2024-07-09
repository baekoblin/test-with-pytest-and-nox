import nox
import subprocess
import os

def install_python_version(version):
    """Install Python version using pyenv if not already installed."""
    result = subprocess.run(["pyenv", "versions", "--bare"], capture_output=True, text=True)
    installed_versions = result.stdout.split()
    if version not in installed_versions:
        subprocess.run(["pyenv", "install", version])

@nox.session
def bootstrap(session):
    """Bootstrap Python versions using pyenv."""
    versions = ["3.7.9", "3.8.6", "3.9.1"]
    for version in versions:
        install_python_version(version)

@nox.session(python=["3.7.9", "3.8.6", "3.9.1"])
def tests(session):
    session.install('pytest')
    session.run('pytest')

@nox.session
def lint(session):
    session.install('flake8')
    session.run('flake8', 'my_project')

@nox.session
def docs(session):
    session.install('sphinx')
    session.run('sphinx-build', 'docs', 'docs/_build')
