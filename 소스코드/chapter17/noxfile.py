import nox

@nox.session(python=['3.7', '3.8', '3.9'])
def tests(session):
    session.install('pytest')
    session.install('-r', 'requirements.txt')
    session.run('pytest')

@nox.session
def lint(session):
    session.install('flake8')
    session.run('flake8', 'my_project')

@nox.session(python=['3.7', '3.8', '3.9'])
def integration_tests(session):
    session.install('pytest')
    session.install('-r', 'requirements.txt')
    session.run('pytest', 'tests/integration')

@nox.session
def docs(session):
    session.install('sphinx')
    session.run('sphinx-build', 'docs', 'docs/_build')
