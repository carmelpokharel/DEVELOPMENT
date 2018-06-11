#!/usr/bin/python
# SHAMIL POKHAREL 2016
# Deletes Python's '.pyc' compilation files in the current directory
import os
import time

environment = os.getcwd()

def cleanCompileFiles(env):
	selected_dir = env

	for filename in os.listdir(selected_dir):
		if filename.endswith('.pyc'):
			os.remove(os.path.join(selected_dir, filename))

cleanCompileFiles(environment)