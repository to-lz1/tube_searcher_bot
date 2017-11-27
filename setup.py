from setuptools import setup, find_packages
import sys

sys.path.append('./test')

setup(
    name='tube_searcher_bot',
    version='0.0.1',
    test_suite = 'test_suite'
)
