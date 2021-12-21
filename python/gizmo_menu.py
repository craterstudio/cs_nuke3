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
    def doStr(self,ln,mnu="Nodes",ext=".gizmo"):
        '''
            class GizmoMenu do str
        '''
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
            # path split head tail, tail file name including extension
            drr,file=os.path.split(slc)
            filename,fileext=os.path.splitext(file)
            if fileext != ext:
                # need gizmo
                continue
            slcq = deque(drr.split(os.sep))
            mnprt=mn.addMenu(slcq.popleft())
            while True:
                # elements in q
                if len(slcq)<=0:
                    break
                mnprt=mnprt.addMenu(slcq.popleft())
            mnprt.addCommand(filename,"nuke.createNode('{}')".format(file))

        return GizmoMenu(parent)
