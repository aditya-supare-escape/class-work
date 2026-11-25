import maya.cmds as cmds 
from PySide6.QtWidgets import (QWidget, QVBoxLayout, QPushButton)



Win_ID = 'Make Cube'

class MakePysideCube(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setObjectName(Win_ID)
        
        main_layout = QVBoxLayout()
        
        self.locator = ''
        
        locator_pb = QPushButton('Make Locator')
        group_pb= QPushButton('Make Group')
        rename_pb = QPushButton('Rename')
        
        main_layout.addWidget(locator_pb)
        main_layout.addWidget(group_pb)
        main_layout.addWidget(rename_pb)
        
        self.setLayout(main_layout)
        
        #connections 
        
        locator_pb.clicked.connect(self.make_locator)
        group_pb.clicked.connect(self.make_group)
        rename_pb.clicked.connect(self.rename)
    
        
    def make_locator(self):
        self.locator =  cmds.spaceLocator(n = 'ur_locator')
        
    def make_group(self):
        
        if not self.locator:
            cmds.warning('Create a locator first')
            
        else:
            group = cmds.group(n = 'ur_group', em = True)
            cmds.parent(self.locator, group)
        
    def rename(self):
        cmds.rename()
        
        
print('starting ui')        
ui = MakePysideCube()
ui.show()
    