
import maya.cmds as cmds

from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLineEdit
)


Win_ID = 'Make Cube'


class MakePysideCube(QWidget):

    def __init__(self):
        super().__init__()

        self.setObjectName(Win_ID)
        self.setWindowTitle('Make Cube')

        main_layout = QVBoxLayout()

        self.locator = ''

        # Buttons
        locator_pb = QPushButton('Make Locator')
        group_pb = QPushButton('Make Group')
        rename_pb = QPushButton('Rename')

        # Rename input
        self.rename_input = QLineEdit()
        self.rename_input.setPlaceholderText('Enter new name...')

        # Add widgets
        main_layout.addWidget(locator_pb)
        main_layout.addWidget(group_pb)
        main_layout.addWidget(self.rename_input)
        main_layout.addWidget(rename_pb)

        self.setLayout(main_layout)

        # Connections
        locator_pb.clicked.connect(self.make_locator)
        group_pb.clicked.connect(self.make_group)
        rename_pb.clicked.connect(self.rename)

    def make_locator(self):

        self.locator = cmds.spaceLocator(n='ur_locator')[0]

    def make_group(self):

        if not self.locator:
            cmds.warning('Create a locator first')
            return

        group = cmds.group(n='ur_group', em=True)

        cmds.parent(self.locator, group)

    def rename(self):

        new_name = self.rename_input.text().strip()

        if not new_name:
            cmds.warning('Enter a new name')
            return

        selection = cmds.ls(selection=True)

        if not selection:
            cmds.warning('Select an object to rename')
            return

        cmds.rename(selection[0], new_name)

        self.rename_input.clear()


print('Starting UI')

ui = MakePysideCube()
ui.show()
