from dataclasses import dataclass
from riot_api import Region
from riotwatcher import LolWatcher

@dataclass
class PrimSummoner:
    name: str
    region: Region

@dataclass
class Summoner:
    data: dict
    region: Region

def get_summoner_info(lol_watcher: LolWatcher, prim_summoner:PrimSummoner):
    data = lol_watcher.summoner.by_name(prim_summoner.region.value, prim_summoner.name)
    return Summoner(data=data, region=prim_summoner.region)