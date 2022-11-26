from rdflib import Graph, Literal, RDF, URIRef
# rdflib knows about quite a few popular namespaces, like W3C ontologies, schema.org etc.
from rdflib.namespace import FOAF , XSD

from rdflib.namespace import NamespaceManager
from rdflib import BNode 


# Create a Graph function
# v namespece is the service namespace
# v ms_name is the service name
# v description
# v ms_type [data loading, data clearning, data trasnfer, data scaling, ... machine learning model,  visulaisation]
# v dependencies is the library
# v framework is the programming framework
# v GPU is indicate if the GPU is required 0 no, 1 yes
# x pipeline is the microservices composition process of this service. IF = 0, then this is atom service. IF != 0, then the pipleline
# is also a two demotional dictionary with step number and service dictionary. The inner service dictionary contains 
# service name and service type and category. The service name is optional but if it is empty, then automatic composition 
# process will start  
# v model_format is the model save formation e.g. h5 that can be invoked 
# v invoke_uri 
# v input_sp 1 presents data, 2 presents image, 3 presents text, 4 presents othertype and 5 presents any 
# v output_sp
# v contributor is which organisation or individul or groups developed this model
# v licence
# v service_category [linearRegression, ... logitstic regression, ... CNN] 

component = './flaskInterface/components/'

def create_services(service):
    services.append(service)
    return services

def create_pipeline(services):
    pipeservices = {}
    i=0
    for ise in services: 
        pipeservices.update({i:ise})
        i=i+1
    return pipeservices

def create_dependencies(requirements):
    dependencies= requirements
    return dependencies

def create_parameters(parameter):
    paramenterslist.append(parameter)
    return parameterslist

def Create_output_spec(outputtxt):
    outputlist={}
    i=0
    for ox in outputtxt:
        output_x = ox.split('.')
        outputlist[i] = output_x 
        i=i+1
    return outputlist

def Create_input_spec(inputtxt):
    inputlist={}
    i=0
    for ix in inputtxt:
        input_x = ix.split('.')
        inputlist[i] = input_x 
        i=i+1
    return inputlist


def greateMSGraph(namespace,ms_name, description, ms_type, dependencies, framework, GPU, pipeline, model_format, input_sp, output_sp, contributor, licence, service_category):
    # need to check names before start but this is future work
    g = Graph()
    g.parse(component+"registry.n3")
    if len(ms_name) > 0 and len(ms_type) > 0 and len(dependencies)> 0: 
        #subject
        MService = URIRef(namespace+'/'+ms_name)
        #object
        _type = URIRef(namespace+'/'+ms_type)
        _contributor = URIRef(contributor)
        _lic = URIRef(licence)
        _sc = URIRef(namespace+'/'+service_category)
        print(_sc)
        #verb
        has_framework = URIRef(namespace+'/framwork')
        has_contributor = URIRef(namespace+'/contributor')
        has_licence = URIRef(namespace+'/licence')
        has_category = URIRef(namespace+'/category')
        has_dep = URIRef(namespace+'/dependency')
        service_uri = URIRef(namespace+'/uri')
        uses = URIRef(namespace+'/uses')
        has_format = URIRef(namespace+'/formate')
        has_pipeline = URIRef(namespace+'/pipe')
        has_input = URIRef(namespace+'/input')
        has_output = URIRef(namespace+'/output')
        has_ioct = URIRef(namespace+'/iocategory')
        has_iodt = URIRef(namespace+'/iodatatype')
        has_ioshape = URIRef(namespace+'/ioshape')
        has_description = URIRef(namespace+'/description')
        has_paramter = URIRef(namespace+'/paramter')
        has_paramter_id = URIRef(namespace+'/pid')
        #triples
        g.add((MService, has_description, Literal(description,lang="en")))
        g.add((MService, RDF.type, _type))
        g.add((MService, has_framework, Literal(framework,lang="en")))
        g.add((MService, has_contributor, _contributor))
        g.add((MService, has_licence, _lic))
        g.add((MService, has_category, _sc))
        g.add((MService, service_uri, URIRef(MService)))
        g.add((MService, has_format, Literal(model_format,lang="en")))
        if GPU==1:
            g.add((MService, uses, Literal('gpu',lang="en")))
        for d in dependencies:
            g.add((MService, has_dep, Literal(d,lang="en")))
        
        if pipeline != 0:
            for x in pipeline:
                g.add((MService, has_pipeline, Literal(x,lang="en")))
        if bool(input_sp):        
            _input = BNode()
            g.add((MService, has_input, _input))
            i=0
            for x in input_sp: 
                _inputp = BNode()
                g.add((_input, has_paramter, _inputp))
                g.add((_inputp, has_paramter_id, Literal(str(i),lang="en")))
                i=i+1
                if len(input_sp[x])>0:
                    g.add((_inputp, has_ioct, URIRef(namespace+'/'+input_sp[x][0])))
                if len(input_sp[x])>1:
                    g.add((_inputp, has_iodt, URIRef(namespace+'/'+input_sp[x][1])))
                if len(input_sp[x])>2:
                    g.add((_inputp, has_ioshape, Literal(input_sp[x][2],lang="en")))
        if bool(output_sp):        
            _output = BNode()
            g.add((MService, has_output, _output))
            i=0
            for x in output_sp:
                _outputp = BNode()
                g.add((_output, has_paramter, _outputp))
                g.add((_outputp, has_paramter_id, Literal(str(i),lang="en")))
                i=i+1
                if len(output_sp[x])>0:
                    g.add((_outputp, has_ioct, URIRef(namespace+'/'+output_sp[x][0])))
                if len(output_sp[x])>1:
                    g.add((_outputp, has_iodt, URIRef(namespace+'/'+output_sp[x][1])))
                if len(output_sp[x])>2:
                    g.add((_outputp, has_ioshape, Literal(output_sp[x][2],lang="en")))
        g.serialize(destination=component+'registry'+".n3")
        