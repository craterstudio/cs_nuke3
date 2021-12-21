import os
from dbg import Dbg
from gizmo_list import GizmoList
from gizmo_add import GizmoAdd
from gizmo_menu import GizmoMenu

def gizmo_list_do():
    '''
        gizmo_list_do do a gizmo listing
    ''' 
    d=Dbg()
    gizmoList=GizmoList()
    gizmoListt=None
    gizmoAdd=None
    gizmoAddd=None
    gizmoMenu=None

    d.print("NUKE MENU PY ","{} {}".format(os.environ["NK_PATH_GIZMOS"],os.environ["NK_PATH_NK"]))

    gizmoListt=gizmoList.doStr("dir /a-D /S /B path",os.environ["NK_PATH_GIZMOS"])

    d.print("NUKE MENU PY ","{}".format(gizmoListt.getStr()))

    gizmoAdd=GizmoAdd(gizmoListt.getStr())
    gizmoAddd=gizmoAdd.doStr()

    d.print("NUKE MENU PY ","{}".format(gizmoAddd.getStr()))

    gizmoMenu=GizmoMenu(gizmoListt.getStr())
    gizmoMenu.doStr(os.environ["NK_PATH_GIZMOS"])

if __name__ == "__main__":
    '''
        menu.py called any time for nuke gui
    '''
    gizmo_list_do()
