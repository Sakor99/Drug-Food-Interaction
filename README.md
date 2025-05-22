# Drug-Food Interaction

This project extracts and semantically models **drug-food interactions** using data sourced from **DrugBank**. It processes natural language interaction descriptions, links terms to biomedical ontologies via **BioFalcon**, and generates a structured RDF-based **Knowledge Graph** of interactions, drugs, foods, effects, impacts, and recommendations.

---

##  Project Workflow

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
├── drugBank_drug_food_interactions.csv  # Raw interaction data from DrugBank (downloaded on Feb 28, 2024)
│
├── Mapping/                            # RDF mapping files and outputs
│   ├── *.ttl                           # Mapping templates (e.g., DrugMapping.ttl)
│   ├── *.nt                            # RDF output files
│   └── config.txt                      # Mapping configuration
│
├── error.log                           # Processing error logs
└── .idea/                              # PyCharm IDE metadata (can be ignored)
```
## 🛠️ Requirements

- Python 3.7+
- `fuzzywuzzy`
- `pandas`
- **BioFalcon API Access**  
  (Make sure to include `.env` or credentials if required for BioFalcon access.)

Install required packages:

```bash
pip install -r requirements.txt
```

If requirements.txt is missing, install manually:
```bash
pip install pandas fuzzywuzzy python-Levenshtein
```
## Usage

1. **Start by extracting interactions**

```bash
python main.py
```

2. **Process multiple-interaction entries**

```bash
python "extracting the Inter has more than one DFI.py"
```

3. **Normalize and prepare terms**

```bash
python dictionary.py
```

4. **Link terms with UMLS using BioFalcon**

```bash
python "BioFalcon linking.py"
```

5. **Refine matches using fuzzy similarity**

```bash
python "compare similarity.py"
```

6. **Extract only recommendation-based interactions**

```bash
python recommendations.py
```

7. **Generate RDF triples with mappings**

Use [SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer) or similar tools to apply `.ttl` mapping files and produce `.nt` RDF outputs.

##  Output

After processing, RDF triples representing **drugs, foods, effects, impacts**, and their interactions will be available in `.nt` format under the `Mapping/` folder. These triples can be used for semantic reasoning, knowledge graph exploration, or querying with SPARQL.

---

##  References

- **DrugBank**: [https://go.drugbank.com/](https://go.drugbank.com/)
- **BioFalcon**: [https://labs.tib.eu/sdm/biofalcon](https://labs.tib.eu/sdm/biofalcon/api?mode=short)
- **UMLS Metathesaurus**: [https://www.nlm.nih.gov/research/umls/index.html](https://www.nlm.nih.gov/research/umls/index.html)
- **SDM-RDFizer**: [https://github.com/SDM-TIB/SDM-RDFizer](https://github.com/SDM-TIB/SDM-RDFizer)

---

##  Acknowledgements

This work was developed as part of the [P4-LUCAT](https://www.tib.eu/de/forschung-entwicklung/projektuebersicht/projektsteckbrief/p4-lucat) project, within a research workflow for semantic enrichment of biomedical data.

