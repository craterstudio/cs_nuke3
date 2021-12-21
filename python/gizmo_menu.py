from collections import deque
import os
import nuke

class GizmoMenu(object):
    '''
        class GizmoMenu add gizmos to menu
    '''
    def __init__(self,strr=""):
        '''
            class GizmoMenu initialize instance
        '''
        self.str=strr
    def getStr(self):
        '''
            class GizmoMenu get str
        '''
        return self.str
    def setStr(self,strr):
        '''
            class GizmoMenu set str
        '''
        self.str=strr
    def doStr(self,splt,mnu="Nodes"):
        '''
            class GizmoMenu do str
        '''
        mnuu=nuke.toolbar(mnu)
        tmplstt=self.str.split("\n")
        parent=""

        for item in tmplstt:
            # go through files
            dirr,file=os.path.split(item)
            # file name extension
            filename,fileext=os.path.splitext(file)
            # remove initial path
            dirra,dirrb=dirr.split(splt)
            # split into parts
            dirrc=deque(dirrb[1:].split(os.sep))
            # add initial menu item
            parent=mnuu.addMenu(dirrc.popleft())

            while True:
                if len(dircc)>0:
                    # add menu items
                    parent=parent.addMenu(dirrc.popleft())
                    continue
                break

            # add command for menu
            parent.addCommand(filename,"nuke.createNode('{}')".format(file))
