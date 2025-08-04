from pyzabbix.api import ZabbixAPI
from host_manager import HostManager
from interface_manager import InterfaceManager
from map_creator import MapCreator

zapi = ZabbixAPI(url='https://zabbix.url.com.br', user='xxx', password='xxx')
print("Connected to Zabbix API Version %s" % zapi.api_version())

hostnames = ["router-01", "switch-core", "firewall-dmz"]  # Pode vir via config/env
host_manager = HostManager(zapi, hostnames)
host_ids = host_manager.get_host_ids()

interface_manager = InterfaceManager(zapi, hostnames, host_ids)
interfaces = interface_manager.get_interfaces()

creator = MapCreator()
creator.gerar_mapa(hostnames, host_ids, interfaces)
