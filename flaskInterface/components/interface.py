import sys  
import os
sys.path.insert(0, '')
import agent as ai
from rdflib import Graph, Literal, RDF, URIRef
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import FOAF , XSD
from rdflib.namespace import NamespaceManager


#we wont be using this file  anylonger because  we are no longer using the terminal for input but a user interface 

ai.reset_knowledge()



taskname = input("Enter task name:")
print("taskname is: " + taskname)

data = input("Enter data path:")
print("data is: " + data)

desire = input("Enter desire output:")
print("desire output is: " + desire)

domain = input("Enter problem domain (optional):")
print("desire output is: " + domain)

category = input("Enter AI task category (optional):")
print("desire output is: " + category)

print('Calling the agent to search a solution for you now...')

ai.output_memery={}
ai.servicelist=[]

value = ai.OperatingTask (taskname,data,[desire],domain,'',category)
#'task1','heart.csv',['pipeline'],'medical','','MLmodel_classification'
