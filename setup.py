#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
	name="memo",
	version="1.0",
	description="memo command",
	url="https://github.com/maruyu998/memo",
	install_requires=[],
	packages=find_packages(),
	entry_points={
		"console_scripts":[
			"memo = memo:main"
		]
	},
	include_package_data=True,
	python_required=">3.8",
)