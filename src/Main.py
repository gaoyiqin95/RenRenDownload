# -*- coding:utf-8 -*-
'''
    author : threegirl2014
'''
from Spider import RenRenSpider
from PersonalInfo import PersonalInfo
from FriendList import FriendList
from Status import Status
from Gossip import Gossip
from Comment import Comment
from BlogList import BlogList
from Blog import Blog
from AlbumList import AlbumList
from Album import Album
from RepoMysql import RepoMysql
import config
import Common
import datetime
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def checkPaths(ownerID):
    Common.checkPath(config.PATH)
    Common.checkPath(config.PATH + '/' + ownerID)
    Common.checkPath(config.PATH + '/' + ownerID + '/' + config.BLOGSPATH)
    Common.checkPath(config.PATH + '/' + ownerID + '/' + config.ALBUMLISTPATH)
                   
def work(userID, lonelyMan, i):

    checkPaths(ownerID=config.ownerID[i])
 
    albumList = AlbumList(userID,lonelyMan,ownerID=config.ownerID[i])
    albumList.work()
       
    status = Status(userID,lonelyMan,config.ownerID[i])
    status.work()
 
    bloglist = BlogList(userID,lonelyMan,config.ownerID[i])
    bloglist.work()
   
    gossip = Gossip(userID,lonelyMan,config.ownerID[i])
    gossip.work()
        
    repo = RepoMysql(userID,lonelyMan)
    repo.work()
    


def Main():
    d1 = datetime.datetime.now()

    lonelyMan = RenRenSpider()
    lonelyMan.login()
    userID = lonelyMan.getUserID()

    #checkPaths(userID)

    for index in range(len(config.ownerID)):
        work(userID, lonelyMan, index)

    d2 = datetime.datetime.now()
    print 'all have been done, time: ', d2 - d1


Main()