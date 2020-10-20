#!/usr/bin/env python3
"""
Author : denton <denton@localhost>
Date   : 2020-09-13
Purpose: change workfolder to last dir in ~/.dydir
"""

# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    import os,sys


    path = os.getenv("HOME")
    try:
        with open(path + '/.dydir') as f1:
            for line in f1:
                pass
    except:
        print('Error: push did not exist!')

#    os.chdir(line[:-1])
#    os.system('cd ' + line[:-1])

    f1.close

    readFile = open(path+ '/.dydir')
    lines = readFile.readlines()
    readFile.close()
    w = open(path + '/.dydir','w')
    w.writelines([item for item in lines[:-1]])
    w.close()


# --------------------------------------------------
if __name__ == '__main__':
    main()
