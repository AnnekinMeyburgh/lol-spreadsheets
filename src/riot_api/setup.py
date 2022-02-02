from riotwatcher import LolWatcher
import os

def setup_lol_watcher():
    return LolWatcher(os.environ.get('RIOT_API_KEY'))