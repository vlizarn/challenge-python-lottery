import random

import data.cover as Class

class Lottery(Class.Cover):

    message = Class.message
    elements = list()
    reward = list()
    won = True
    count = 0

    def __init_subclass__(
            cls,
            lmode = "Auto",
            lTitle = "Default",
            lTimes = 5,
            lTimesConjunt = 7,
            lTimesStar = 3,
            lMaxConjunt = 50,
            lMaxStar = 9,
            lRandConjunt = False,
            lRandStar = False
        ):
            cls.mode = lmode
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

        if self.mode == "Auto" or self.mode == "Manual":
   
            try:
                if int(self.times) > 0:
                    self.header()
                    self.build()
                    self.footer()
                else:
                    self.print('msg', 'lottery', 4)

            except ValueError:
                    self.print('msg', 'error', 1)
        else:
            self.print('msg', 'lottery', 3)

    def matrix(self, mode, limit, timeslimit, randBool):
        storage, group, value = list(), list(), int

        def rand(data, mode):
            return (data, random.randint(1, data)) [mode == True]

        def manual(x, y):
            return int(input(f'Element[{x}][{y}]='))

        for x in range(self.times):
            element = rand(timeslimit, randBool)

            if randBool == True:
                value = self.times - 1
            else:
                value = 0

            for y in range(element+value):
                autoValues = random.randint(1, limit)

                try:
                    if mode == "Auto":
                        storage.append(autoValues)

                    if mode == "Manual":
                        manualValues = manual(x, y)

                        if manualValues > 0 and manualValues <= limit:
                            storage.append(manualValues)
                        else:
                            storage.append(autoValues)
                            self.print('msg', 'error', 2)

                except ValueError:
                    storage.append(autoValues)
                    self.print('msg', 'error', 2)

            group.append(storage[x*element:element+x*element])

            if len(group) <= self.times:
                pass
            else:
                group.pop(0)

        return group

    def generate(self):
        self.times = (1, int(self.times)) [int(self.times) > 1]

        def annex(data, name, amount = 1):
            storage = list()

            storage.append(
            [
                self.matrix(
                    mode = name,
                    limit = self.maxConjunt,
                    timeslimit = self.timesConjunt,
                    randBool = self.randConjunt,
                ),
                self.matrix(
                    mode = name,
                    limit = self.maxStar,
                    timeslimit = self.timesStar,
                    randBool = self.randStar,
                )
            ])
                
            for x in range(self.times):
                data.append([storage[0][0][x], storage[0][1][x]])

            if len(data) > amount:
                storage.pop(0)
                data.pop(0)
            else:
                pass

            return data

        annex(self.reward, "Auto")
        annex(self.elements, self.mode, self.times)

        if self.mode == "Manual":
            self.print('null', 'null', 0)
        else:
            pass
   
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
        self.generate()
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