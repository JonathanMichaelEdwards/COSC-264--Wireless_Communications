"""
...
"""



import time
import socket
import os
from FileRequest import FileRequest



def currentTime():
    """
    Returns the current time
    """
    return time.strftime("%H:%M:%S", time.localtime())


def sendRequest(soc, fileName):
    """
    Sends byte data detailing the information the Client would like to
    retrieve from the Server.
    """
    record = bytearray(0)
    number = 0x497E

    fr = FileRequest(number, fileName)
    fr.encodeFixedHeader(record)
    
    # Sending Info to Server
    soc.send(record)
    soc.send(fileName.encode('utf-8'))


def setUpClient():
    """
    Checking for errors and setting up the server.
    """
    # Analysing the entered host name, port number and file name
    try:
        (host, port, fileName) = input("Please enter in a Hosts Name, " +
        "Port Number and a File Name:\n- ").split()
    except ValueError as e:
        print('\n',str(e))
        exit()

    try:
        addrInfo = socket.getaddrinfo(host, port)
    except socket.error as e:
        print('\n',str(e))
        exit()

    if int(port) < 1024 or 64000 < int(port):
        print("\nERROR: Port number '{0}' is not within values 1,024 and 64,000...".format(port))
        print("Terminating Program")
        exit()

    if os.path.exists("Client/"+fileName):
        print("\nERROR: File '{0}' already exists locally...\nTerminating Program.".format(fileName))
        exit()
   
    # Attempting to create a socket
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('\n',str(e))
        exit()

    # Attempting to connect with the server
    try:
        soc.connect(addrInfo[0][-1])
    except socket.error as e:
        print('\n',str(e))
        exit()

    return (soc, fileName)


def main():
    """
    Runs and Controls the program flow of the server.
    """
    (soc, fileName) = setUpClient()
    sendRequest(soc, fileName)  # Sending a request


main()