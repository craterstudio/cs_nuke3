import os
from dbg import Dbg
from gizmo_list import GizmoList
from gizmo_add import GizmoAdd

def gizmo_list_do():
    '''
        gizmo_list_do do a gizmo listing
    ''' 
    d=Dbg()

    d.print("NUKE MENU PY ","{} {}".format(os.environ["NK_PATH_GIZMOS"],os.environ["NK_PATH_NK"]))

if __name__ == "__main__":
    '''
        menu.py called any time for nuke gui
    '''
    gizmo_list_do()
