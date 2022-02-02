from riotwatcher import LolWatcher
from riot_api.datadragon import get_datadragon_version
from riot_api import Summoner

def get_all_champion_data(lol_watcher: LolWatcher, region, full=False):
    version = get_datadragon_version(lol_watcher, region)
    return lol_watcher.data_dragon.champions(version, full=full)['data']

def get_all_summoner_champion_data(lol_watcher:LolWatcher, summoner:Summoner):
    return lol_watcher.champion_mastery.by_summoner(summoner.region.value, summoner.data['id'])

def get_all_summoner_champion_data_extended(lol_watcher: LolWatcher, summoner:Summoner, full=False):
    all_champion_data = get_all_champion_data(lol_watcher, summoner.region, full=full)
    all_champion_data = {int(data['key']): data for data in all_champion_data.values()}
    all_summoner_champion_data = get_all_summoner_champion_data(lol_watcher, summoner)
    all_summoner_champion_data = {int(data['championId']): data for data in all_summoner_champion_data}
    result = {}
    for champion_id, data in all_champion_data.items():
        summoner_champion_data = all_summoner_champion_data.get(champion_id,{})
        result[champion_id] = {
            **summoner_champion_data,
            'champion_data': data
        }
    return result
