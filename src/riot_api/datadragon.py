from riotwatcher import LolWatcher

def get_datadragon_version(lol_watcher: LolWatcher, region):
    return lol_watcher.data_dragon.versions_for_region(region.value)['v']