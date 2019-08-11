"""
...
"""



import time
import socket


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

    return fd


def setUpServer():
    """
    Checking for errors and setting up the server.
    """
    # Analysing the entered port number
    port = int(input("Please enter in a Port Number: "))
    if port < 1024 and 64000 > port:
        print("ERROR: Port number '{0}' is not within values 1,024 and 64,000.".format(port))
        exit()
    
    # Attempting to create a socket
    try:
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print(str(e))
        exit()
    
    # Attempting to bind to the port number
    try:
        soc.bind(('', port))
    except socket.error as e:
        print(str(e))
        exit()

    # Attempting to listen for the socket
    try:
        soc.listen(1)
    except socket.error as e:
        print(str(e))
        soc.close()
        exit()

    return soc


def runServer(soc):
    """
    Runs the server until closed/exited.
    """
    while 1:
        fd = acceptSocket(soc)
        data = fd.recv(20)
        print("The data is: ", str(data))
        # fd.send(data)

    # fd.close()


def main():
    """
    Runs and Controls the program flow of the server.
    """
    soc = setUpServer()
    print("Waiting to be connected...")
    runServer(soc)
    


main()


# record = bytearray(0)


# # Reading the fixed header bytes into a bytearray
# byte1 = fr.magicNum >> 8    
# byte2 = fr.magicNum & 0xFF      
# byte3 = fr._type               
# byte4 = fr.fileNameLen >> 8     
# byte5 = fr.fileNameLen & 0xFF

# record += bytes([byte1]) + bytes([byte2]) + bytes([byte3]) + bytes([byte4]) + bytes([byte5])
# print(record)