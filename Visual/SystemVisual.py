#
#   PROJECT:   VHDL Code Generator
#   NAME:      SystemVisual
#
#   LICENSE:   GNU-GPL V3
#

__author__ = "BlakeTeam"

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from Visual import *
from Visual import *

class QSystem(QGraphicsItem):
    COLOR = 0,0,100,100 # Red, Green, Blue, Alpha
    HEIGHT = 160

    def __init__(self, system, parent = None):
        """ QGraphicsItem that represent the system of the current project.
            Each QSystem has an array of input ports, an array of output ports,
            & a rectangle that enclose the area (pure estetically)
        """
        super().__init__(parent)
        self.system = system
        self.rect = QRectF(-4*WIDTH/10,-4*HEIGHT/10,4*WIDTH/5,4*HEIGHT/5)

    def boundingRect(self):
        return self.rect

    def shape(self):
        path = QPainterPath()
        path.addRect(self.rect)
        return path

    def paint(self,painter,styleOptionGraphicsItem,widget):
        InputBlock = self.system.system_input
        OutputBlock = self.system.system_output

        di = self.height/(len(InputBlock.input_ports) + 1)
        do = self.height/(len(OutputBlock.output_ports) + 1)

        painter.drawRect(self.rect)
        painter.fillRect(self.rect, QColor(*QSystem.COLOR))

        # Drawing input ports
        for i in range(len(InputBlock.input_ports)):
            painter.drawLine(-4*WIDTH/10, di*(i + 1), -4*WIDTH/10 + 20, di*(i + 1))
            print(InputBlock.input_ports[i])

        # Drawing output ports
        for i in range(len(OutputBlock.output_ports)):
            painter.drawLine(70 ,do*(i + 1), 90,do*(i + 1))