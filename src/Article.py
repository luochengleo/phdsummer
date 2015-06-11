import urllib2


__author__ = 'luochengsi2013'

class Article:
    def __init__(self):
        pass
    def fromString(self,line):
        title,tag,url,_,content,_,accountname,accountid,quality = line.strip().split('\t')
        self.title = title
        self.tag = tag
        self.url = url
        self.content = content
        self.accountname = accountname
        self.accountid  = accountid
        self.quality = quality
    def dump(self):
        return '\t'.join([str(item) for item in [self.id,self.quality,self.accountid,self.accountname,self.title,self.content,self.tag,self.url]])


def initArticles():
    articles = list()
    id = 0 
    for l in open('../data/hulianwang.utf8.dat'):
        id +=1 
        _article = Article()
        _article.fromString(l)
        _article.id = id
        fout = open('../data/rawwebpage/'+str(int(float(_article.quality)))+'-'+str(id)+'-'+str(_article.accountid)+'.html','w')
        print _article.url
        fout.write(urllib2.urlopen(_article.url).read())
        fout.close()
        articles.append(_article)
    return articles
def dumpArticles(articles,filename):
    open(filename,'w').write('\n'.join([a.dump() for a in articles]))

def loadArticles(filename):
    articles= list()
    for l in open(filename):
        _article = Article()
        _article.id,_article.quality,_article.accountid,_article.accountname,_article.title,_article.content,_article.tag,_article.url = l.strip().split('\t')
        articles.append(_article)
    return articles
articles = initArticles()

dumpArticles(articles,'../data/articles.dump')

loadArticles('../data/articles.dump')

initArticles()