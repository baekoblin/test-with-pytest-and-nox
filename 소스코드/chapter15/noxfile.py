import nox

@nox.session
@nox.parametrize("python_version", ["3.8", "3.9", "3.10"])
@nox.parametrize("django_version", ["2.2", "3.0", "3.1"])
def tests2(session, python_version, django_version):
    session.install(f"django=={django_version}")
    session.install('pytest')
    session.run('pytest')


@nox.session
@nox.parametrize("python_version, django_version", [
    ("3.8", "2.2"),
    ("3.9", "3.0"),
    ("3.10", "3.1"),
])
def tests3(session, python_version, django_version):
    session.install(f"django=={django_version}")
    session.install('pytest')
    session.run('pytest')



import nox

@nox.session(tags=['test_tag'])
def tests4(session):
    session.install('pytest')
    session.run('pytest')

@nox.session(tags=['test_tag'])
def lint(session):
    session.install('flake8')
    session.run('flake8', 'my_project')


import nox

@nox.session
def change_dir(session):
    session.chdir('my_project')
    session.install('pytest')
    session.run('pytest')



@nox.session
def set_env(session):
    session.env['MY_VAR'] = 'value'
    session.install('pytest')
    session.run('pytest')
