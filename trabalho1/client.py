import rpyc
import sys

def create_array(length):
   return list(i for i in range(length))

if len(sys.argv) < 2:
   exit("Usage {} SERVER".format(sys.argv[0]))
 
server = sys.argv[1]
 
connection = rpyc.connect(server,18861)

print(connection.root)
print(connection.root.sum_array(create_array(10000))) #chamada pro método de somar um array
print(connection.root.get_answer())
print(connection.root.the_real_answer_though)