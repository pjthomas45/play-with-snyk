import request

username ='perry'
password  = 'dskhdkasjhd732468723jh@#DFSFG$%YBGFgffg'


def login(tag):
    request.session.get(f"http://perry.host.com/?{tags}&user={username}&pass={password}")
