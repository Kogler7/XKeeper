import argparse
import time
from tqdm import trange

parser = argparse.ArgumentParser()

# parser.add_argument('-h', '--help', help="这是一个帮助信息")
parser.add_argument('-u', '--user', default="admin", help="user")
parser.add_argument('-p', '--password', default="xxx", help="password")

args = parser.parse_args()

tag = f"@{args.user}"

while True:
    rcv = input(f"keeper{tag}>")
    if rcv == "exit":
        exit()
    elif rcv == "log":
        print(args)
    elif rcv == "run":
        for i in trange(10):
            time.sleep(1)
    else:
        print("Unexpected Command.")