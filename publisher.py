import zmq, time
import os

print('Please provide a folder name with a full path, for example, C:\Files\docs: ')
path = input()
shortPathName = os.path.basename(path)

context = zmq.Context()
s = context.socket(zmq.PUB)  # create a publisher socket
p = 'tcp://' + '192.168.0.105' + ':' + '8888'  # how and where to communicate
s.bind(p)  # bind socket to the address

listOfFiles = []
listOfFiles = os.listdir(path)

while True:
    time.sleep(5)  # wait every 5 seconds
    for i in listOfFiles:
        s.send_string('Folder ' + shortPathName + ' has ' + str(i))


