from colorama import init, Fore, Back, Style
import urllib.request,urllib.parse
import json
import socket
import sys,os
import argparse
import re
init()

def banner():
    print(Fore.BLUE+" ___________                           ")      
    print("|_   _| ___ \                          ")      
    print("  | | | |_/ / __ _____   _____ _ __ ___  ___ ")
    print("  | | |  __/ '__/ _ \ \ / / _ \ '__/ __|/ _ \\")
    print(" _| |_| |  | | |  __/\ V /  __/ |  \__ \  __/")
    print(" \___/\_|  |_|  \___| \_/ \___|_|  |___/\___|"+Fore.RESET)
    print(Fore.WHITE+"\n by br0k3r | br0k3r@protonmail.com"+Fore.RESET)

def geoip(ip):
    url = 'http://ip-api.com/json/'+ip+'?fields=country,regionName,city,zip,lat,lon,isp,query'
    f = urllib.request.urlopen(url)
    data = json.loads(f.read().decode('utf-8'))
    geo=" google.com.mx/maps/@"+str(data["lat"])+","+str(data["lon"])+"z"
    print(" +--------------------------------+")
    print('{0:10}{1:23}{2}'.format(" |ISP","|"+data["isp"]," |"));
    print(" +--------------------------------+")
    print('{0:10}{1:23}{2}'.format(" |PAIS","|"+data["country"]," |"));
    print(" +--------------------------------+")
    print('{0:10}{1:23}{2}'.format(" |ESTADO","|"+data["regionName"]," |"));
    print(" +--------------------------------+")
    print('{0:10}{1:23}{2}'.format(" |CIUDAD","|"+data["city"]," |"));
    print(" +--------------------------------+")
    print('{0:10}{1:23}{2}'.format(" |CP","|"+data["zip"]," |"));
    print(" +--------------------------------+")
    print(geo)
	
def urlsock(url):
	ip=socket.gethostbyname(url)
	geoip(ip)

parser = argparse.ArgumentParser(description=banner())
parser.add_argument('-g','--geolocation',help="Geolocalizacion de IP")
parser.add_argument('-w','--whois', help="Whois a un dominio")
parser = parser.parse_args()

if parser.geolocation:
	x = re.match("^[0-9]+[.][0-9]+[.][0-9]+[.][0-9]+$", parser.geolocation)
	if x:
		geoip(parser.geolocation)
	else:		
		print("\n [x]>> IP incorrecta")
else:
	print(" "+Fore.WHITE+"\n["+Fore.RED+"x"+Fore.WHITE+"]>> "+Fore.RED+"Argumentos vacios, ingrese un argumento")


	


   

