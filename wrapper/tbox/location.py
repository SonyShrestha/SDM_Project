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
g.add((sb.Location, RDF.type, RDFS.Class))


# Properties of class location
g.add((sb.idLocation, RDF.type, RDF.Property))
g.add((sb.idLocation, RDFS.domain, sb.Location))
g.add((sb.idLocation, RDFS.range, XSD.string))

g.add((sb.countryCode, RDF.type, RDF.Property))
g.add((sb.countryCode, RDFS.domain, sb.Location))
g.add((sb.countryCode, RDFS.range, XSD.string))

g.add((sb.postalCode, RDF.type, RDF.Property))
g.add((sb.postalCode, RDFS.domain, sb.Location))
g.add((sb.postalCode, RDFS.range, XSD.string))

g.add((sb.place_name, RDF.type, RDF.Property))
g.add((sb.place_name, RDFS.domain, sb.Location))
g.add((sb.place_name, RDFS.range, XSD.string))

g.add((sb.latitude, RDF.type, RDF.Property))
g.add((sb.latitude, RDFS.domain, sb.Location))
g.add((sb.latitude, RDFS.range, XSD.string))

g.add((sb.lontitude, RDF.type, RDF.Property))
g.add((sb.lontitude, RDFS.domain, sb.Location))
g.add((sb.lontitude, RDFS.range, XSD.string))


g.serialize(destination='./output/tbox/tbox_location.ttl', format='turtle')