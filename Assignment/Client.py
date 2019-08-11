"""
...
"""



import time
import socket
import os
from FileRequest import FileRequest


def fixedHeader(fr, record):
    """
    The Fixed Header is made up of five bytes. The Client 
    sends these data bytes over to the Server through the
    socket.
    """
    byte1 = fr.magicNum >> 8    
    byte2 = fr.magicNum & 0xFF      
    byte3 = fr._type               
    byte4 = fr.fileNameLen >> 8     
    byte5 = fr.fileNameLen & 0xFF

    record += bytes([byte1]) + bytes([byte2]) + bytes([byte3]) + bytes([byte4]) + bytes([byte5])


def sendRequest(soc):
    """
    Sends byte data detailing the information the Client would like to
    retrieve from the Server.
    """
    record = bytearray(0)

    fr = FileRequest(0x497E, 5)
    fixedHeader(fr, record)
    print(record)
    # myString = "hello world"
    # soc.send(fr.encode('utf-8'))


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
        (host, port, fileName) = input("Please enter in a Hosts Name, " +
        "Port Number and a File Name:\n- ").split()  # host = "Jono
    except ValueError as e:
        print(str(e))
        exit()

    try:
        addrInfo = socket.getaddrinfo(host, port)
    except socket.error as e:
        print('\n',str(e))
        exit()

    if int(port) < 1024 and 64000 > int(port):
        print("\nERROR: Port number '{0}' is not within values 1,024 and 64,000...\n" +
        "Terminating Program.".format(port))
        exit()

    if os.path.exists("Client/"+fileName):
        print("\nERROR: File {0} already exists locally...\nTerminating Program.".format(fileName))
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

    sendRequest(soc) # Sending a request
    
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