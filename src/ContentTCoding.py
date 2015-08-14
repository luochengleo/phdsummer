__author__ = 'luocheng'
import sys
reload(sys)
sys.setdefaultencoding('utf8')


fout = open('../data/luocheng.utf8.dat','w')
for l in open('../data/luocheng.dat').readlines():
	fout.write(l.decode('gbk','ignore').encode('utf8'))
fout.close()