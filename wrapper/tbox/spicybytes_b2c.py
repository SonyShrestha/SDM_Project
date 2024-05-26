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
g.add((sb.BusinessPurchase, RDF.type, RDFS.Class))


# Properties of class location
g.add((sb.idBuyer, RDF.type, RDF.Property))
g.add((sb.idBuyer, RDFS.domain, sb.BusinessPurchase))
g.add((sb.idBuyer, RDFS.range, XSD.string))

g.add((sb.idSeller, RDF.type, RDF.Property))
g.add((sb.idSeller, RDFS.domain, sb.BusinessPurchase))
g.add((sb.idSeller, RDFS.range, XSD.string))

g.add((sb.nameProduct, RDF.type, RDF.Property))
g.add((sb.nameProduct, RDFS.domain, sb.BusinessPurchase))
g.add((sb.nameProduct, RDFS.range, XSD.string))

g.add((sb.unitPrice, RDF.type, RDF.Property))
g.add((sb.unitPrice, RDFS.domain, sb.BusinessPurchase))
g.add((sb.unitPrice, RDFS.range, XSD.float))

g.add((sb.quantity, RDF.type, RDF.Property))
g.add((sb.quantity, RDFS.domain, sb.BusinessPurchase))
g.add((sb.quantity, RDFS.range, XSD.float))

g.add((sb.datePurchase, RDF.type, RDF.Property))
g.add((sb.datePurchase, RDFS.domain, sb.BusinessPurchase))
g.add((sb.datePurchase, RDFS.range, XSD.date))

g.serialize(destination='./output/tbox/tbox_spicybytes_b2c.ttl', format='turtle')