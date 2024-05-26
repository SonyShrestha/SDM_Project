from rdflib import Graph, Namespace, URIRef, Literal
from rdflib.namespace import RDF, RDFS, XSD

# Define namespaces
xsd = Namespace("http://www.w3.org/2001/XMLSchema#")
rdf = Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")
rdfs = Namespace("http://www.w3.org/2000/01/rdf-schema#")
sb = Namespace("http://www.example.edu/spicy_bytes/")

# Create an empty graph
g = Graph()

# Add triples to the graph
g.add((sb.CustomerInventory, RDF.type, RDFS.Class))


# Properties of class location
g.add((sb.idCustomer, RDF.type, RDF.Property))
g.add((sb.idCustomer, RDFS.domain, sb.CustomerInventory))
g.add((sb.idCustomer, RDFS.range, XSD.string))

g.add((sb.nameCustomer, RDF.type, RDF.Property))
g.add((sb.nameCustomer, RDFS.domain, sb.CustomerInventory))
g.add((sb.nameCustomer, RDFS.range, XSD.string))

g.add((sb.nameProduct, RDF.type, RDF.Property))
g.add((sb.nameProduct, RDFS.domain, sb.CustomerInventory))
g.add((sb.nameProduct, RDFS.range, XSD.string))

g.add((sb.unitPrice, RDF.type, RDF.Property))
g.add((sb.unitPrice, RDFS.domain, sb.CustomerInventory))
g.add((sb.unitPrice, RDFS.range, XSD.float))

g.add((sb.quantity, RDF.type, RDF.Property))
g.add((sb.quantity, RDFS.domain, sb.CustomerInventory))
g.add((sb.quantity, RDFS.range, XSD.float))

g.add((sb.datePurchased, RDF.type, RDF.Property))
g.add((sb.datePurchased, RDFS.domain, sb.CustomerInventory))
g.add((sb.datePurchased, RDFS.range, XSD.date))

g.serialize(destination='./output/tbox/tbox_customer_inventory.ttl', format='turtle')