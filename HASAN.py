#<\>!python3.11
#<\>coded by HASAN
#----------------Don't Copy This Script--------------#
import os, sys, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('xdg-open https://facebook.com/groups/1094033011587184/')
import requests
try:
    if sys.argv[1]=='update':
        os.system('rm -rf HASAN.so')
except:
    pass
os.system('rm -rf HASAN.so')
os.system('git pull')

bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('RMXXD.so'):
        os.system('curl -L https://github.com/TechnicalHasanBhai/HASAN.so/blob/main/HASAN.so') 
        import HASAN
        #HASAN.H()
    else:
        import HASAN
        #HASAN.H()
elif bit == '32bit':
    exit('\033[1;31m\n Sorry System or 32bit device not supported ')
    
    
