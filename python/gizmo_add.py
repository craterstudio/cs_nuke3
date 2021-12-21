class GizmoAdd(object):
    '''
        class GizmoAdd add gizmo to environment
    '''
    def __init__(self,strr=""):
        '''
            class GizmoAdd initialize instance
        '''
        self.str=strr
    def setStr(self,strr=""):
        '''
            class GizmoAdd set str
        '''
        self.str=strr
    def getStr(self):
        '''
            class GizmoAdd get str
        '''
        return self.str
    def doStr(self):
        '''
            class GizmoAdd do str
        '''
        tmplstt=self.str.split("\n")
        tmpsp=";"

        return GizmoAdd(tmpsp.join(tmplstt))
