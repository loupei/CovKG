import re
from rdflib import Graph, Literal, RDF, URIRef

#  Create an empty graph
g = Graph()

# URIRef creates a URI link, and Literal creates a literal
relation_hascui=URIRef("http://www.imicams.ac.cn/pmd-cov-kg#hascui")
relation_haslabel=URIRef("http://www.imicams.ac.cn/pmd-cov-kg#haslabel")
relation_hastext=URIRef("http://www.imicams.ac.cn/pmd-cov-kg#hastext")
relation_hasannotation=URIRef("http://www.imicams.ac.cn/pmd-cov-kg#hasannotation")
relation_hasurl=URIRef("http://www.imicams.ac.cn/pmd-cov-kg#hasurl")
relation_cui2label=URIRef("http://www.imicams.ac.cn/pmd-cov-kg#cui2label")
relation_hassemantic=URIRef("http://www.imicams.ac.cn/pmd-cov-kg#hassemantic")

content = open(":\.nt",'r',encoding="utf-8").readlines()

for i in content:

    if "-----" in i:
        citation=re.findall('Citation (\d+)', i)
        citation_str = "".join(citation)

    elif "|relation|" in i:
        pattern1=re.findall('(.*?)\|relation\|(C\d+)\|(.*?)\|(.*?)\|.*\|(.*?)\|(C\d+)\|(.*?)\|(.*?)\|', i)
        for j in pattern1:
            
            # Adds a triplet to the graph
            cui1 = j[1]
            entity=j[0]
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+entity), relation_hascui, (URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+cui1))))
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+citation_str), relation_hasannotation, URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + entity)))
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+cui1), relation_hasurl, Literal("http://linkedlifedata.com/resource/umls/id/" + cui1)))

            cui2 = j[5]
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+entity), relation_hascui, (URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+cui2))))
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+citation_str), relation_hasannotation, URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + entity)))
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+cui2), relation_hasurl, Literal("http://linkedlifedata.com/resource/umls/id/" + cui2)))

            label1 = j[2]
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+entity), relation_haslabel, Literal(label1)))
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+citation_str), relation_hasannotation, URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + entity)))

            label2 = j[6]
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+entity), relation_haslabel, Literal(label2)))
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+citation_str), relation_hasannotation, URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + entity)))

            label3 = j[4]
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + cui1), URIRef("http://www.relationc.lp/KG#hasrelation/" + label3),URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + cui2)))

            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + cui1), relation_cui2label,Literal(label1)))
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + cui2), relation_cui2label,Literal(label2)))

            label4 = j[3]
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + cui1), relation_hassemantic,Literal(label4)))

            label5 = j[7]
            g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/" + cui2), relation_hassemantic, Literal(label5)))

            
            print(cui1, cui2, label1, label2,label3)

    else:

        pattern2 = re.findall('(\d+.(?:ti|ab)+.\d+)', i)
        pattern2_str="".join(pattern2)
        g.add((URIRef("http://www.imicams.ac.cn/pmd-cov-kg/"+pattern2_str), relation_hastext, Literal(i)))
        

# A triple traversal graph output
print("--- printing raw triples ---")
for s, p, o in g:
    print((s, p, o))
# Serializing the map in N3 format
print("--- printing mboxes ---")
print(g.serialize(format='nt11'))

with open(":\.nt",'w',encoding="utf-8") as f:
    f.write(g.serialize(format='nt'))
