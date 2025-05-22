# Drug-Food Interaction

This project extracts and semantically models **drug-food interactions** using data sourced from **DrugBank**. It processes natural language interaction descriptions, links terms to biomedical ontologies via **BioFalcon**, and generates a structured RDF-based **Knowledge Graph** of interactions, drugs, foods, effects, impacts, and recommendations.

---

## 🚀 Project Workflow

1. **Data Extraction**  
   - The CSV file `drugBank_drug_food_interactions.csv` contains raw interaction descriptions from DrugBank.
   - `main.py` processes the CSV file and extracts relevant terms (drugs, foods, effects, impacts, interactions).
   - `extracting the Inter has more than one DFI.py` handles cases where multiple DFIs are embedded in a single entry.

2. **Term Normalization**  
   - `dictionary.py` is used to normalize extracted terms (e.g., converting "increased", "increasing" → "increase").

3. **Entity Linking to UMLS**  
   - `BioFalcon linking.py` uses **BioFalcon** to link each term to its UMLS Concept Unique Identifier (CUI).
   - `compare similarity.py` applies fuzzy matching (`fuzzywuzzy`) to improve label alignment with UMLS terms.

4. **Recommendation Extraction**  
   - `recommendations.py` filters out and extracts only the interaction texts that are **explicit recommendations**.

5. **Semantic Mapping to RDF**  
   - RDF/Turtle mapping files in the `Mapping/` directory define rules to convert processed CSV files into RDF triples (`.nt` format).
   - Output `.nt` files represent the semantic **Knowledge Graph**, suitable for querying and reasoning.

---

## 🧾 Repository Structure

```plaintext
Drug-Food-Interaction-main/
│
├── main.py                             # Extracts data from DrugBank CSV
├── extracting the Inter has more than one DFI.py  # Handles multiple DFIs in one entry
├── dictionary.py                       # Normalizes terms to avoid duplicates
├── BioFalcon linking.py               # Links terms to UMLS using BioFalcon
├── compare similarity.py              # Matches terms using fuzzy similarity
├── recommendations.py                 # Extracts recommendation-based interactions
│
├── drugBank_drug_food_interactions.csv  # Raw interaction data from DrugBank
│
├── Mapping/                            # RDF mapping files and outputs
│   ├── *.ttl                           # Mapping templates (e.g., DrugMapping.ttl)
│   ├── *.nt                            # RDF output files
│   └── config.txt                      # Mapping configuration
│
├── error.log                           # Processing error logs
└── .idea/                              # PyCharm IDE metadata (can be ignored)
