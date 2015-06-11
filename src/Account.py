import urllib2
accounts = set()
import os
for f in os.listdir('../data/rawwebpage'):
	accounts.add('-'.join(f.replace('.html','').split('-')[2:]))

for acc in accounts:
	print len(acc)
	open('../data/accounts.txt','a').write(acc+'\n')