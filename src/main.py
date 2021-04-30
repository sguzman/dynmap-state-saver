import logging

def init_log() -> None:
    logging.basicConfig(
        format=f'%(asctime)s %(levelname)-8s %(message)s',
        level=logging.DEBUG,
        datefmt='%Y-%m-%d %H:%M:%S')


def init() -> None:
    init_log()

def main() -> None:
    init()