import os

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
        tmpdt={}
        tmppt=""

        for item in tmplstt:
            # item is a file including full path
            tmppt=os.path.dirname(item)
            if tmppt in tmpdt:
                # item in dictionary
                tmpdt[tmppt] += 1
            else:
                # item not in dictionary add it
                # need unique items
                tmpdt[tmppt] = 1
        return GizmoAdd(tmpsp.join(list(tmpdt)))
