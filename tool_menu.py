import maya.cmds as cmds

def makeToolMenu():
    
    tool_menu_id = 'my_tool_menu'
    
    if cmds.menu(tool_menu_id, exists = True):
        cmds.deleteUI(tool_menu_id, menu = True)
    
    
    cmds.menu(tool_menu_id, label = 'Tool Menu', p = 'MayaWindow', tearOff = True)
    cmds.menuItem(label = 'make cube', p = tool_menu_id, command = make_cube)
    
    
def make_cube(*args):
        cmds.polyCube(n = 'mi cube')
        
        
makeToolMenu()