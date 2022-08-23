import datetime


class LogProxy:
    def __init__(self, user: str):
        self.user = user
        self.date = datetime.datetime.now().date()
        self.month = datetime.datetime.now().strftime("%Y-%m")
        self.dir_path = "D:/CodeBase/PycharmPrjs/XKeeper/logs/"
        self.log_path = self.dir_path + str(self.month) + '.txt'
        with open(self.log_path, 'a') as f:
            f.write(f'{self.date}\n')

    def log(self, data, prt: bool = True):
        _s = str(data)
        if prt:
            print(_s)
        with open(self.log_path, 'a') as f:
            f.write(_s + '\n')

    def put(self, info):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        self.log(f"[{now}] XKeeper > {info}")

    def get(self):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        title = f"[{now}] @{self.user} > "
        rcv = input(title)
        self.log(f"{title}{rcv}", prt=False)
        return rcv
