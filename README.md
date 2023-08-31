# Coronavirus Knowledge Graph (CovKG)

The Coronavirus Knowledge Graph (CovKG) is a comprehensive biological knowledge graph for coronavirus, relating diseases, virus, drugs, genes, molecular function, etc. CovKG includes information from existing databases such as UMLS, DrugBank, Gene Ontology, and data collected from literature related to coronavirus. CovKG contains 17,369,620 triples, covering 13,065 concepts 209 semantic types, and 97 semantic relations. 
![image](https://github.com/loupei/CovKG/blob/main/figure.jpg)
Figure. The main schema of CovKG with the integration of multi-source biomedical knowledge. PubMedAnn: the biomedical literature knowledge base of coronavirus. GO: Gene Ontology.

## CovKG dataset

The whole dataset contains two parts:
* `pubmedann_rdf.zip`: PubMedAnn includes 18,687 coronavirus-related biomedical literature published between January 2000 and June 2022. The pubmedann_rdf file is generated through semantic structure conversion.
* `experiment_data.zip`: Contains the data of entities, relations, and triples used for the experiment.

## Model

### PubMedAnn construction

* `semantic_conversion_model.py`: A tool that organizes triples extracted from PubMed literature and converts them into RDF format for storage.

### Pretrained CovKG embedding

Six KG embedding models are explored to predict potential targets and candidate drugs to repurpose for coronavirus. Among them, TransR performed the best in translational models, and RESCAL performed the best in semantic matching models. The entity embedding and relation embedding can be loaded separately with np.load.  
* `TransR_entity.npy`: NumPy binary data, storing the entity embedding.  
* `TransR_relation.npy`: NumPy binary data, storing the relation embedding.  
*	`RESCAL_entity.npy`: NumPy binary data, storing the entity embedding.  
* `RESCAL_relation.npy`: NumPy binary data, storing the relation embedding.  

### Semantic reasoning

* `SPARQL.txt`: An example of SPARQL query and logic reasoning statements for drugs and targets across heterogeneous databases.  

## Result

* `result_linkpredict.xlsx`: The link prediction results.  
*	`result_sim.xlsx`: The drug similarity calculation results.

## Cite

Please cite our dataset if you use this code and data in your work.  
```
  @misc{CovKG2023,  
    author = {Pei Lou, An Fang, Wanqing Zhao, Kuanda Yao, Yusheng Yang, Jiahui Hu},  
    title = {Potential Target Discovery and Drug Repurposing for Coronavirus: A Knowledge Graph-Based Approach},  
    howpublished = "\url{https://github.com/loupei/CovKG}",  
    year = {2023}  
  }
```
