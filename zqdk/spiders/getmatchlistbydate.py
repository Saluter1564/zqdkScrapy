# -*- coding: utf-8 -*-
import scrapy
import time
import json
from zqdk.items import GetMatchListItem

class GetmatchlistbydateSpider(scrapy.Spider):
    name = 'getmatchlistbydate'
    allowed_domains = ['sport.ttyingqiu.com']
    start_urls = ['http://sport.ttyingqiu.com/']

    def start_requests(self):
        url='http://sport.ttyingqiu.com/sportdata/f?agentId=2335083&platform=android&appVersion=6.1.0'
        data={
            "timestamp":str(int(time.time()*1000)),
            "verifyStr":"",
            "simple":"1",
            "apiName":"getMatchListByDate",
            "game":"0",
            "pageNo":"1",
            "pageSize":"300"
        }

        yield scrapy.http.JSONRequest(url=url,data=data,callback=self.parse,method='POST')


    def parse(self, response):
        result=json.loads(response.text)
        print(len(result['matchList']))
        for matchList in result['matchList']:
            item=GetMatchListItem()
            item["aicaiAwayId"] = matchList.get("aicaiAwayId")
            item["aicaiHomeId"] = matchList.get("aicaiHomeId")
            item["aicaiLeagueId"] = matchList.get("aicaiLeagueId")
            item["awayId"] = matchList.get("awayId")
            item["awayLogo"] = matchList.get("awayLogo")
            item["awayName"] = matchList.get("awayName")
            item["awayRank"] = matchList.get("awayRank")
            item["bigsmall"] = matchList.get("bigsmall")
            item["card"] = str(matchList.get("card"))
            item["corner"] = matchList.get("corner")
            item["elapsedTime"] = matchList.get("elapsedTime")
            item["homeId"] = matchList.get("homeId")
            item["homeLogo"] = matchList.get("homeLogo")
            item["homeName"] = matchList.get("homeName")
            item["homeRank"] = matchList.get("homeRank")
            item["isCartoon"] = matchList.get("isCartoon")
            item["isVideo"] = matchList.get("isVideo")
            item["leagueColor"] = matchList.get("leagueColor")
            item["leagueId"] = matchList.get("leagueId")
            item["leagueName"] = matchList.get("leagueName")
            item["leagueType"] = matchList.get("leagueType")
            item["matchDate"] = matchList.get("matchDate")
            item["matchId"] = matchList.get("matchId")
            item["matchTime"] = matchList.get("matchTime")
            item["middle"] = matchList.get("middle")
            item["oddsAsia"] = matchList.get("oddsAsia")
            item["oddsEurope"] = matchList.get("oddsEurope")
            item["qtMatchId"] = matchList.get("qtMatchId")
            item["score"] = str(matchList.get("score"))
            item["status"] = matchList.get("status")

            yield item
