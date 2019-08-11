"""
...
"""



import time
import socket
from FileRequest import FileRequest


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
    fd, addr = soc.accept()
    
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

    #------ unsure
    # try:
    #     fOpen = open(fileName, 'r')
    # except FileExistsError as e:
    #     print(str(e))
    #     exit()
    #------------
    

    # Attempting to create a socket
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(str(e))
        exit()

    # Attempting to connect with the server
    try:
        soc.connect(addrInfo[0][-1])
    except socket.error as e:
        print(str(e))
        exit()

    # Preparing a File Request record for the server
    # fr = FileRequest(0x497E, 5)
    myString = "hello world"
    soc.send(myString.encode('utf-8'))
    
    return soc


# def runClient(soc):
#     """
#     Runs the server until closed/exited.
#     """
#     while 1:
#         acceptSocket(soc)


def main():
    """
    Runs and Controls the program flow of the server.
    """
    soc = setUpClient()
    # runClient(soc)


main()