from riot_api import PrimSummoner, Summoner
from riotwatcher import LolWatcher
from dataclasses import dataclass
from riot_api.summoner import get_summoner_info
from riot_api.champions import get_all_summoner_champion_data_extended

@dataclass
class RiotCollect:
    champions: dict
    summoner: Summoner

def collect_riotwatcher(lol_watcher:LolWatcher, prim_summoner:PrimSummoner) -> RiotCollect:
    summoner = get_summoner_info(lol_watcher, prim_summoner)
    champions = get_all_summoner_champion_data_extended(lol_watcher, summoner)
    return RiotCollect(champions=champions,summoner=summoner)
