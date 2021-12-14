import random

import data.cover as Class

class Lottery(Class.Cover):

    message = Class.message
    elements = list()
    reward = list()
    won = True
    count = 0

    def __init__(
        self,
        lTitle = "Default",
        lTimes = 5,
        lTimesConjunt = 7,
        lTimesStar = 3,
        lMaxConjunt = 50,
        lMaxStar = 9,
        lRandConjunt = False,
        lRandStar = False,
    ):
        self.title = lTitle
        self.times = lTimes
        self.timesConjunt = lTimesConjunt
        self.timesStar = lTimesStar
        self.maxConjunt = lMaxConjunt
        self.maxStar = lMaxStar
        self.randConjunt = lRandConjunt
        self.randStar = lRandStar

    def __init_subclass__(
            cls,
            lTitle = "Default",
            lTimes = 5,
            lTimesConjunt = 7,
            lTimesStar = 3,
            lMaxConjunt = 50,
            lMaxStar = 9,
            lRandConjunt = False,
            lRandStar = False,
        ):
            cls.title = lTitle
            cls.times = lTimes
            cls.timesConjunt = lTimesConjunt
            cls.timesStar = lTimesStar
            cls.maxConjunt = lMaxConjunt
            cls.maxStar = lMaxStar
            cls.randConjunt = lRandConjunt
            cls.randStar = lRandStar

    def __del__(self) -> None:
        self.elements.clear()
        self.reward.clear()
  
    def bet(self):
        if self.times > 0:
            self.header()
            self.build()
            self.footer()
        else:
            self.print('msg', 'lottery', 0)

    def matrix(self, times, limit):
        storage, group = list(), list()

        for x in range(self.times):

            for y in range(times):
                number = random.randint(1, limit)
                storage.append(number)

            group.append(storage[0+x*times:times+x*times])

            if len(group) <= self.times:
                pass
            else:
                group.pop(0)

        return group

    def create(self):
        self.times = (1, self.times) [self.times > 1]
        
        def rand(data, mode):
            return (data, random.randint(1, data)) [mode == True]

        def annex(data, amount = 1):
            
            for x in range(amount):

                data.append(
                [
                    self.matrix(
                        times=rand(self.timesConjunt, self.randConjunt), 
                        limit=self.maxConjunt,
                    )[x],
                    self.matrix(
                        times=rand(self.timesStar, self.randStar), 
                        limit=self.maxStar,
                    )[x],
                ])

                if len(data) > amount:
                    data.pop(0)
                else:
                    pass

            return data

        annex(self.reward)
        annex(self.elements, self.times)
   
    def filter(self):

        for x in range(self.times):
            if (self.elements.count(self.elements[x])) <= 1:
                self.count += self.elements.count(self.elements[x])
            else:
                pass

        for x in range(self.count):
            result = self.times - self.count

            if self.count == self.times:
                self.won = True

                if self.won == True:
                    self.printStr('1', [x, self.elements[x]])
                else:
                    pass
            else:
                self.won = False
                self.printStr('2', [result])

    def build(self):
        self.create()
        self.filter()

    def match(self):
        message = False

        for x in range(self.times):

            if self.elements[x] == self.reward[0] and self.won == True:
                message = True
            else:
                pass

        return [message, self.reward[0]]

    def header(self):
        self.string('1', [self.title])
 
    def footer(self):
        self.printList('1', [self.match()[1]])

        if self.match()[0] == True:
            self.print('msg', 'lottery', 0)
        else:
            self.print('msg', 'lottery', 1)