# -*- coding: utf-8 -*-
import scrapy
import time
import json
from zqdk.items import GetMatchInfoItem
class GetMatchScheduleList(scrapy.Spider):
    name = 'getmatchschedulelist'
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
                    "apiName":"getMatchScheduleList",
                    "matchId":str(matchList['matchId']),
                    }
            yield scrapy.http.JSONRequest(url=self.url,data=data,callback=self.parse,method='POST')



    def parse(self, response):
        result=json.loads(response.text)
        print(result)
        msg=result["msg"]
        awayNearResult=result["awayLeagueMatchVOList"]
        homeNearResult = result["homeLeagueMatchVOList"]
        if msg=="成功":
            for awayMatchList in awayNearResult:

                item=GetMatchInfoItem()
                item["awayRank"] = awayMatchList.get("awayRank")
                item["awayTeamId"] = awayMatchList.get("awayTeamId")
                item["awayTeamLogo"] = awayMatchList.get("awayTeamLogo")
                item["awayTeamName"] = awayMatchList.get("awayTeamName")
                item["elapsedTime"] = awayMatchList.get("elapsedTime")
                item["existGroupMatch"] = awayMatchList.get("existGroupMatch")
                item["homeRank"] = awayMatchList.get("homeRank")
                item["homeTeamId"] = awayMatchList.get("homeTeamId")
                item["homeTeamLogo"] = awayMatchList.get("homeTeamLogo")
                item["homeTeamName"] = awayMatchList.get("homeTeamName")
                item["leagueId"] = awayMatchList.get("leagueId")
                item["leagueMatchId"] = awayMatchList.get("leagueMatchId")
                item["leagueName"] = awayMatchList.get("leagueName")
                item["leagueSeasonId"] = awayMatchList.get("leagueSeasonId")
                item["leagueStageId"] = awayMatchList.get("leagueStageId")
                item["leagueType"] = awayMatchList.get("leagueType")
                item["matchStatus"] = awayMatchList.get("matchStatus")
                item["matchTime"] = awayMatchList.get("matchTime")
                item["middle"] = awayMatchList.get("middle")
                item["qtMatchId"] = awayMatchList.get("qtMatchId")
                item["score"] = str(awayMatchList.get("score"))
                item["seasonFlag"] = awayMatchList.get("seasonFlag")

                yield item

            for homeMatchList in homeNearResult:
                item = GetMatchInfoItem()
                item["awayRank"] = homeMatchList.get("awayRank")
                item["awayTeamId"] = homeMatchList.get("awayTeamId")
                item["awayTeamLogo"] = homeMatchList.get("awayTeamLogo")
                item["awayTeamName"] = homeMatchList.get("awayTeamName")
                item["elapsedTime"] = homeMatchList.get("elapsedTime")
                item["existGroupMatch"] = homeMatchList.get("existGroupMatch")
                item["homeRank"] = homeMatchList.get("homeRank")
                item["homeTeamId"] = homeMatchList.get("homeTeamId")
                item["homeTeamLogo"] = homeMatchList.get("homeTeamLogo")
                item["homeTeamName"] = homeMatchList.get("homeTeamName")
                item["leagueId"] = homeMatchList.get("leagueId")
                item["leagueMatchId"] = homeMatchList.get("leagueMatchId")
                item["leagueName"] = homeMatchList.get("leagueName")
                item["leagueSeasonId"] = homeMatchList.get("leagueSeasonId")
                item["leagueStageId"] = homeMatchList.get("leagueStageId")
                item["leagueType"] = homeMatchList.get("leagueType")
                item["matchStatus"] = homeMatchList.get("matchStatus")
                item["matchTime"] = homeMatchList.get("matchTime")
                item["middle"] = homeMatchList.get("middle")
                item["qtMatchId"] = homeMatchList.get("qtMatchId")
                item["score"] = str(homeMatchList.get("score"))
                item["seasonFlag"] = homeMatchList.get("seasonFlag")

                yield item
            else:
                print("没有这场的数据")