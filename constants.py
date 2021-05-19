#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Standard library imports.
import json
import os

# Constant definitions.
_MODULE_PATH = os.path.dirname(os.path.realpath(__file__))
PACKAGE_NAME = "app_icon_creator"
VERSION_FILE = os.path.join(_MODULE_PATH, "version.json")

with open(VERSION_FILE, "r") as file:
    AUTHOR  = "Behron Georgantas"
    VERSION = json.load(file)

DEFAULT_ENCODING = "utf-8"

# Module dunder definitions.
__author__  = AUTHOR
__version__ = (
    f"{VERSION['letter']}."
    f"{VERSION['major']}."
    f"{VERSION['minor']}."
    f"{VERSION['patch']}."
)
