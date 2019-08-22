# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

"""
比赛列表
"""
class GetMatchListItem(scrapy.Item):
    table='article_matchlist'
    aicaiAwayId = scrapy.Field()
    aicaiHomeId = scrapy.Field()
    aicaiLeagueId = scrapy.Field()
    awayId = scrapy.Field()
    awayLogo = scrapy.Field()
    awayName = scrapy.Field()
    awayRank = scrapy.Field()
    bigsmall = scrapy.Field()
    card = scrapy.Field()
    corner = scrapy.Field()
    elapsedTime = scrapy.Field()
    homeId = scrapy.Field()
    homeLogo = scrapy.Field()
    homeName = scrapy.Field()
    homeRank = scrapy.Field()
    isCartoon = scrapy.Field()
    isVideo = scrapy.Field()
    leagueColor = scrapy.Field()
    leagueId = scrapy.Field()
    leagueName = scrapy.Field()
    leagueType = scrapy.Field()
    matchDate = scrapy.Field()
    matchId = scrapy.Field()
    matchTime = scrapy.Field()
    middle = scrapy.Field()
    oddsAsia = scrapy.Field()
    oddsEurope = scrapy.Field()
    qtMatchId = scrapy.Field()
    score = scrapy.Field()
    status = scrapy.Field()

"""
比赛信息
"""
class GetMatchInfoItem(scrapy.Item):
    table = 'article_leaguematchvo'
    awayRank = scrapy.Field()
    awayTeamId = scrapy.Field()
    awayTeamLogo = scrapy.Field()
    awayTeamName = scrapy.Field()
    elapsedTime = scrapy.Field()
    existGroupMatch = scrapy.Field()
    homeRank = scrapy.Field()
    homeTeamId = scrapy.Field()
    homeTeamLogo = scrapy.Field()
    homeTeamName = scrapy.Field()
    leagueId = scrapy.Field()
    leagueMatchId = scrapy.Field()
    leagueName = scrapy.Field()
    leagueSeasonId = scrapy.Field()
    leagueStageId = scrapy.Field()
    leagueType = scrapy.Field()
    matchStatus = scrapy.Field()
    matchTime = scrapy.Field()
    middle = scrapy.Field()
    qtMatchId = scrapy.Field()
    score = scrapy.Field()
    seasonFlag = scrapy.Field()

"""
比赛分析-基本面-历史交锋
"""
class GetTeamBoutExploitsItem(scrapy.Item):
    table = 'article_teamboutexploits'
    amidithion = scrapy.Field()
    asiaHanciap = scrapy.Field()
    asiaResult = scrapy.Field()
    awayName = scrapy.Field()
    awayTeamId = scrapy.Field()
    awayTeamLogo = scrapy.Field()
    bigSamllResult = scrapy.Field()
    bigSmallHanciap = scrapy.Field()
    fullResult = scrapy.Field()
    halfResult = scrapy.Field()
    homeName = scrapy.Field()
    homeTeamId = scrapy.Field()
    homeTeamLogo = scrapy.Field()
    leagueId = scrapy.Field()
    leagueName = scrapy.Field()
    matchId = scrapy.Field()
    matchTime = scrapy.Field()
    middle = scrapy.Field()
    qiutanMatchId = scrapy.Field()

class GetMatchAnalysisNumber(scrapy.Item):
    table = 'article_matchstanding'
    attackToScoreRate = scrapy.Field()
    averageLost = scrapy.Field()
    averageScore = scrapy.Field()
    beCornerKick = scrapy.Field()
    beFreeKick = scrapy.Field()
    beShootOn = scrapy.Field()
    beShooted = scrapy.Field()
    control = scrapy.Field()
    cornerKick = scrapy.Field()
    dangerousAttack = scrapy.Field()
    freeKick = scrapy.Field()
    halfControlRate = scrapy.Field()
    lostScoreRate = scrapy.Field()
    shoot = scrapy.Field()
    shootOn = scrapy.Field()
    leagueMatchId=scrapy.Field()
    awayId = scrapy.Field()
    awayLogo = scrapy.Field()
    awayName = scrapy.Field()
    homeId = scrapy.Field()
    homeLogo = scrapy.Field()
    homeName = scrapy.Field()