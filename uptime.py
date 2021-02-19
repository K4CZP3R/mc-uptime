from time import time

class Uptime:
    def __init__(self, time_of_check: float, ping: int, online: bool ) -> None:
        self.time_of_check = time_of_check
        self.ping = ping
        self.online = online
    
    def to_dict(self):
        return {
            'time_of_check': self.time_of_check,
            'ping': self.ping,
            'online': self.online
        }
    @classmethod
    def from_dict(cls, i_dict: dict):
        return cls(
            time_of_check=float(i_dict['time_of_check']),
            ping=int(i_dict['ping']),
            online=bool(i_dict['online'])
        )
    
    @classmethod
    def new(cls, ping: int, online: bool):
        return cls(
            time_of_check=time(),
            ping=ping,
            online=online
        )