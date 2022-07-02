import FreeCADGui, Part
from pivy.coin import *


__title__="Mid Point Line profile lib"
__author__ = "Vedansh Vijaywargiya & Sujay Goswami"
__url__ = "http://www.freecadweb.org"

class para:
    
    """This class will create a Parallelogram after the user clicks three points on the screen"""

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
            if len(self.stack) == 3:
                l1 = Part.LineSegment(self.stack[1], self.stack[0])
                l2 = Part.LineSegment(self.stack[2], self.stack[0])
                l3 = Part.LineSegment(self.stack[1], (self.stack[1]-(self.stack[0]-self.stack[2])))
                l4 = Part.LineSegment(self.stack[2], (self.stack[2]-(self.stack[0]-self.stack[1])))
                shape1 = l1.toShape()
                shape2 = l2.toShape()
                shape3 = l3.toShape()
                shape4 = l4.toShape()
                Part.show(shape1)
                Part.show(shape2)
                Part.show(shape3)
                Part.show(shape4)
                self.view.removeEventCallbackPivy(SoMouseButtonEvent.getClassTypeId(), self.callback)
    
    def GetResources(self):
        return {'Pixmap': 'C:\Program Files (x86)\FreeCAD\Mod\Features\para_icon.png', 'MenuText': 'Parallelogram', 'ToolTip': 'Creates a Parallelogram after the user clicks three points on the screen'}

FreeCADGui.addCommand('para', para())
