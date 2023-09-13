import rpyc
import sys
 
if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
 
connection = rpyc.connect(server,18861)

print(connection.root)
print(connection.root.get_answer())
print(connection.root.the_real_answer_though)