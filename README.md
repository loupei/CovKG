# Coronavirus Knowledge Graph (CovKG)

The Coronavirus Knowledge Graph (CovKG) is a comprehensive biological knowledge graph relating diseases, virus, drugs, genes, molecular function, etc. CovKG includes information from existing databases such as UMLS, DrugBank, Gene Ontology, and data collected from literature related to coronavirus. CovKG contains 17,369,620 triples covering 13,065 concepts belonging to 209 semantic types and 97 semantic relations. We present the main schema of CovKG and integrate the knowledge from multiple sources.
![image](https://github.com/loupei/CovKG/blob/main/figure.jpg)
Figure. The main schema of CovKG with the integration of multi-source biomedical knowledge. PubMedAnn: the biomedical literature knowledge base of coronavirus.
GO: Gene Ontology.

## CovKG dataset

pubmedann_rdf.zip, PubMedAnn includes 18,687 coronavirus-related biomedical literature published between January 2000 and June 2022.   
experiment_data.zip, contains the entities, relations, and triples used for the experiment.

## Model

### PubMedAnn construction

semantic_conversion_model.py, a tool that organizes triples extracted from PubMed literature and converts them into RDF format for storage.

### Pretrained CovKG embedding

CovKG embeddings are trained using 6 models. Among them, TransR performed the best in translational models, and RESCAL performed the best in semantic matching models. Four files are provided. one can use np.load to load the entity embeddings and relation embeddings separately:  
TransR_entity.npy, NumPy binary data, storing the entity embedding.  
TransR_relation.npy, NumPy binary data, storing the relation embedding.  
RESCAL_entity.npy, NumPy binary data, storing the entity embedding.  
RESCAL_relation.npy, NumPy binary data, storing the relation embedding.  

### Semantic reasoning

SPARQL.txt, the SPARQL code used to retrieve the graph database.  

## Result
result_linkpredict.xlsx, the link prediction results.  
result_sim.xlsx, the drug similarity calculation results.

