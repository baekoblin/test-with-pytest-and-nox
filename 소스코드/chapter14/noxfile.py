
import nox



@nox.session
def tests(session):
    session.install('pytest')
    session.run('pytest')


@nox.session
def lint(session):
    session.install('flake8')
    session.run('flake8', "")


import nox

@nox.session
def install_requests(session):
    session.install('requests')
    session.run('python', '-c', 'import requests; print(requests.__version__)')



@nox.session(python=['3.7', '3.8', '3.9'])
def tests2(session):
    session.install('pytest')
    session.run('pytest')