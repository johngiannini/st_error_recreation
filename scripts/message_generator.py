import time

from scripts.output import Output


def generate_messages():
    i = 0
    while True:
        Output().write(f"Still runnin...{i}")
        i += 1
        time.sleep(2)
