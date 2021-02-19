from time import time

class Uptime:
    def __init__(self, time_of_check: int, ping: int, players_online:int, online: bool ) -> None:
        self.time_of_check = time_of_check
        self.ping = ping
        self.players_online = players_online
        self.online = online
    
    def to_dict(self):
        return {
            'time_of_check': self.time_of_check,
            'ping': self.ping,
            'players_online': self.players_online,
            'online': self.online
        }
    @classmethod
    def from_dict(cls, i_dict: dict):
        return cls(
            time_of_check=int(i_dict['time_of_check']),
            ping=int(i_dict['ping']),
            players_online=int(i_dict['players_online']),
            online=bool(i_dict['online'])
        )
    
    @classmethod
    def new(cls, ping: int, players_online:int, online: bool):
        return cls(
            time_of_check=int(time() * 1000),
            ping=ping,
            players_online=players_online,
            online=online
        )