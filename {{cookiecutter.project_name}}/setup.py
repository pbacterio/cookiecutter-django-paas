from setuptools import setup

setup(name='{{cookiecutter.project_name}}',
#      version='1.0',
#      description='OpenShift App',
#      author='Your Name',
#      author_email='example@example.com',
#      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=['Django', 'waitress', 'dj-database-url', 'dj-static', 'psycopg2'],
     )

