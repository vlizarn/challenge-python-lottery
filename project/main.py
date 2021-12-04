import os
import sys

class Program:

    def __init__(self):
        self.run = 1
        self.main()

    def __del__(self):
        print("\nMessage: The program closed!")

    def status(self):
        step = input("\nDo you want close program (Yes or No)?\n")

        clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

        if(step == "Yes"):
            self.run = 0
        elif(step == "No"):
            clear()
        else:
            print("\nMessage: Try another option!")
            self.status()

    def main(self):

        while self.run == 1:

            try:
                pass

            except:
                pass
                
            finally:
                self.status()

app = Program()
app.main()
