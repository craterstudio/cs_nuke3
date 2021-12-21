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
    def doStr(self,ln,mnu="Nodes"):
        '''
            class GizmoMenu do str
        '''
        mnuu=nuke.toolbar(mnu)
        tmplstt=self.str.split("\n")
        slc=""
        slcq=""
        parent=""
        mn=nuke.toolbar(mnu)
        mnprt=""

        for item in tmplstt:
            # go through files
            slc = item[(ln+1):]
            parent += slc
            parent += ";"
            drr,file=os.path.split(slc)
            slcq = deque(drr.split(os.sep))
            mnprt=mn.addMenu(slcq.popleft())
            while True:
                # elements in q
                if len(slcq)<0:
                    break
                mnprt=mnprt.addMenu(slcq.popleft())

        return GizmoMenu(parent)
