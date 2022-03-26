#!bin/Python3
from time import sleep
import math
import base64
import socket
import sys

rPorts = [22,443,80,8080,53,19,111,17,23,67,68,69,123,135,
136,137,138,139,161,162,1900,3389,5353,5900,1433,21,3306]
def main():

    sleep(0.3)
    print("""
 __  __                           __  __       _ _   _ _              _     
|  \/  |                         |  \/  |     | | | (_) |            | |    
| \  / | ___   __ _ _ __ __ _    | \  / |_   _| | |_ _| |_ ___   ___ | |___ 
| |\/| |/ _ \ / _` | '__/ _` |   | |\/| | | | | | __| | __/ _ \ / _ \| / __|
| |  | | (_) | (_| | | | (_| |   | |  | | |_| | | |_| | || (_) | (_) | \__ |
|_|  |_|\___/ \__, |_|  \__,_|   |_|  |_|\__,_|_|\__|_|\__\___/ \___/|_|___/
               __/ |                                                      
              |___/                                                       
        """)

    print("""
        [1]Scan Ports
        [2]base64 decoder
        [3]Port test
        [4]Calculator
        [5]Notepad
        [6]Exit
        """)
def ch():
    choose = int(input("Choose a option: "))
    if choose == 1:

        rHost = input("Enter IP: ")
        rHostIP = socket.gethostbyname(rHost)
        sleep(0.3)
        print("-="*20)
        print("Please wait, scanning...", rHostIP)
        print("-="*20)

        try:

            for ports in rPorts:

                """
                portas:
                    0 = Aberta
                    1 = Fechada
                tcp connect:
                    SOCK_STREAM
                ipv4 specification:
                    AF_INET
                """

                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(0.1)
                resultado = s.connect_ex((rHostIP, ports))

                if resultado == 0:

                    sleep(0.3)
                    print("Port {} open".format(ports))

                else:

                    sleep(0.3)
                    print("Port {} closed".format(ports))

        except KeyboardInterrupt:

            print("\nProgram interrupted")
            sys.exit()

    elif choose == 2:

        try:

            coded_string = input("Type the base64: ")
            decoded = base64.b64decode(coded_string)
            sleep(0.5)
            print(decoded)

        except KeyboardInterrupt:

            print("\nProgram interrupted")
            sys.exit()

    elif choose == 3:

            rHOST = input("Enter IP: ")
            rPORT = int(input("Enter Port: "))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = s.connect_ex((rHOST,rPORT))

            if result == 0:
                
                sleep(0.3)
                print("Port {} open".format(rPORT))

            else:

                sleep(0.3)
                print("Port {} closed".format(rPORT))

    elif choose == 4:

        print("""
                [1]Addition
                [2]Subtraction
                [3]Division
                [4]Square root
                [5]Exit
            """)

        choose2 = int(input("choose a option: "))

        if choose2 == 1:

            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            print("{} + {} = {}".format(num1, num2, num1 + num2))

        elif choose2 == 2:

            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            print("{} - {} = {}".format(num1, num2, num1 - num2))

        elif choose2 == 3:

            num1 = float(input("Enter a number: "))
            num2 = float(input("Enter another number: "))
            print("{} / {} = {:.2f}".format(num1, num2, num1 / num2))

        elif choose2 == 4:

            num3 = float(input("Enter a number: "))
            print("{:.2f}".format(math.sqrt(num3)))

        elif choose2 != 5:

            sys.exit()

    elif choose == 5:
        
            create = open('Datas.txt','a')
            text = input(">>> ")
            brk = "\n"
            create.write(text)
            create.write(brk)
            main()
            ch()
    
    elif choose != 6:

        sys.exit()

main()
ch()
