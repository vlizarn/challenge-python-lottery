import os

import data.game as Class

class Program(Class.Game):

    def __init__(self):
        self.state = 1

    def __del__(self) -> None:
        super().__del__()
        self.print('msg', 'program', 0)

    def confirm(self):
        step = input(self.message.reportDict['request'][3])
        
        clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        if step == "Yes":
            self.state = 0
        elif step == "No":
            clear()
        else:
            self.print('msg', 'program', 1)
            self.confirm()

    def run(self):

        while self.state == 1:

            try:
                title = input(self.message.reportDict['request'][1])
                mode = input(self.message.reportDict['request'][0])
                amount = input(self.message.reportDict['request'][2])

                if title == "Simple":
                    Class.Game(
                        mode, title,
                        amount, 5, 2
                    ).bet()
                elif title == "Multiple":
                    Class.Game(
                        mode, title,
                        amount, 11, 5,
                        lRandConjunt=True,
                        lRandStar=True
                    ).bet()
                else:
                     self.print('msg', 'lottery', 2)
            except:
                self.error()
            finally:
                self.confirm()

def main():
    app = Program()
    app.run()

main()