import socket
import os 

class VNA_Driver(socket):
    def __init__(self,address,port)
        super().__init__()
        self.a = address
        self.p = port
        self.connect()
    
    def connect(self):
        self.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connect((self.a, self.p))
        self.send(str.encode("TST?\n"))
        reply = vna.recv(2056)
        if (not reply):
            print('selftest passed')
        else: 
            print('error')
            exit()

    def setup_without_cali(self):
        self.send(str.encode("SYSTem:ERRor:CLEar"))
        self.send(str.encode("DISPlay:COLor:RESet"))
        self.send(str.encode("DISPlay:COUNT 1"))
        self.send(str.encode("CALCulate:PARameter:COUNT 1"))
        self.send(str.encode("DISPlay:WINDow1:SPLit R1C1"))
        self.send(str.encode("DISPlay:WINDow1:ACTivate 1"))
        self.send(str.encode("DISPlay:SIZe MAXimum"))
        self.send(str.encode("CALCulate:PARameter1:DEFine S11"))
        self.send(str.encode("CALCulate:PARameter1:FORMat MLOGarithmic"))

        self.send(str.encode("SENS:FREQ:STAR %d\n" %(f_begin*1E9)))
        self.send(str.encode("SENS:FREQ:STOP %d\n" %(f_begin*1E9)))
        self.send(str.encode("SENS:SWEEP:TYPe LINear\n"))
        self.send(str.encode("SENS:SWEEP:POINTS %d\n" %(points)))
        #vna.send(str.encode("SENS:BAND 70E1\n"))

        #vna.send(str.encode("CALCulate1:PARameter4:FORMat SMITh\n"))

        #self.send(str.encode("MMEMory:CATalog? '%s'" %(setup_dir)))
        #self.send(str.encode("MMEMory:CATalog? '%s'" %(data_dir)))

    def setup_recall(self):
        return 0


    def data_save(self,filename):
        self.send(str.encode("MMEMory:STORe '%s\%s'" %(self.dir,filename)))



if __name__ == '__main__':
    
    exit()
    vna = VNA_Driver("10.20.175.173", 5001)

    
 