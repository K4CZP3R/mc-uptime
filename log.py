import datetime

class Log:
    @staticmethod
    def out(content: str):
        dt_now = datetime.datetime.now()
        dt_formatted = dt_now.strftime('%b %d %Y %H:%M:%S')
        print(f"[{dt_formatted}]: {content}")