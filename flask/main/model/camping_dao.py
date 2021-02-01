# from dto import Camping_review
from model.dbModule import Database


class CampingDao:

    def get_camping_info(self,sido,gu):
        result = None
        db_class = Database()
        sql = "select * from CAMPING_INFO where Name="+name
        try:
            result = db_class.executeAll(sql)
        except:
            print("failed")
        return result
        # recommanded searching results

    def get_camping_review(self,name):
        db_class= Database()
        sql = "Select * from CAMPING_REVIEW where ="+name 
        try:
            result = db_class.executeAll(sql)
        except:
            print("failed")
        return result

    def get_camping_addresses(self,name):
        db_class= Database()
        sql = "Select * from CAMPING_ADDRESS where CAMPING_INDEX= "+index 
        try:
            result = db_class.executeAll(sql)
        except:
            print("failed")
        return result

    def get_every_camping_locations(self):
        db_class = Database()
        sql = "select * from CAMPING_ADDRESS"
        try:
            results = db_class.executeAll(sql)
        except:
            print("failed")
        return results
    
