__author__ = 'luocheng'
import sys
reload(sys)
sys.setdefaultencoding('utf8')

open('../data/hulianwang.utf8.dat','w').write(open('../data/hulianwang.dat').read().decode('gbk','ignore').encode('utf8'))