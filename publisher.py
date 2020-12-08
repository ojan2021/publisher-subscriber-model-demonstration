import zmq, time
import os
import sys

print('Please provide a folder name with a full path, for example, C:\Files\docs: ')
path = input()
shortPathName = os.path.basename(path) #We shorten the whole directory name to the one folder for the sake of simplicity

context = zmq.Context()
s = context.socket(zmq.PUB)  # create a publisher socket
p = 'tcp://' + str(sys.argv[1]) + ':' + str(sys.argv[2])  # how and where to communicate
                                                          # (Program gets IP address and Port number from the user via commandline arguements
s.bind(p)  # bind socket to the address

listOfFiles = []
listOfFiles = os.listdir(path)  #List of all files and folders in the required path

while True:
    time.sleep(5)  # wait every 5 seconds
    for i in listOfFiles:
        s.send_string('Folder ' + shortPathName + ' has ' + str(i))     # Sending list of files/folders to subscriber.
    s.send_string('\n')


