import json
import logging
import requests
from typing import Dict

url: str = 'https://emperor.hexa-network.net'

def init_log() -> None:
    logging.basicConfig(
        format=f'%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')


def init() -> None:
    init_log()

def config() -> Dict:
    config_url: str = f'{url}/up/configuration'
    resp: str = requests.get(config_url).text
    obj: Dict = json.loads(resp)

    return json.dumps(obj, indent=4, sort_keys=True)

def main() -> None:
    init()
    print(config())

if __name__ == "__main__":
    main()
