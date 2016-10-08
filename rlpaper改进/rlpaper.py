import os
import re
import requests 
os.chdir(r'C:\Users\v-yuewng\Desktop\rlpaper')

allfilepath = 'rlpaper.txt'

allfile = open(allfilepath,'r')

filelines = allfile.readlines()

inafolder = 0


def transtitle(title):
    a =re.search('\:',title)
    
    if a:
        res = title[:a.start()]+'_'+title[a.end():]+'.pdf'
    else:
        res = title + '.pdf'
    return res 
    
def transpdf(pdf):
    r = requests.get(pdf) 
    return r.content
    
    
def arxivpdf(pdf):
    a = re.search('abs',pdf)
    return pdf[:a.start()]+'pdf'+pdf[a.end():]
    
def createfolder(path):
    if not os.path.exists(path):
        os.mkdir(ii[3:-1])
        

for ii in filelines:
    print 0
    if ii[0:2]=="##" and inafolder==0:
        createfolder(ii[3:-1])
        os.chdir('./'+ii[3:-1])
        inafolder = 1
        print 1
    if ii[0:2]=="##" and inafolder==2:
        os.chdir('../')
        createfolder(ii[3:-1])
        os.chdir('./'+ii[3:-1])
        inafolder = 1
        print 2
    if re.search('http',ii):
        info = re.search('.*\[(.*)\].*\((http.*)\).*',ii)
        title = info.group(1)
        pdf = info.group(2)
        if not os.path.exists(transtitle(title)):
            if pdf[-3:]=="pdf":
                with open(transtitle(title),'wb') as f:
                    f.write(transpdf(pdf))
            elif re.search('arxiv',pdf):
                pdf = arxivpdf(pdf+'.pdf')
                with open(transtitle(title),'wb') as f:
                    f.write(transpdf(pdf))
            inafolder =2
    print 'done'+str(ii)
       
    
    
    
    