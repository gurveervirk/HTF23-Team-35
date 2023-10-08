# -*- coding: utf-8 -*-
"""Activate virtualenv for the current interpreter:
Use exec(open(this_file).read(), {'__file__': this_file}).
This can be used when you must use an existing Python interpreter, not the virtualenv
bin/python.
"""
import os
import site
import sys

try:
    abs_file = os.path.abspath(__file__)
except NameError:
    raise AssertionError("You must use exec(open(this_file).read(), {'__file__': this_file})")

bin_dir = os.path.dirname(abs_file)
base = os.path.dirname(bin_dir)  # Strip away the bin part from the __file__ and add the path separator

# Prepend bin to PATH (this file is inside the bin directory)
os.environ["PATH"] = os.pathsep.join([bin_dir] + os.environ.get("PATH", "").split(os.pathsep))
os.environ["VIRTUAL_ENV"] = base  # Virtual env is right above the bin directory

# Add the virtual environment's libraries to the host Python import mechanism
prev_length = len(sys.path)
for lib in ["..\\Lib\\site-packages"]:  # Use double backslashes for Windows path
    path = os.path.realpath(os.path.join(bin_dir, lib))
    site.addsitedir(path.decode("utf-8") if "" else path)

sys.path[:] = sys.path[prev_length:] + sys.path[0:prev_length]
sys.real_prefix = sys.prefix
sys.prefix = base
