import maya.cmds as cmds 

# # cmds.ls(selection = True)
# sel = cmds.ls(sl = 1)
# print(sel)

# geo_type = cmds.ls(sel, typ = 'transform')
# print(geo_type)

# types_list = cmds.ls(showType = 1)

# for i in range(0, len(types_list), 2):
#     print(f'this is the object{types_list[i]}, and its type {types_list[i+1]} ')
    

def clean_transforms(items, expected_value, transforms):
    res = []
    res_failed = []
    transform_list = transforms
    
    for item in items:
        attr_list = []
        for attr in transform_list:
            attr_list.append(cmds.getAttr(f'{item}.{attr}'))
        if attr_list != expected_value:
            res_failed.append(item)
        else:
            res.append(item)
            
    return(res_failed, res)

# sel = cmds.ls(sl=1)
# failed, passed = clean_transforms(items = sel, expected_value = [0, 0, 0], transforms=['tx', 'ty', 'tz'])
# failed, passed = clean_transforms(items = sel, expected_value = [1, 1, 1], transforms=['sx', 'sy', 'sz'])
# print(failed, passed)


Window_name = 'Maya_Win'

if cmds.window(Window_name, ex = 1):
    cmds.deleteUI(Window_name)
    print('window exists, deleting ui....')
else: 
    print('Windows does not exists')
    
    
def make_window():
    window = cmds.window(Window_name, title = 'my maya window')
    layout = cmds.columnLayout('main_layout', adj = True)
    
    button_a = cmds.button(label = 'print gello')
    button_b = cmds.button(l = 'make cube')
    
    h_layout = cmds.rowLayout('row_layout', nc = 2, adj = 2)
    label = cmds.text(l = 'this is a label')
    button_c = cmds.button(l = 'another button')
    button_d = cmds.button(l='another one', p = layout)
    
    return(window)

window = make_window()
cmds.showWindow(window)