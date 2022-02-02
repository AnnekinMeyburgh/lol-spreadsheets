from riot_api import collect_riotwatcher, PrimSummoner, Region
from sheets.get import get_lol_sheet, get_lol_sheet_names
from sheets.update import update_lol_sheet, create_lol_sheet, remove_lol_sheet
from string import ascii_uppercase
import os

def get_prim_summoners(service):
    resp = get_lol_sheet(service, 'Summoners', 'A2:C')
    prim_summoners = []
    for row in resp:
        prim_summoners.append(
            PrimSummoner(
                name=row[1],
                region=Region(row[2].lower())
            )
        )
    return prim_summoners

def update_summoner_sheet(lol_watcher, service, sheets, prim_summoner):
    riotcollect = collect_riotwatcher(lol_watcher, prim_summoner)
    
    order_tmp = [(value['champion_data']['id'], key) for key, value in riotcollect.champions.items()]
    order_tmp.sort()
    order = [key for name, key in order_tmp]

    columns = []

    columns.append(("Champion", [riotcollect.champions[key]['champion_data']['id'] for key in order]))
    columns.append(("Level", [riotcollect.champions[key].get('championLevel',0) for key in order]))
    columns.append(("XP", [riotcollect.champions[key].get('championPoints',0) for key in order]))

    total_reset = os.environ.get('CHAMPION_SHEET_TOTAL_RESET','no') == 'yes'
    if total_reset:
        remove_lol_sheet(service, prim_summoner.name)

    if prim_summoner.name not in sheets or total_reset:
        create_lol_sheet(service, prim_summoner.name, from_sheet='ChampionStatsBase')

    # TODO: make use of batch update
    for i, (column_name, column) in enumerate(columns):
        column_id = ascii_uppercase[i]
        update_lol_sheet(service, prim_summoner.name, f"{column_id}1:{column_id}{len(column)+1}", [[column_name] + column], major_dimension='COLUMNS')


def run(lol_watcher, service):
    prim_summoners = get_prim_summoners(service)
    sheets = get_lol_sheet_names(service)
    for prim_summoner in prim_summoners:
        update_summoner_sheet(lol_watcher, service, sheets, prim_summoner)