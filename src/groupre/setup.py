'''Setup script for groupre.'''

# https://pythonhosted.org/an_example_pypi_project/setuptools.html

from setuptools import setup

setup(
    name='groupre',
    version='0.1',
    description='''Matching tool for assigning students to chairs
        based on student preferences and chair attributes.''',
    url='https://github.com/jeyerena/ClassTeamBuilder/tree/master',
    packages=['data_structures', 'helpers', 'matching_algorithms'],
    # install_requires=[]
    scripts=[
        'groupre.py',
        'groupre_globals.py'
    ],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha'
    ],
)
