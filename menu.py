import os
from gizmo_list import GizmoList
from gizmo_add import GizmoAdd

if __name__ == "__main__":
    '''
        menu.py called any time for nuke gui
    '''
    print(">>> NUKE MENU PY")
    print(">>> {} {}".format(os.environ["NK_PATH_GIZMOS"],os.environ["NK_PATH_NK"]))
