import configparser

class getConfig(object):
    def __init__(self,configfile):
        self.configfile = configfile
        cf = configparser.ConfigParser()  # 实例化
        cf.read(self.configfile, encoding='utf-8')
        secs = cf.sections()
        list = []
        for sec in secs:
            map = dict(cf.items(sec))
            list.append(map)
        self.list = list

    def getconfig(self):
        return self.list