import subprocess
import shlex
import sys

def GetLiveOutputFromProcess_WhileRunning(cmd):
    '''
    Get the live output from the process while its running
    '''
    arg = shlex.split('python test.py')
    proc = subprocess.Popen(arg,shell=True,bufsize=1024,stderr=subprocess.PIPE,stdout=subprocess.PIPE)
    
    outputs = []
    while True:
        #stdout,stderr = proc.communicate() -> this is sync so i avoided it
        
        bufferReader = proc.stdout
        #sys.stdout.flush()
        
        if proc.poll() == None:
            if proc.stdout != None:
                outputs.append(bufferReader.read(1024).decode().strip("\n"))
                sys.stdout.flush()
                print(bufferReader.read(1024).decode().strip("\n"))
                sys.stdout.flush()
        else:
            break # terminated

    print("process terminated")
    return outputs

if __name__ == '__main__':
    outs = GetLiveOutputFromProcess_WhileRunning('python infinite_printer.py')
    print(outs) # Only get executed once the process terminated. Live stdout data will be always printed by 'GetLiveOutputFromProcess_WhileRunning'
