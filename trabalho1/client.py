import rpyc
import sys
from time import time

def create_array(length):
   return list(i for i in range(length))

def call_exposed_function_and_variable(connection):
   print(connection.root.get_answer())
   print(connection.root.the_real_answer_though)

def try_unexposed_function(connection):
   print(connection.root.get_question())

def call_arraysum_function(connection, length):
   start = time()
   array = create_array(length)
   print(connection.root.sum_array(array))
   end = time()
   print("Tempo de execução no cliente: {}s".format(end-start))

if __name__ == "__main__":
   if len(sys.argv) < 2:
      exit("Usage {} SERVER".format(sys.argv[0]))
   
   server = sys.argv[1]
   
   connection = rpyc.connect(server,18861)
   # call_exposed_function_and_variable(connection)
   try_unexposed_function(connection)
   # call_arraysum_function(connection, 10000)
   