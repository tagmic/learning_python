__author__="tagmic"
import sys
def test():
    args=sys.argv
    if len(args)==1:
        print ('hello world')
    elif len(args==2):
        print ('hello ,%s'%args[1])
    else:
        print ('too many arguments!')

def _private_1(name):
    print('hello %s'%name)
    
if __name__=='__main__':
    test()
    _private_1('小明')
