import socket
from tkinter import filedialog

class VNA_Driver:
    def __init__(self,sock=None,path=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock
    
    def connect(self,host,port):
        self.sock.connect((host,port))
        self.sock.send(str.encode("TST?\n"))
        reply = self.sock.recv(2056)
        if (not reply):
            print('selftest passed')
        else: 
            print('error')
            #exit()
    
 #   def config_path(self,path):
 #       self.conf_path = path
    def save_path(self):
        self.s_path = filedialog.askdirectory()
        print(self.s_path)

    def setup_without_cali(self):
        self.sock.send(str.encode("SYSTem:ERRor:CLEar"))
        self.sock.send(str.encode("DISPlay:COLor:RESet"))
        self.sock.send(str.encode("DISPlay:COUNT 1"))
        self.sock.send(str.encode("CALCulate:PARameter:COUNT 1"))
        self.sock.send(str.encode("DISPlay:WINDow1:SPLit R1C1"))
        self.sock.send(str.encode("DISPlay:WINDow1:ACTivate 1"))
        self.sock.send(str.encode("DISPlay:SIZe MAXimum"))
        self.sock.send(str.encode("CALCulate:PARameter1:DEFine S11"))
        self.sock.send(str.encode("CALCulate:PARameter1:FORMat MLOGarithmic"))

        self.sock.send(str.encode("SENS:FREQ:STAR %d\n" %(f_begin*1E9)))
        self.sock.send(str.encode("SENS:FREQ:STOP %d\n" %(f_begin*1E9)))
        self.sock.send(str.encode("SENS:SWEEP:TYPe LINear\n"))
        self.sock.send(str.encode("SENS:SWEEP:POINTS %d\n" %(points)))
        #vna.send(str.encode("SENS:BAND 70E1\n"))

        #vna.send(str.encode("CALCulate1:PARameter4:FORMat SMITh\n"))

        #self.send(str.encode("MMEMory:CATalog? '%s'" %(setup_dir)))
        #self.send(str.encode("MMEMory:CATalog? '%s'" %(data_dir)))

    def setup_recall(self):
        return 0


    def data_save(self,filename):
        self.sock.send(str.encode("MMEMory:STORe '%s\%s'" %(self.s_path,filename)))
        #f = open('%s\%s'%(self.s_path,filename),'w')



if __name__ == '__main__':
    import time 
    vna = VNA_Driver()
    vna.save_path()

    
    #for i in range(10):
     #   vna.data_save('auto_save_%d.csv' %(i+1))
      #  time.sleep(2)


    time.sleep(5)
    vna.connect("10.36.125.226", 5001)
    for i in range(10):
        vna.data_save('auto_save_%d.csv' %(i+1))
        time.sleep(2)

    
 
