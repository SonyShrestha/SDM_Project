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
g.add((sb.BusinessInventory, RDF.type, RDFS.Class))


# Properties of class location
g.add((sb.idStore, RDF.type, RDF.Property))
g.add((sb.idStore, RDFS.domain, sb.BusinessInventory))
g.add((sb.idStore, RDFS.range, XSD.string))

g.add((sb.nameStore, RDF.type, RDF.Property))
g.add((sb.nameStore, RDFS.domain, sb.BusinessInventory))
g.add((sb.nameStore, RDFS.range, XSD.string))

g.add((sb.nameProduct, RDF.type, RDF.Property))
g.add((sb.nameProduct, RDFS.domain, sb.BusinessInventory))
g.add((sb.nameProduct, RDFS.range, XSD.string))

g.add((sb.unitPrice, RDF.type, RDF.Property))
g.add((sb.unitPrice, RDFS.domain, sb.BusinessInventory))
g.add((sb.unitPrice, RDFS.range, XSD.float))

g.add((sb.quantity, RDF.type, RDF.Property))
g.add((sb.quantity, RDFS.domain, sb.BusinessInventory))
g.add((sb.quantity, RDFS.range, XSD.float))

g.add((sb.dateManufacture, RDF.type, RDF.Property))
g.add((sb.dateManufacture, RDFS.domain, sb.BusinessInventory))
g.add((sb.dateManufacture, RDFS.range, XSD.date))

g.add((sb.dateExpiry, RDF.type, RDF.Property))
g.add((sb.dateExpiry, RDFS.domain, sb.BusinessInventory))
g.add((sb.dateExpiry, RDFS.range, XSD.date))

g.serialize(destination='./output/tbox/tbox_business_inventory.ttl', format='turtle')