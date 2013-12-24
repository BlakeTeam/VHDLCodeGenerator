#-------------------------------------------------------------------------------
#   PROJECT:   VHDL Code Generator
#   NAME:      Main Window
#
#   LICENSE:   GNU-GPL V3
#-------------------------------------------------------------------------------

__author__ = "BlakeTeam"

import os
import pickle

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4 import uic

from lib.System import System as _System
from lib.Block import *
from lib.Connection import *

from visual.SystemVisual import *
from data.NewProject import *
from lib.ProjectInterface import *

WIDTH = 200
HEIGHT = 200

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initializeUI()

        self.projects = {}              # All projects {string dirName: IProject project }
        self.dynamicProjectTable = {}   # All projects opened (on tabs) {int tabIndex: IProject project }
        self.currentProject = None      # Project that is being used on each moment

        self.defaultDirectory = os.getenv("USERPROFILE") + r"\VHDL Code Generator\Projects"

    def initializeUI(self):
        """ Initialize all graphics components of the Main Window.
        """
        self.ui = uic.loadUi('mainWindow.ui', self)

        # Toggling dock widgets on closing
        self.ui.BlockBox.closeEvent = lambda event: self.ui.action_Block_Box.toggle()

        self.ui.action_New_System.triggered.connect(self.create)
        self.ui.tabWidget.tabCloseRequested.connect(self.ui.tabWidget.removeTab)
        self.ui.tabWidget.currentChanged.connect(self.changeTab)

    def changeTab(self,tab):
        """ Action that is executed when the tab is changed.
            Current project should be changed.
        """
        # TODO: This is a test code, here is when we set the new current project
        try:
            # print(tab)
            pass
            # self.currentView = self.tabWidget.widget(self.tabWidget.currentIndex()).layout().itemAt(0).widget()   # Current View
            # system = _System("main",(2,3),(5,))
            # self.currentView.scene().addItem(QSystem(system))
        except AttributeError:
            pass

    def create(self):
        """ Create a new Project, generating a new TabWidget and initializing it components.
        """
        #TODO: We have to allow that the user can set the name of the current project.
        #TODO: Two projects with the same name are not allowed

        projectCreator = NProjectWindow(self)
        projectCreator.show()

    def createProject(self,name,input_info,output_info):
        directory = self.defaultDirectory + "\\" + name + ".vcgproj"
        project = IProject(directory,input_info,output_info)
        project.save()

        self.dynamicProjectTable[len(self.projects)] = project
        self.projects[name] = project
        self.currentProject = project

