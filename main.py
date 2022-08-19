import argparse

parser = argparse.ArgumentParser()

# parser.add_argument('-h', '--help', help="这是一个帮助信息")
parser.add_argument('-n', '--name', default="Kogler", help="这是一个帮助信息")

args = parser.parse_args()
print(args)

parser.parse_args()
