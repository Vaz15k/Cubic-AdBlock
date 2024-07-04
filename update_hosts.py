import requests
from datetime import datetime

# Function to download content from a URL
def download_hosts(url):
    try:
        response = requests.get(url)
        return response.text
    except Exception as e:
        print(f"Error downloading hosts from {url}: {str(e)}")
        return None

# Function to remove duplicate lines from the hosts file
def remove_duplicate_lines(hosts_content):
    lines_seen = set()
    cleaned_hosts = ""
    for line in hosts_content.split("\n"):
        if line not in lines_seen:
            cleaned_hosts += line + "\n"
            lines_seen.add(line)
    return cleaned_hosts

# Function to remove commented lines from the hosts file
def remove_commented_lines(hosts_content):
    cleaned_hosts = ""
    for line in hosts_content.split("\n"):
        if "#" not in line:
            cleaned_hosts += line + "\n"
    return cleaned_hosts

# Function to remove lines with specific addresses from the hosts file
def remove_blocked_hosts(hosts_content, blocked_hosts):
    hosts = ""
    for line in hosts_content.split("\n"):
        parts = line.split()
        if parts and len(parts) >= 2 and not any(blocked_host in parts[1] for blocked_host in blocked_hosts):
            hosts += line + "\n"
    return hosts

# Function to add a custom header to the hosts file
def add_header(hosts_content, header):
    return header + "\n" + hosts_content

# Function to add new lines to the end of the hosts file
def add_new_lines(hosts_content, new_lines):
    return hosts_content + "\n".join(new_lines)

# List of URLs for the host lists
host_lists = [
    "https://raw.githubusercontent.com/StevenBlack/hosts/master/hosts",
    "https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/malware.hosts?ref_type=heads",
    "https://gitlab.com/quidsup/notrack-blocklists/-/raw/master/trackers.hosts?ref_type=heads",
    "https://raw.githubusercontent.com/jerryn70/GoodbyeAds/master/Hosts/GoodbyeAds.txt",
    "https://pgl.yoyo.org/adservers/serverlist.php?showintro=0;hostformat=hosts",
    "https://o0.pages.dev/Pro/hosts.txt",
    "https://raw.githubusercontent.com/hagezi/dns-blocklists/main/hosts/ultimate.txt"
]

# List of addresses to be removed
blocked_addresses = [
    # AliExpress
    "alicdn.com",
    # Adobe
    "sstats.adobe.com",
    # NordVPN
    "launches.appsflyer.com",
    # Amazon
    "amazon-adsystem.com",
    "aan.amazon.com",
    "api.us-east-1.aiv-delivery.net",
    # Microsoft
    "live.com",
    "microsoft.com",
    "microsoftonline.com",
    # Allow Facebook login
    "edge.mqtt.facebook.com",
    "graph.facebook.com",
    # Streaming
    "tidal.com",
    "spotify.com",
    # News pages in some games (Brawl Start, Clash of Clans...)
    "sentry.io",
    # Google
    "googleapis.com",
    "googleadservices.com",
    "s.youtube.com",
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

# Get the current date
current_date = datetime.now().strftime("%Y-%m-%d")

# Custom header
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

# New lines to add to the end of the hosts file
# Exemple: 0.0.0.0 ads.google.com
# I don't think it's necessary, since hosts don't cover almost everything
new_lines = [
"""
# The lines below are added directly to the module

0.0.0.0 tigr1234566.github.io
"""]

# Download and concatenate the hosts from the lists
hosts_content = ""
for url in host_lists:
    content = download_hosts(url)
    if content:
        hosts_content += content + "\n"

# Remove duplicate lines
cleaned_hosts = remove_duplicate_lines(hosts_content)

# Remove commented lines
cleaned_hosts = remove_commented_lines(cleaned_hosts)

# Remove blocked hosts
hosts = remove_blocked_hosts(cleaned_hosts, blocked_addresses)

# Add custom header
hosts_with_header = add_header(hosts, header)

# Add new lines
hosts_with_new_lines = add_new_lines(hosts_with_header, new_lines)

# Write the updated file
with open("module/system/etc/hosts", "w") as file:
    file.write(hosts_with_new_lines)

print("Hosts file generated successfully!")
