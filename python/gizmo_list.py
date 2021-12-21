import os

class GizmoList(object):
    '''
        class GizmoList list gizmos found on the file system
    '''
    def __init__(self,strr=""):
        '''
            class GizmoList initialize instance
        '''
        self.str=strr
    def getStr(self):
        '''
            class GizmoList get str
        '''
        return self.str
    def setStr(self,strr):
        '''
            class GizmoList set str
        '''
        self.str=strr
    def doStr(self,cmd,path):
        '''
            class GizmoList do str
            
                command can depend on OS
                eg NT command dir /a-D /S /B path
                list all files recursive path
                
                can be something else for linux
        '''
        p=os.popen("{} {}".format(cmd,path))

        return GizmoList(p.read())
