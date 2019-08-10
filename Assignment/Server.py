import sys 
import socket

"""
...
"""


def getPort():
    """
    ...
    """
    port = int(input("Select a Port Number: "))
    
    # Check port number entered
    if port < 1024 and 64000 > port:
        print("ERROR: Port number '{0}' is not within values 1,024 and 64,000.".format(port))
        sys.exit()
    
    # Creating and binding socket if no error message detected
    infoSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a = infoSocket.bind((str(infoSocket.getsockname()), port))
    ## --- Get hostname from client




def main():
    """
    ...
    """
    getPort()



main()
