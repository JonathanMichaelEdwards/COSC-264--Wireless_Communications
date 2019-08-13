"""
...
"""


import os
import time
import socket
from FileRequest import FileRequest, decodeFixedHeader
from FileResponse import FileResponse



# Fixed constants
BUFFER_SIZE = 200


def currentTime():
    """
    Returns the current time
    """
    return time.strftime("%H:%M:%S", time.localtime())


def sendResponse(fd, fRead, statusCode):
    """
    Sends byte data detailing the information the Client would like to
    retrieve from the Server.
    """
    record = bytearray(0)
    number = 0x497E

    fr = FileResponse(number, statusCode, 200)
    fr.encodeFixedHeader(record)
    
    # Sending data to server over the File Directory
    for line in fRead:
        record += line
    fd.send(record)


def readFile(fileName):
    """
    Reading byte data from the file.
    """
    return open("Server/"+fileName, 'rb').readlines()


def checkFile(soc, fd, data, fileName):
    """
    Attempting to read the file to see if it exists
    locally in the Server and is readable.
    - Returns Status Code of 1 when file exists and
      can be opened, otherwise 0.
    """  
    statusCode = True

    if not os.path.exists("Server/"+fileName):
        statusCode = False
        print("\nERROR: File '{0}' doesn't exist locally in Server, aborting...".format(fileName))
        print("Please try again.\n")
        fd.close()      # Closing th File Directory (fd) socket
        runServer(soc)  # Restating the loop process 

    return statusCode


def fileRequest(soc, fd, data, startTime):
    """
    ...
    """
    # Reads the first 5 bytes
    (magicNum, _type, fileNameLen) = decodeFixedHeader(data)  

    # If the time gap is greater then 1, restart process
    if (time.clock()-startTime) >= 1.0:
        print("\nERROR: File Request is erroneous, aborting...")
        print("Please try again.\n")
        fd.close()      # Closing th File Directory (fd) socket
        runServer(soc)  # Restating the loop process 

    # Checking the validity of the File Request
    fr = FileRequest(magicNum, fileNameLen, _type) 
    if fr.requestChecker():
        print("\nERROR: Couldn't read the record from the socket...")
        print("Please try again.\n")
        fd.close()      # Closing th File Directory (fd) socket
        runServer(soc)  # Restating the loop process 
    
    fileName = data[5:].decode('utf-8')  # decoding byte data
    statusCode = checkFile(soc, fd, data, fileName)  # Gets the status code
    
    return (fileName, statusCode)


def acceptSocket(soc):
    """
    Printing server acceptance message.
    """
    port = soc.getsockname()[1]
    fd, addr = soc.accept()
    print("- {0}  IP = {1}  Port = {2}".format(currentTime(), addr[0], port))

    return fd


def setUpServer():
    """
    Checking for errors and setting up the server.
    """
    # Analysing the entered port number
    port = int(input("Please enter in a Port Number: "))
    if port < 1024 or 64000 < port:
        print("\nERROR: Port number '{0}' is not within values 1,024 and 64,000...".format(port))
        print("Terminating Program")
        exit()
    
    # Attempting to create a socket
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('\n',str(e))
        exit()
    
    # Attempting to bind to the port number
    try:
        soc.bind(('', port))
    except socket.error as e:
        print('\n',str(e))
        exit()

    # Attempting to listen for the socket
    try:
        soc.listen(1)
    except socket.error as e:
        print('\n',str(e))
        soc.close()
        exit()

    return soc


def runServer(soc):
    """
    Runs the server until closed/exited.
    """
    while True:
        fd = acceptSocket(soc)
        startTime = time.clock()  # Start timer
        data = fd.recv(BUFFER_SIZE)  # Data sent from Client through a socket
        (fileName, statusCode) = fileRequest(soc, fd, data, startTime)
        fRead = readFile(fileName) 
        sendResponse(fd, fRead, statusCode)


def main():
    """
    Runs and Controls the program flow of the server.
    """
    soc = setUpServer()
    print("Waiting for Client to connect...")
    runServer(soc)
    

main()
