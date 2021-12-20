import os

if __name__ == "__main__":
    '''
        menu.py called any time for nuke gui
    '''
    print(">>> NUKE MENU PY")
    print(">>> {} {}".format(os.environ["NUKE_PATH_GIZMOS"],os.environ["NUKE_PATH_NK"]))
