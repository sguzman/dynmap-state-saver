import json
import logging
import requests
import time
from typing import Dict


request = requests.Session()


def init_log() -> None:
    logging.basicConfig(
        format=f'%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')


def init() -> None:
    init_log()

def get(path: str) -> str:
    full_url: str = f'https://emperor.hexa-network.net/up/{path}'
    return request.get(full_url).text

def get_json(path: str) -> Dict:
    resp: str = get(path)
    return json.loads(resp)


def config() -> Dict:
    return get_json('configuration')

def update() -> Dict:
    return get_json(f'world/world/')

def pretty(obj: Dict) -> str:
    return json.dumps(obj, indent=4, sort_keys=True)

def main() -> None:
    init()
    
    while True:
        logging.info(pretty(update()["updates"]))
        time.sleep(2)


if __name__ == "__main__":
    main()
