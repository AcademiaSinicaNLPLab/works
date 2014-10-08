# coding: utf-8

import pymongo
db = pymongo.Connection('doraemon.iis.sinica.edu.tw')['LJ40K']

def fetch_docs(udocIDs):
    """
    fetch docs from mongodb

    Parameters
    ==========
    a list, range or xrange storing udocIDs
    """
    docs = {}
    for udocID in udocIDs:
        docs[udocID] = map(lambda x:x['sent'], db['sents'].find({'udocID': udocID}))
    for i, (udocID, sentlst) in enumerate(sorted(docs.items(), key=lambda x:x[0])):
        with open('post-'+str(i)+'.txt', 'w') as fw:
            fw.write( '\n'.join(sentlst) )
        

if __name__ == '__main__':
    
    ## fetch_docs(range(35800, 35810))