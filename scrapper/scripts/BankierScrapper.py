from bs4 import BeautifulSoup
import datetime
import requests
import sqlite3
from scrapper.models import Asset

class BankierScrapper:

    pageContent = ''
    url = 'https://www.bankier.pl/gielda/notowania/akcje'

    def getPageContent(self, url):
        response = requests.get(url)
        self.pageContent = response.content

    def saveAssetsToDatabase(self, assets):
        row_id = 1
        for asset in assets:
            try:
                db_asset = Asset()
                db_asset.id = row_id
                db_asset.name = asset['name']
                db_asset.code = asset['code']
                db_asset.exchange = asset['exchange']
                db_asset.download_datetime = asset['downloadDatetime']
                db_asset.save()
                row_id += 1
            except:
                print("Failed to insert data to database.")

    def clearDatabase(self):
        try:
            Asset.objects.all().delete()
        except:
            print("Failed to truncate table.") 

    def run(self):
        self.getPageContent(self.url)
        parsedHTML = self.parseContentHTML(self.pageContent)
        assets = self.getInformations(parsedHTML)
        self.clearDatabase()
        self.saveAssetsToDatabase(assets)

    def parseContentHTML(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        return soup

    def getInformations(self, parsedHTML):
        table = parsedHTML.find("table", {'class': ['sortTable', 'floatingHeaderTable', 'tablesorter', 'tablesorter-default', 'hasStickyHeaders']}).find("tbody")
        allTr = table.find_all("tr")
        datetimeNow = datetime.datetime.now().strftime('%H:%M:%S %d-%m-%Y')
        assetList = []
        for tr in allTr:
            if tr.attrs.get('class') == None:
                assetName = tr.find("td", class_='colWalor').find("a")['title']
                assetCode = tr.find("td", class_='colWalor').find("a").text
                assetExchange = tr.find("td", class_="colKurs").text
                asset = {'name': assetName, 'code': assetCode, 'exchange': assetExchange, 'downloadDatetime': datetimeNow}
                assetList.append(asset)
        return assetList
            


