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
    
    def __init__(self, magicNum, fileNameLen, _type=TYPE):
        """ 
        Init
        """
        self.magicNum = magicNum
        self.fileNameLen = fileNameLen
        self._type = _type


    def getChecker(self):
        """
        Returns the status of the Fixed Header.
        """
        checkFileLen = self.fileNameLen < 1 or self.fileNameLen > 2**10
        if (self.magicNum != MAGIC_NO) or checkFileLen or (self._type != TYPE):
            return EXIT_FAILURE
        return EXIT_SUCCESS
