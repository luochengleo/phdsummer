#coding=utf8
from Article import *

articles = loadArticles('../data/articles.dump')

for a in articles:
	open('../data/batch.bat','a').write('mv '+str(int(float(a.quality)))+'-'+str(a.id)+'.html '+str(int(float(a.quality)))+'-'+str(a.id)+'-'+a.accountname+'.html\n')