from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in demo1/__init__.py
from demo1 import __version__ as version

setup(
	name="demo1",
	version=version,
	description="Demo1",
	author="Demo1",
	author_email="Demo1@demo1.demo1",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
