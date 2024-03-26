from setuptools import setup
REQUIRES = [
    'records',
    'structlog',
    'allure-pytest'
]
setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/AndreiDudin/db_client.git',
    license='MIT',
    author='Andrey Dudin',
    author_email='.',
    install_requires=REQUIRES,
    description='db_client with allure and logger'
)
