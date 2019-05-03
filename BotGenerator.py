from bots import Config
import os

a=open("Bot.py","r").read()

botlist=Config.GetBotNames()

for i in botlist:
    if os.path.exists("bots/"+i+".py"):
        os.remove("bots/"+i+".py")
        os.remove("bots/"+i+".sh")
        os.remove("/lib/systemd/system/"+i+".service")
        os.system("systemctl stop "+i+".service")


for i in botlist:
    open("bots/"+i+".py",'w').write("botname=\""+i+"\"\n"+a)
    cd=os.path.abspath(os.path.curdir)
    open("bots/"+i+".sh",'w').write("#!/bin/sh\ncd "+cd+"\nexec python3 bots/"+i+".py\nexit 0")

    service="""[Unit]
Description=Discord bot service
After=network.target

[Service]
Type=idle
User=root
ExecStart="""+cd+"/bots/"+i+""".sh
RestartSec=10
Restart=always

[Install]
WantedBy=multi-user.target

"""
    open("/lib/systemd/system/"+i+".service",'w').write(service)
    os.system("systemctl start "+i+".service")



    