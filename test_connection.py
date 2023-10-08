import socket

host='localhost'
port=7777

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # open a socket to the game
    s.connect((host, port))
except OSError:
    raise ConnectionError("No active instance of Command to connect to. Aborting.")