import re

class InterfaceManager:
    def __init__(self, zapi, hostnames, host_ids):
        self.zapi = zapi
        self.hostnames = hostnames
        self.host_ids = host_ids

    def _limpar_nome_dispositivo(self, interface):
        encontrados = re.findall(r'\(([^)]+)\)', interface)
        for texto in encontrados:
            for dispositivo in self.hostnames:
                if dispositivo in texto:
                    return dispositivo
        for dispositivo in self.hostnames:
            if dispositivo in interface:
                return dispositivo
        return None

    def _remover_duplicatas(self, lista):
        vistos = set()
        return [x for x in lista if x and not (x in vistos or vistos.add(x))]

    def get_interfaces(self):
        lista = []
        for i, host_id in enumerate(self.host_ids):
            result = self.zapi.item.get(
                output=['name'],
                hostids=[host_id],
                search={'name': 'Operational status'}
            )
            nomes = [item['name'] for item in result]
            dispositivos = [self._limpar_nome_dispositivo(nome) for nome in nomes]
            dispositivos = self._remover_duplicatas(dispositivos)
            indices = [self.hostnames.index(d) for d in dispositivos if d in self.hostnames]
            lista.append([self.hostnames[i], dispositivos, indices])
        return lista
