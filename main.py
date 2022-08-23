import argparse

import time
from tqdm import trange
from log_proxy import LogProxy

parser = argparse.ArgumentParser()

# parser.add_argument('-h', '--help', help="这是一个帮助信息")
parser.add_argument('-u', '--user', default="admin", help="user")
parser.add_argument('-p', '--password', default="xxx", help="password")

args = parser.parse_args()

user = args.user

log = LogProxy(user)

log.put("Welcome!")

while True:
    rcv = log.get()
    if rcv == "exit":
        log.put("Goodbye!")
        exit()
    elif rcv == "log":
        log.put(args)
    elif rcv == "run":
        for i in trange(10):
            time.sleep(1)
    else:
        log.put("Unexpected Command.")
