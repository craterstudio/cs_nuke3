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
        parent=""

        for item in tmplstt:
            # go through files
            parent += item[(ln+1):]
            parent += ";"

        return GizmoMenu(parent)
