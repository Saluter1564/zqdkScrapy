# -*- coding: utf-8 -*-
import scrapy
import time
import json
from zqdk.items import GetMatchInfoItem
class GetMatchInfoById(scrapy.Spider):
    name = 'getmatchinfobyid'
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
            data = {
                "timestamp": str(int(time.time() * 1000)),
                "verifyStr": "",
                "apiName": "getMatchInfoById",
                "leagueMatchId": str(matchList['matchId']),
            }
            print(matchList['matchId'])
            print(data)
            yield scrapy.http.JSONRequest(url=self.url,data=data,callback=self.parse,method='POST')

    def parse(self, response):
        result=json.loads(response.text)
        result=result["leagueMatchVO"]
        item = GetMatchInfoItem()
        item["awayRank"] = result.get("awayRank")
        item["awayTeamId"] = result.get("awayTeamId")
        item["awayTeamLogo"] = result.get("awayTeamLogo")
        item["awayTeamName"] = result.get("awayTeamName")
        item["elapsedTime"] = result.get("elapsedTime")
        item["existGroupMatch"] = result.get("existGroupMatch")
        item["homeRank"] = result.get("homeRank")
        item["homeTeamId"] = result.get("homeTeamId")
        item["homeTeamLogo"] = result.get("homeTeamLogo")
        item["homeTeamName"] = result.get("homeTeamName")
        item["leagueId"] = result.get("leagueId")
        item["leagueMatchId"] = result.get("leagueMatchId")
        item["leagueName"] = result.get("leagueName")
        item["leagueSeasonId"] = result.get("leagueSeasonId")
        item["leagueStageId"] = result.get("leagueStageId")
        item["leagueType"] = result.get("leagueType")
        item["matchStatus"] = result.get("matchStatus")
        item["matchTime"] = result.get("matchTime")
        item["middle"] = result.get("middle")
        item["qtMatchId"] = result.get("qtMatchId")
        item["score"] = str(result.get("score"))
        item["seasonFlag"] = result.get("seasonFlag")

        yield item