import os

import data.game as Class

class Program(Class.Game):

    def __init__(self):
        self.state = 1

    def __del__(self) -> None:
        super().__del__()
        self.print('msg', 'program', 0)

    def confirme(self):
        step = input(self.message.reportDict['request'][3])
        
        clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        if(step == "Yes"):
            self.state = 0
        elif(step == "No"):
            clear()
        else:
            self.print('msg', 'program', 1)
            self.confirme()

    def run(self):

        while self.state == 1:

            try:
                mode = input(self.message.reportDict['request'][0])
                name = input(self.message.reportDict['request'][1])
                amount = input(self.message.reportDict['request'][2])

                if name == "Simple":
                    Class.Game(
                        mode, name,
                        int(amount), 5, 2
                    ).bet()
                elif  name == "Multiple":
                    Class.Game(
                        mode, name,
                        int(amount), 11, 5,
                        lRandConjunt=True,
                        lRandStar=True
                    ).bet()
                else:
                     pass
            except:
                self.error()

            finally:
                self.confirme()

def main():
    app = Program()
    app.run()

main()