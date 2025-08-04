from pyzabbix.api import ZabbixAPI

class HostManager:
    def __init__(self, zapi, hostnames):
        self.zapi = zapi
        self.hostnames = hostnames

    def get_host_ids(self):
        ids = []
        for name in self.hostnames:
            result = self.zapi.host.get(filter={"host": [name]}, output=["hostid"])
            ids.append(result[0]['hostid'])
        return ids
