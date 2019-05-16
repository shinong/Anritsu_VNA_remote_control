import socket

def general_setup(setup_dir,data_dir):
    vna.send(str.encode("TST?\n"))
    reply = vna.recv(2056)
    if (not reply):
        print('selftest passed')
    else: 
        print('error')
        exit()
    
    vna.send(str.encode("SYSTem:ERRor:CLEar"))
    vna.send(str.encode("DISPlay:COLor:RESet"))
    vna.send(str.encode("DISPlay:COUNT 1"))
    vna.send(str.encode("CALCulate:PARameter:COUNT 1"))
    vna.send(str.encode("DISPlay:WINDow1:SPLit R1C1"))
    vna.send(str.encode("DISPlay:WINDow1:ACTivate 1"))
    vna.send(str.encode("DISPlay:SIZe MAXimum"))
    vna.send(str.encode("CALCulate:PARameter1:DEFine S11"))
    vna.send(str.encode("CALCulate:PARameter1:FORMat MLOGarithmic"))

    vna.send(str.encode("MMEMory:CATalog? '%s'" %(setup_dir)))
    vna.send(str.encode("MMEMory:CATalog? '%s'" %(data_dir)))


def sweep_setup(f_begin,f_stop,points):
    vna.send(str.encode("SENS:FREQ:STAR %d\n" %(f_begin*1E9)))
    vna.send(str.encode("SENS:FREQ:STOP %d\n" %(f_begin*1E9)))
    vna.send(str.encode("SENS:SWEEP:TYPe LINear\n"))
    vna.send(str.encode("SENS:SWEEP:POINTS %d\n" %(points)))
    #vna.send(str.encode("SENS:BAND 70E1\n"))

    #vna.send(str.encode("CALCulate1:PARameter4:FORMat SMITh\n"))

def setup_recall(path):
    return 0


def data_save(dir,filename):
    vna.send(str.encode("MMEMory:STORe '%s\%s'" %(dir,filename)))


exit()

if __name__ == '__main__':
    vna = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    vna.connect(("10.20.175.173", 5001))
    print ('hello world')