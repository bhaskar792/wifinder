import subprocess
import re
from threading import Timer
import os
import signal
import time
#from airodump import AirodumpProcessor
class selecting:
    def ifconfig(self):
        self.ifconfig = subprocess.Popen(['ifconfig'],stdout=subprocess.PIPE
                                   ,stderr = subprocess.PIPE, stdin = subprocess.PIPE,
                                   universal_newlines=True, bufsize = 0)

        lines = self.ifconfig.stdout.readlines()
        self.interfaces = {}
        interfaces = self.interfaces
        count = 1
        for line in lines:

            if(line.find(': flags')!=-1):
                Interface=line.split(':')
                Interface=Interface[0].strip()
                interfaces[count] = Interface
                print(str(count)+' '+interfaces[count])
                count+=1
    def monitorMode(self):
        while True:
            print("select interface (hint: it should be wifi's interface eg. wlan0)" )
            ifId = input()
            print('selected '+ self.interfaces[int(ifId)])
            self.interface = self.interfaces[int(ifId)]
            moniterMode = subprocess.Popen(['airmon-ng','start', self.interface],stdout = subprocess.PIPE,
                                           universal_newlines=True, bufsize=0)
            lines = moniterMode.stdout.readlines()
            try:
                if lines[1].find('Found') != -1:
                    print('monitor mode turned on for ' + self.interface)
                    break

            except:
                print('can not start monitor mode select another interface')
                continue
    def listAP(self):
        while True:
                print('how long do you want to scan for Access Points in seconds')
                timeout = input()
                if self.interface.find('mon') == -1:
                    self.interface = self.interface+'mon'
                interface = self.interface
                table = ''
                stdout = []
                table_start = re.compile('\sCH')
                start_time = time.time()

                airodump = subprocess.Popen(['airodump-ng', interface], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                            universal_newlines=True, bufsize=1)

                while time.time() < start_time + int(timeout):
                    line = airodump.stdout.readline()
                    if table_start.match(line):
                        table = ''.join(stdout)
                        stdout = []
                    stdout.append(line)
                airodump.terminate()
                f = open('ap.txt','w')
                f.truncate(0)
                f.write(table)
                f.close()
                f = open('ap.txt', 'r')
                lines = f.read().splitlines()
                f.close()
                os.remove('ap.txt')
                for line in lines:
                    if line.find(';') == -1:
                        print(line)
                print('do you want to scan again Y/N')
                userInput = input()
                if userInput == 'Y' or userInput == 'y' or userInput == 'yes' or userInput == 'YES':
                    continue
                else:
                    break
       # print(stdout)
        #print(lines[1])








a = selecting()
a.ifconfig()
a.monitorMode()
a.listAP()



