# from dto import Camping_review
from model.dbModule import Database
from datetime import datetime

class CampingDao:

    def get_camping_ranking(self):
        db_class = Database()
        formattedDate = datetime.now().strftime("%Y%m%d")

        sql = "select * from CAMPING_INFO INFO WHERE INFO.CAMPING_INDEX IN (SELECT POPULARITY.CAMPING_INDEX FROM CAMPING_POPULARITY POPULARITY WHERE JSON_EXTRACT(VIEWED_HISTORY_COUNT,'$.[20200113]');"
        result = db_class.executeOne(sql)
        print(result)
    def search_camping_info(self,sido,gu):
        result = None
        db_class = Database()
        sql = "select * from CAMPING_INFO INFO WHERE INFO.CAMPING_INDEX IN (SELECT ADDRESS.CAMPING_INDEX FROM CAMPING_ADDRESS ADDRESS WHERE ADDRESS.REGION= '"+sido+"' AND ADDRESS.CITY='"+gu+"');"
        try:
            result = db_class.executeOne(sql)
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
    
