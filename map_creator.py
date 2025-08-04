class MapCreator:
    def __init__(self, filename="MapCreateScript.txt"):
        self.filename = filename

    def gerar_mapa(self, hostnames, host_ids, interfaces):
        with open(self.filename, "w") as f:
            f.write('zapi.map.create(\n name="teste",\n width=1920,\n height=1080,\n selements=[\n')

        for i, host_id in enumerate(host_ids):
            with open(self.filename, "a") as f:
                f.write(f'{{"selementid": {i+1}, "elements": [{{"hostid": "{host_id}"}}], "elementtype": 0, "label": "{{HOST.HOST}}\\r\\n{{HOST.CONN}}", "iconid_off": 3402}},\n')

        self._truncate_tail(5)

        with open(self.filename, "a") as f:
            f.write('],\n links=[\n')

        for i, (_, _, indices) in enumerate(interfaces):
            for idx in indices:
                with open(self.filename, "a") as f:
                    f.write(f'{{"selementid1": {i+1}, "selementid2": {idx+1}, "drawtype": 2, "color": "00CC00"}},\n')

        self._truncate_tail(4)
        with open(self.filename, "a") as f:
            f.write('\n])')

    def _truncate_tail(self, num_bytes):
        with open(self.filename, 'rb+') as f:
            f.seek(0, 2)
            size = f.tell()
            if size > 0:
                f.truncate(size - num_bytes)
