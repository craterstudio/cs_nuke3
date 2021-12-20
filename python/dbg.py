class Dbg(object):
    '''
        class Dbg print debug messages if true
    '''
    def __init__(self):
        '''
            class Dbg initialize instance
        '''
        self.check=True
    def setCheck(self,check):
        '''
            class Dbg set check
        '''
        self.check=check
    def getCheck(self):
        '''
            class Dbg get check
        '''
        return self.check
    def print(self,pre,msg):
        '''
            class Dbg get check
        '''
        self.check and print(pre+msg)
