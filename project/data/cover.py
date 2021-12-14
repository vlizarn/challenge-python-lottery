import sys

import data.message as message

class Cover():

    def __init__(self,
        lTag = 'null',
        lReport = 'null',
        lIndex = 0,
    ):
        self.tag = message.tagDict[lTag]
        self.report = message.reportDict[lReport][lIndex]
        self.content = self.tag + self.report

    def __del__(self) -> None:
        pass

    def print(self):
        print(self.content)

    def print(self, tag, report, index):
        self.tag = message.tagDict[tag]
        self.report = message.reportDict[report][index]
        self.content = self.tag + self.report

        print(self.content)

    def printStr(self, index, data):

        library = {
            '1': "["+str(data[0]+1)+"]"+" "+str(data[1]),
            '2': "Message: We identify "+str(data[0])+" bets equals. Try again!",
            '3': "\nMessage: You choose a "+str(data[0])+" bet.\n",
        }

        print(library[index])

    def printList(self, index, data):

        library = {
            '1': "\nPrize Values\n\nConjunts: "+str(data[0][0])+'\nStars: '+str(data[0][1]),
        }

        print(library[index])

    def string(self, index, data):
    
        library = {
            '1': "\nMessage: You choose a "+data[0]+" bet.\n",
        }

        print(library[index])  

    def error(self):
        print(message.reportDict['error'][0], sys.exc_info()[0])