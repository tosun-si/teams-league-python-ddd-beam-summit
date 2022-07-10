from setuptools import find_packages, setup

setup(
    name="team_league_app",
    version="0.0.1",
    install_requires=[
        'asgarde==0.16.0',
        'dacite==1.6.0',
        'dependency-injector==4.38.0',
        'pydantic==1.5.1',
        'toolz==0.11.1',
        'pampy==0.3.0'
    ],
    packages=find_packages(),
)
