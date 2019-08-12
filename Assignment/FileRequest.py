"""
The File Request record Fixed Header contains:

- 16 bit field for Magic numbers which needs to be 0x497E,
  this acts as safeguard.
- 8 bit field for type which contains the fixed value of 1.
- 16 bit field for the length of the file name,
  the value needs to be between 1 and 1,024 and the value
  is denoted as the varible n.
- Finally the record contains n byts for the actual filename.
"""


# Fixed constants
EXIT_SUCCESS = 0
EXIT_FAILURE = 1

MAGIC_NO = 0x497E  # required safeguard
TYPE     = 0x1     # required Type


class FileRequest():
    """ 
    Creating a file request.
    """
    
    def __init__(self, magicNum, fileName, _type=TYPE):
        """ 
        Init
        """
        self.magicNum = magicNum
        self._type = _type

        # Set the length of a file name
        try:
            self.fileNameLen = len(fileName)  # got a type string
        except TypeError:
            self.fileNameLen = fileName       # got a type int

    
    def encodeFixedHeader(self, record):
        """
        The Fixed Header is made up of five bytes. The Client 
        sends these bytes over to the Server through the
        socket.
        """
        # Encoding Fixed Header
        byte1 = self.magicNum >> 8    
        byte2 = self.magicNum & 0xFF      
        byte3 = self._type               
        byte4 = self.fileNameLen >> 8     
        byte5 = self.fileNameLen & 0xFF
    
        record += bytes([byte1]) + bytes([byte2]) + bytes([byte3]) + bytes([byte4]) + bytes([byte5])


    def getChecker(self):
        """
        Checks the validity of the File Request record and returns the 
        status of the Fixed Header.
        - Returns 0 if record is correct.
        """
        checkFileLen = self.fileNameLen < 1 or self.fileNameLen > 2**10
        if (self.magicNum != MAGIC_NO) or checkFileLen or (self._type != TYPE):
            return EXIT_FAILURE
        return EXIT_SUCCESS


def decodeFixedHeader(data):
    """
    Decodes the 5 byte Fixed Header and returns the three wanted
    values, (magicNum, _type and fileNameLen).
    """
    # Decoding Fixed Header
    magicNum = data[0] << 8 | data[1]    
    _type = data[2]   
    fileNameLen = data[3] << 8 | data[4]

    return (magicNum, _type, fileNameLen)