# FieldShortcuts.py
# sys.path.append('./');import d3script

from gui.inputmap import *
from d3 import *
import d3script

def initCallback():
    d3script.log("EncoderLink","EncoderLink Loaded")


def openManager():
    widget = LayerColorManager()

    d3gui.root.add(widget)
    widget.pos = (d3gui.root.size / 2) - (widget.size/2)
    widget.pos = Vec2(widget.pos[0],widget.pos[1]-100)

class LayerColorManager(Widget):

    def __init__(self):
        Widget.__init__(self)
        self.add(TitleButton('Test'))

        critWidget = Widget()
        valWidget = Widget()
        colorWidget = Widget()

        critWidget.add(TextLabel('Criteria'))
        valWidget.add(TextLabel('Value'))
        colorWidget.add(TextLabel('Color'))



SCRIPT_OPTIONS = {
    "minimum_version" : 23, # Min. compatible version
    "init_callback" : initCallback, # Init callback if version check passes
    "scripts" : [
        {
            "name" : "TCB-SCRIPT", # Display name of script
            "group" : "TCB_GROUP", # Group to organize scripts menu.  Scripts menu is sorted a separated by group
            "help_text" : "This is a Test", #text for help system
            "callback" : openManager, # function to call for the script
        }
    ]
}
