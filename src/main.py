from riot_api import setup_lol_watcher
from sheets import setup_service
from dotenv import load_dotenv
import server

def main():
    load_dotenv()
    lol_watcher = setup_lol_watcher()
    service = setup_service()
    server.run(lol_watcher, service)

if __name__ == '__main__':
    main()