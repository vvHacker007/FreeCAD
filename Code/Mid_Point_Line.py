import FreeCADGui, Part
from pivy.coin import *


__title__="Mid Point Line profile lib"
__author__ = "Vedansh Vijaywargiya & Sujay Goswami"
__url__ = "http://www.freecadweb.org"

class midpoint_line:
    
    """This class will create a mid point line after the user clicked mid and the end points on the screen"""

    def Activated(self):
        self.view = FreeCADGui.ActiveDocument.ActiveView
        self.stack = []
        self.callback = self.view.addEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.getpoint)

    def getpoint(self, event_cb):
        event = event_cb.getEvent()
        if event.getState() == SoMouseButtonEvent.DOWN:
            pos = event.getPosition()
            point = self.view.getPoint(pos[0], pos[1])
            self.stack.append(point)
            if len(self.stack) == 2:
                l = Part.LineSegment(self.stack[1], (2*self.stack[0])-(self.stack[1]))
                shape = l.toShape()
                Part.show(shape)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
    
    def GetResources(self):
        return {'Pixmap': 'C:\Program Files (x86)\FreeCAD\Mod\Features\mpl_icon.png', 'MenuText': 'Mid Point Line', 'ToolTip': 'Creates a line by clicking 2 points on the screen'}

FreeCADGui.addCommand('midpoint_line', midpoint_line())
