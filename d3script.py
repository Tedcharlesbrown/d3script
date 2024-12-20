# sys.path.append('./');import d3script
# d3script.refresh_scripts()

import importlib
from d3 import *
from gui.columnlistview import ColumnListView, ColumnListViewItem, ColumnListViewColumn
import os
import json
import sys
import math
import time
import struct
import socket
import win32com.client
import win32api
import win32con
from gui.track.layerview import LayerSelection

# Constants
SCRIPTSFOLDER = "./Scripts"
SCRIPTMENUTITLE = 'Script Menu'
SCRIPTBUTTONTITLE = 'Scripts'

# Utility function to find a widget by name
def findWidgetByName(name):
	"""Find a GUI widget by name."""
	return d3gui.root.findWidgetByName(name)

# Function to load scripts (basic example)
def load_scripts():
	"""Sets up a basic menu with a "Hello World" button."""
	openScriptMenu = findWidgetByName(SCRIPTMENUTITLE)
	if openScriptMenu:
		openScriptMenu.parent.close()

	# Create and show the script menu
	d3gui.root.add(ScriptMenu())
 
def refresh_scripts():
	"""Unload and reload the script."""
	if 'd3script' in sys.modules:
		del sys.modules['d3script']
	sys.path.append('./')
	import d3script
	print("Scripts refreshed.")

# Basic script menu class
class ScriptMenu(Widget):
	isStickyable = True

	def __init__(self):
		Widget.__init__(self)

		# Add a title button
		self.titleButton = TitleButton(SCRIPTMENUTITLE)
		self.add(self.titleButton)

		# Add a "Hello World" button
		self.add_button("Hello World", self.say_hello)

		self.arrangeVertical()
		d3gui.root.add(self)
		self.titleButton.toggleSticky()

	def say_hello(self):
		print("Hello, World!")

	def add_button(self, text, function):
		button = Button(text, function)
		button.border = Vec2(0, 12)
		self.add(button)
		self.arrangeVertical()

# Initialize the script
load_scripts()
