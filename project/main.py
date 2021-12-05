import os

import data.message as msg
import data.cover as send
import data.lottery as machine

class Program:

    def __init__(self):
        self.run = 1

    def __del__(self) -> None:
        send.Cover('msg', 'action', 0).print()
        pass

    def status(self):
        step = input(msg.reportDict['request'][0])

        clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        if(step == "Yes"):
            self.run = 0
        elif(step == "No"):
            clear()
        else:
            send.Cover('msg', 'action', 1).print()
            self.status()

    def main(self):

        while self.run == 1:

            try:
                lottery = machine.Lottery('Simple', 5, 2, 5)
                lottery.bet()

            except:
                send.Cover('null', 'error', 0).printr()
                
            finally:
                self.status()

app = Program()
app.main()