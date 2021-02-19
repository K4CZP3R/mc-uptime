from database import Database
from mcstatus import MinecraftServer
from os import getenv
from log import Log
from time import time
from uptime import Uptime

Log.out("Getting environment variabeles.")

mongo_url = str(getenv('MONGO_URL'))
mc_address = str(getenv('MC_ADDRESS'))
check_interval = int(getenv('CHECK_INTERVAL'))
Log.out(f"Minecraft server: '{mc_address}'")
Log.out(f"Check interval: '{check_interval}'")

db = Database(
    connection_string=mongo_url
)

mc = MinecraftServer(mc_address)

last_check = 0
last_alive = 0
while True:
    if time() - last_check < check_interval:
        continue

    if time() - last_alive > 60*60:
        Log.out("I'm alive!")
        last_alive = time()

    # Log.out("Checking...")
    last_check = time()
    # Log.out("Pinging...")
    try:
        status_resp = mc.status()
        ping = status_resp.latency
        players_online = status_resp.players.online
        # Log.out(f"Server responded within {ping_resp}ms")
        uptime = Uptime.new(ping, players_online, True)
    except:
        uptime = Uptime.new(-1,0, False)
        Log.out("Server seems to be down...")
    
    # Log.out(f"Uptime obj: '{uptime.__dict__}'")
    db.insert(uptime)
    # Log.out("Inserted!")
    
