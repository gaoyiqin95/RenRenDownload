# -*- coding:utf-8 -*-

import urllib
import json
import config

class Comment:

    def __init__(self,userID,spider,entryId,sourceType,ownerID):
        self.url = config.COMMENTURL
        self.userID = userID
        self.spider = spider
        self.entryId = entryId
        self.sourceType = sourceType
        self.ownerID = ownerID
        self.comments = []
        
    def getCommentUrl(self, offset=0):
        data = {
                'limit' : 20,
                'desc' : 'false',
                'offset' : offset,
                'replaceUBBLarge' : 'true',
                'type' : self.sourceType,
                'entryId' : self.entryId,
                'entryOwnerId' : self.ownerID
                }
        return self.url + '?' + urllib.urlencode(data)
        
    def setContent(self,content):
#         print content
        dictinfo = json.loads(content)
        for item in dictinfo.get('comments',{}):
            temp = {}
            temp['type'] = item.get('type','')
            temp['id'] = item.get('id','')
            temp['time'] = item.get('time','')
            temp['authorName'] = item.get('authorName','')
            temp['authorId'] = item.get('authorId','')
            temp['content'] = item.get('content','')
            self.comments.append(temp)
#         print dictinfo['hasMore'], len(self.comments)
        return (dictinfo.get('hasMore',False), dictinfo.get('nextOffset',0))
            
        
    def saveContent(self):
        lines = '\n'
        for item in self.comments:
            lines += item['authorName'] + '    ' + item['time'] + '\n\n'
#             for line in item['content'].split('\n'):
#                 if line == '':
#                     continue
            line = item['content'].replace('\n','')
            line = line.replace('\r','')
            lines += '*' + line + '*\n\n'
        return lines.encode('utf-8')
    
    def work(self):
        offset = 0
        while True:
            result = self.setContent(self.spider.getContent(self.getCommentUrl(offset)))
            hasMore,nextOffset = result
            if hasMore:
                offset = nextOffset
            else:
                break
        return self.saveContent()