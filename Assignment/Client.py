"""
...
"""



import os
import time
import socket
from FileRequest import FileRequest
from FileResponse import FileResponse, decodeFixedHeader


# Fixed constants
BUFFER_SIZE = 200


def currentTime():
    """
    Returns the current time
    """
    return time.strftime("%H:%M:%S", time.localtime())

    
def readResponse(soc, data):
    """
    ...
    """
    # Reads the first 8 bytes
    # (magicNum, _type, fileNameLen) = decodeFixedHeader(data) 

    decodedData = data.decode('utf-8')  # decoding byte data
    print(decodedData)
    # Reads the first 8 bytes
    # (magicNum, _type, fileNameLen) = decodeFixedHeader(data)  
    # # Reads the first 5 bytes
    # (magicNum, _type, fileNameLen) = decodeFixedHeader(data)  

    # # If the time gap is greater then 1, restart process
    # if (time.clock()-startTime) >= 1.0:
    #     print("\nERROR: File Request is erroneous, aborting...")
    #     print("Please try again.\n")
    #     fd.close()      # Closing th File Directory (fd) socket

    # # Checking the validity of the File Request
    # fr = FileRequest(magicNum, fileNameLen, _type) 
    # if fr.responseChecker():
    #     print("\nERROR: Couldn't read the record from the socket...")
    #     print("Please try again.\n")
    #     fd.close()      # Closing th File Directory (fd) socket

    
    # # Attempting to read the file to see if it exists
    # fileName = data[5:].decode('utf-8')  # decoding file from byte array 
    # if not os.path.exists("Server/"+fileName):
    #     print("\nERROR: File '{0}' doesn't exist locally in Server, aborting...".format(fileName))
    #     print("Please try again.\n")
    #     fd.close()      # Closing th File Directory (fd) socket
    
    # return fileName


def sendRequest(soc, fileName):
    """
    Sends byte data detailing the information the Client would like to
    retrieve from the Server.
    """
    record = bytearray(0)
    number = 0x497E

    fr = FileRequest(number, fileName)
    fr.encodeFixedHeader(record)
    
    # Sending Info to the Server
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


def runClient():
    """
    Runs and Controls the program flow of the Client.
    """
    (soc, fileName) = setUpClient()
    sendRequest(soc, fileName)  # Sending a request
    data = soc.recv(BUFFER_SIZE)  # Data sent from Client through a socket
    readResponse(soc, data)


runClient()