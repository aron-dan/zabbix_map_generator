# 🗺️ Zabbix Map Generator

Automatize a criação de mapas no Zabbix usando a API oficial. Este projeto coleta hosts e suas interfaces de status operacional, organizando tudo em um script para gerar mapas de rede com links entre os dispositivos.

---

## 🚀 Objetivo

Evitar a criação manual e repetitiva de mapas, permitindo que redes grandes ou dinâmicas sejam representadas automaticamente.

---

## 🧰 Tecnologias

- Python 3.8+
- [PyZabbix](https://pypi.org/project/pyzabbix/) — integração com a Zabbix API
- Regex — identificação de nomes de dispositivos nas interfaces
- Arquivo `.txt` — saída do script para consumo pelo Zabbix

---

## 📁 Estrutura do Projeto

zabbix_map_generator/ ├── host_manager.py # Obtenção dos hostids ├── interface_manager.py # Filtragem de interfaces e identificação de links ├── map_creator.py # Geração do script de mapa ├── config.py # Credenciais e parâmetros ├── script_runner.py # Ponto de entrada principal


---

## ⚙️ Como usar

### 1. Instale as dependências

```bash
pip install pyzabbix
2. Configure a conexão com o Zabbix
Edite config.py ou substitua diretamente no script_runner.py:

python
ZABBIX_URL = "https://zabbix.sempre.tec.br"
ZABBIX_USER = "usuario"
ZABBIX_PASS = "senha"
3. Defina os nomes dos hosts
python
hostnames = ["router-01", "switch-core", "firewall-dmz"]
4. Execute o script
bash
python script_runner.py
5. Verifique o arquivo gerado
O script criará o MapCreateScript.txt com o conteúdo da chamada:

python
zapi.map.create(
  name = "teste",
  width = 1920,
  height = 1080,
  selements = [...],
  links = [...]
)
Esse conteúdo pode ser usado diretamente em automações no Zabbix.

🔮 Possíveis melhorias futuras
Adicionar testes unitários

Transformar em pacote instalável com setup.py

Interface web simples para controle visual

Uso de .env para configurações seguras

👨‍💻 Autor
Desenvolvido por Daniel Aron — especialista em redes e automações Zabbix.

📄 Licença
Distribuído sob a licença MIT. Veja LICENSE para mais informações.