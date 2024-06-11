import requests
from datetime import datetime

# Função para baixar conteúdo de uma URL
def download_hosts(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        print(f"Erro ao baixar hosts de {url}: {str(e)}")
        return None

# Função para remover linhas duplicadas do arquivo hosts
def remove_duplicate_lines(hosts_content):
    lines_seen = set()
    cleaned_hosts = ""
    for line in hosts_content.split("\n"):
        if line not in lines_seen:
            cleaned_hosts += line + "\n"
            lines_seen.add(line)
    return cleaned_hosts

# Função para remover linhas com comentários do arquivo hosts
def remove_commented_lines(hosts_content):
    cleaned_hosts = ""
    for line in hosts_content.split("\n"):
        if "#" not in line:
            cleaned_hosts += line + "\n"
    return cleaned_hosts

# Função para remover linhas com determinados endereços do arquivo hosts
def remove_blocked_hosts(hosts_content, blocked_hosts):
    hosts = ""
    for line in hosts_content.split("\n"):
        parts = line.split()
        if parts and len(parts) >= 2 and not any(blocked_host in parts[1] for blocked_host in blocked_hosts):
            hosts += line + "\n"
    return hosts

# Função para adicionar um cabeçalho personalizado ao arquivo hosts
def add_header(hosts_content, header):
    return header + "\n" + hosts_content

# Lista de URLs das listas de hosts
host_lists = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    "https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/malware.hosts?ref_type=heads",
    "https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/trackers.hosts?ref_type=heads",
    "https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds.txt",
    "https://pgl.yoyo.org/adservers/serverlist.php?showintro=0;hostformat=hosts",
    "https://o0.pages.dev/Pro/hosts.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/ultimate.txt"
]

# Lista de endereços a serem removidos
blocked_addresses = [
    "alicdn.com",
    # Microsoft
    "live.com",
    "microsoft.com",
    "microsoftonline.com",
    # Allow Facebook login
    "facebook.com",
    # Streaming
    "tidal.com",
    "spotify.com",
    # Allows loading of news pages in some games
    "07c225f3.online",
    "sentry.io",
    # Google
    "googleapis.com",
    "googleadservices.com",
    "ads.youtube.com",
    "s.youtube.com",
    "youtube.com",
    # Samsung Apps
    "samsungrs.com",
    "samsungosp.com",
    "samsungcloud.com",
    "samsungapps.com",
    "samsung-gamelauncher.com",
    # Allow Catalog in Whatsapp
    "whatsapp.com",
    "whatsapp.net"
]

# Obter a data atual
current_date = datetime.now().strftime("%Y-%m-%d")

# Cabeçalho personalizado
header = f"""
######################################################################
#          ____            _                 _                       #
#         / ___| _   _ ___| |_ ___ _ __ ___ | |    ___  ___ ___      #
#         \___ \| | | / __| __/ _ \ '_ ` _ \| |   / _ \/ __/ __|     #
#          ___) | |_| \__ \ ||  __/ | | | | | |__|  __/\__ \__ \     #
#         |____/ \__, |___/\__\___|_| |_| |_|_____\___||___/___/     #
#            / \ |___/ | __ )| | ___   ___| | __                     #
#           / _ \ / _` |  _ \| |/ _ \ / __| |/ /                     #
#          / ___ \ (_| | |_) | | (_) | (__|   <                      #
#         /_/   \_\__,_|____/|_|\___/ \___|_|\_\                     #
######################################################################
#                                                                    #
#  Creator: Vaz15K                                                   #
#  Last Update: {current_date}                                           #
#  Based Hosts:                                                      #
#                  Steven Black | Peter Lowe | GoodbyeAds            #
#                     Hagezi    |  NoTrack   | 1Hosts                #
#                                                                    #
######################################################################
"""

# Baixar e concatenar os hosts das listas
hosts_content = ""
for url in host_lists:
    content = download_hosts(url)
    if content:
        hosts_content += content + "\n"

# Remover linhas duplicadas
cleaned_hosts = remove_duplicate_lines(hosts_content)

# Remover linhas com comentários
cleaned_hosts = remove_commented_lines(cleaned_hosts)

# Remover hosts bloqueados
hosts = remove_blocked_hosts(cleaned_hosts, blocked_addresses)

# Adicionar cabeçalho personalizado
hosts_with_header = add_header(hosts, header)

# Escrever o arquivo atualizado
with open("module/system/etc/hosts", "w") as file:
    file.write(hosts_with_header)

print("Arquivo 'hosts' gerado com sucesso!")
