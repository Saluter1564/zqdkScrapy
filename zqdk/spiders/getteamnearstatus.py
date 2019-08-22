# -*- coding: utf-8 -*-
import scrapy
import time
import json
from zqdk.items import GetTeamBoutExploitsItem
class GetMatchInfoById(scrapy.Spider):
    name = 'getteamnearstatus'
    allowed_domains = ['sport.ttyingqiu.com']
    start_urls = ['http://sport.ttyingqiu.com/']
    def __init__(self):
        self.url='http://sport.ttyingqiu.com/sportdata/f?agentId=2335083&platform=android&appVersion=6.1.0'
    def start_requests(self):
        data={
            "timestamp":str(int(time.time()*1000)),
            "verifyStr":"",
            "simple":"1",
            "apiName":"getMatchListByDate",
            "game":"0",
            "pageNo":"1",
            "pageSize":"300"
        }
        yield scrapy.http.JSONRequest(url=self.url,data=data,callback=self.matchId_requests,method='POST')

    def matchId_requests(self,response):
        result=json.loads(response.text)

        for matchList in result['matchList']:
            data = {"timestamp":str(int(time.time()*1000)),
                    "verifyStr":"",
                    "apiName":"getTeamNearStatus",
                    "matchId":str(matchList['matchId']),
                    "number":"10"
                    }
            yield scrapy.http.JSONRequest(url=self.url,data=data,callback=self.parse,method='POST')



    def parse(self, response):
        result=json.loads(response.text)
        awayNearResult=result["awayNearStatus"]["list"]
        homeNearResult = result["awayNearStatus"]["list"]
        for awayMatchList in awayNearResult:

            item=GetTeamBoutExploitsItem()
            item["amidithion"] = awayMatchList.get("amidithion")
            item["asiaHanciap"] = awayMatchList.get("asiaHanciap")
            item["asiaResult"] = awayMatchList.get("asiaResult")
            item["awayName"] = awayMatchList.get("awayName")
            item["awayTeamId"] = awayMatchList.get("awayTeamId")
            item["awayTeamLogo"] = awayMatchList.get("awayTeamLogo")
            item["bigSamllResult"] = awayMatchList.get("bigSamllResult")
            item["bigSmallHanciap"] = awayMatchList.get("bigSmallHanciap")
            item["fullResult"] = awayMatchList.get("fullResult")
            item["halfResult"] = awayMatchList.get("halfResult")
            item["homeName"] = awayMatchList.get("homeName")
            item["homeTeamId"] = awayMatchList.get("homeTeamId")
            item["homeTeamLogo"] = awayMatchList.get("homeTeamLogo")
            item["leagueId"] = awayMatchList.get("leagueId")
            item["leagueName"] = awayMatchList.get("leagueName")
            item["matchId"] = awayMatchList.get("matchId")
            item["matchTime"] = awayMatchList.get("matchTime")
            item["middle"] = awayMatchList.get("middle")
            item["qiutanMatchId"] = awayMatchList.get("qiutanMatchId")

            yield item

        for homeMatchList in homeNearResult:
            item = GetTeamBoutExploitsItem()
            item["amidithion"] = homeMatchList.get("amidithion")
            item["asiaHanciap"] = homeMatchList.get("asiaHanciap")
            item["asiaResult"] = homeMatchList.get("asiaResult")
            item["awayName"] = homeMatchList.get("awayName")
            item["awayTeamId"] = homeMatchList.get("awayTeamId")
            item["awayTeamLogo"] = homeMatchList.get("awayTeamLogo")
            item["bigSamllResult"] = homeMatchList.get("bigSamllResult")
            item["bigSmallHanciap"] = homeMatchList.get("bigSmallHanciap")
            item["fullResult"] = homeMatchList.get("fullResult")
            item["halfResult"] = homeMatchList.get("halfResult")
            item["homeName"] = homeMatchList.get("homeName")
            item["homeTeamId"] = homeMatchList.get("homeTeamId")
            item["homeTeamLogo"] = homeMatchList.get("homeTeamLogo")
            item["leagueId"] = homeMatchList.get("leagueId")
            item["leagueName"] = homeMatchList.get("leagueName")
            item["matchId"] = homeMatchList.get("matchId")
            item["matchTime"] = homeMatchList.get("matchTime")
            item["middle"] = homeMatchList.get("middle")
            item["qiutanMatchId"] = homeMatchList.get("qiutanMatchId")

            yield item