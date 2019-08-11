"""
...
"""



import time
import socket
from FileRequest import ValidityChecks


def currentTime():
    """
    Returns the current time
    """
    return time.strftime("%H:%M:%S", time.localtime())


def acceptSocket(soc):
    """
    Printing server acceptance message.
    """
    port = soc.getsockname()[1]
    _, addr = soc.accept()
    
    print("{0}  IP = {1}  Port = {2}".format(currentTime(), addr[0], port))


def setUpClient():
    """
    Checking for errors and setting up the server.
    """
    # Analysing the entered host name, port number and file name
    try:
        (host, port, fileName) = input("Please enter in a Hosts Name, Port Number and a File Name:\n- ").split()  # host = "Jono
    except ValueError as e:
        print(str(e))
        exit()

    try:
        addrInfo = socket.getaddrinfo(host, port)
    except socket.error as e:
        print(str(e))
        exit()

    if int(port) < 1024 and 64000 > int(port):
        print("ERROR: Port number '{0}' is not within values 1,024 and 64,000.".format(port))
        exit()

    # try:
    #     fOpen = open(fileName, 'r')
    # except FileExistsError as e:
    #     print(str(e))
    #     exit()
    

    # Attempting to create a socket
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(str(e))
        exit()

    # # Attempting to bind to the port number
    # try:
    #     soc.connect(addrInfo)
    # except socket.error as e:
    #     print(str(e))
    #     exit()

    # # Attempting to listen for the socket
    # try:
    #     soc.listen(5)
    # except socket.error as e:
    #     print(str(e))
    #     soc.close()
    #     exit()
    
    return soc


def runClient(soc):
    """
    Runs the server until closed/exited.
    """
    while 1:
        acceptSocket(soc)


def main():
    """
    Runs and Controls the program flow of the server.
    """
    soc = setUpClient()
    # runClient(soc)



main()
