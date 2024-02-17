from probability import Probability
from statistics import Statistics
from os import system

if __name__=="__main__":
    ch = True
    while(ch):
        i = input("PSTAT> ").lower().strip()
        match i:
            case "prob":
                nfo = int(input("Number of fav outcomes: "))
                to = int(input("Total Outcomes: "))
                print(Probability.prob(nfo,to))

            case "mean":
                lst = input("Elements: ")
                try:
                    tpl = lst.split()
                    print(Statistics.mean(tpl))
                except e:
                    print("Format Error: Use 'Val1 Val2 Val3 Val4' format")

            
            case "median":
                lst = input("Elements: ")
                try:
                    tpl = lst.split()
                    print(Statistics.median(tpl))
                except e:
                    print("Format Error: Use 'Val1 Val2 Val3 Val4' format")

            case "mode":
                lst = input("Elements: ")
                try:
                    tpl = lst.split()
                    print(Statistics.mode(tpl))
                except e:
                    print("Format Error: Use 'Val1 Val2 Val3 Val4' format")





            case "exit": 
                quit()

            case "clear":
                system("clear")

            case _: 
                print("Not a valid choice")
