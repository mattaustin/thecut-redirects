from setuptools import setup, find_packages
from version import get_git_version


setup(
    name='thecut-redirects',
    author='The Cut',
    author_email='development@thecut.net.au',
    url='https://projects.thecut.net.au/projects/thecut-redirects',
    namespace_packages=['thecut'],
    version=get_git_version(),
    packages=find_packages(),
    include_package_data=True,
)
