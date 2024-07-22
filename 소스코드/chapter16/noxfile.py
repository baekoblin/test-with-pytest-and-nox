import nox

@nox.session
def type_check(session):
    session.install('mypy')
    session.run('mypy','test_nox.py')


@nox.session
def external_command(session):
    session.run('echo', 'Hello, world!', external=True)


@nox.session
def silent_command(session):
    session.run('echo', 'This will not be shown', silent=True)



@nox.session
def log_output(session):
    session.log('Logging this message')
    session.run('echo', 'This will be logged')


@nox.session
def install_system_dependencies(session):
    session.run_always('apt-get', 'update', external=True)
    session.run_always('apt-get', 'install', '-y', 'some-package', external=True)
