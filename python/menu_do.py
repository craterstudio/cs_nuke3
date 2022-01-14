import os
import nuke
import DeadlineNukeClient
from dbg import Dbg
from gizmo_list import GizmoList
from gizmo_add import GizmoAdd
from gizmo_menu import GizmoMenu

def deadline_menu_do():
    '''
        deadline_menu_do add deadline submitter to menu
    ''' 
    menubar=nuke.menu("Nuke")
    thinkboxmenu=menubar.addMenu("&Thinkbox")
    thinkboxmenu.addCommand("Submit nuke to deadline", DeadlineNukeClient.main, "")

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
    gizmoMenuu=None

    d.print("NUKE MENU PY ","{} {} {} {}".format(os.environ["NK_PATH_GIZMOS"],os.environ["NK_PATH_NK"],len(os.environ["NK_PATH_GIZMOS"]),len(os.environ["NK_PATH_NK"])))

    gizmoListt=gizmoList.doStr("dir /a-D /S /B path",os.environ["NK_PATH_GIZMOS"])

    d.print("NUKE MENU PY ","{}".format(gizmoListt.getStr()))

    gizmoAdd=GizmoAdd(gizmoListt.getStr())
    gizmoAddd=gizmoAdd.doStr()

    d.print("NUKE MENU PY ","{}".format(gizmoAddd.getStr()))

    gizmoMenu=GizmoMenu(gizmoListt.getStr())
    gizmoMenuu=gizmoMenu.doStr(len(os.environ["NK_PATH_GIZMOS"]))

    d.print("NUKE MENU PY ","{}".format(gizmoMenuu.getStr()))


def main():
    '''
        main run for main method
    ''' 
    deadline_menu_do()
    gizmo_list_do()

