import csv
import re

impact_mapping ={
    'increasing': 'increase',
    'increased': 'increase',
    'increases': 'increase',
    'decreased': 'decrease',
    'decreases': 'decrease',
    'enhanced': 'enhance',
    'reduces': 'reduce',
    'reduced': 'reduce',
    'potentiated': 'potentiate',
    'potentiates': 'potentiate',
    'caused': 'cause',



}

food_mapping = {
    'herbs and supplements with anticoagulant/antiplatelet activity': 'herb',
    'hypertensive herbs (e': 'herb',
    'excessive or chronic alcohol consumption': 'alcohol',
    'dietary avidin (a glycoprotein in uncooked egg-whites)': 'egg-whites',
    'milk and dairy products': 'dairy_products',
    'foods and supplements high in flavonoids': 'flavonoids',
    'foods high in furanocoumarins': 'furanocoumarins',
    'foods rich in citrate': 'citrate',
    'foods and supplements high in vitamin C': 'vitamin C',
    'with foods containing vitamin C': 'vitamin C',
    'the intake of phenylalanine and tyrosine': 'phenylalanine-tyrosine',
    'tyramine-containing foods and supplements': 'tyramine',
    'histamine-containing foods and supplements': 'histamine',
    'caffeine intake': 'caffeine',
    'caffeine': 'caffeine',
    "St. John's Wort": "St John's Wort",
    'calcium supplements/calcium rich foods': 'calcium',
    'iodine-containing foods and supplements': 'iodine',
    'concomitant mineral supplements': 'mineral supplements',
    'drastic dietary changes': '',
    'foods rich in vitamin K': 'vitamin K',
    'multivalent ions': 'ions',
    'high-fat meal': 'fatty food',
    'with a high fat meal': 'fatty food',
    'natural licorice': 'licorice',
    'fatty foods': 'fatty food',
    'folic acid supplement': 'folic acid',
    'a ketogenic diet': 'ketogenic diet',
    'with a light meal or snack': 'snacks'


}



def map_effect(effect):
    effects = []
    if 'myopathy' in effect:
        effects.append('myopathy')
    if 'rhabdomyolysis' in effect:
        effects.append('rhabdomyolysis')
    if effect == "d":
        return ''
    if 'sleep' in effect:
        effects.append('drowsiness')
    if 'excretion' in effect:
        effects.append('excretion')
    if 'QT' in effect:
        effects.append('QT prolongation')
    if 'potassium' in effect:
        effects.append('hyperkalemia')
    if 'adverse effects' in effect:
        effects.append('Adverse effects')
    if 'exposure to finerenone' in effect:
        effects.append('Adverse effects')
    if 'levels of cabozantinib' in effect:
        effects.append('drug concentrations')
    if 'when alcohol is ingested' in effect:
        effects.append('hypoglycemia')
    if 'actions of mecamylamine' in effect:
        effects.append('drug efficacy')
    if 'when taken with foods' in effect:
        effects.append('CALCIUM SUPPLEMENTS')
    if 'by antacid use' in effect:
        effects.append('drug absorption')
    if 'the hypokalemic effect of hydrochlorothiazide' in effect:
        effects.append('drug efficacy')
    if 'exposure to ivacaftor' in effect:
        effects.append('drug exposure')
    if 'exposure to this drug' in effect:
        effects.append('drug exposure')
    if 'systemic exposure to the drug' in effect:
        effects.append('drug exposure')
    if 'drug efficacy' in effect:
        effects.append('drug efficacy')
    if 'bone' in effect:
        effects.append('osteoporosis')
    if 'Kidney' in effect:
        effects.append('Kidney Calculi')
    if 'lithium concentrations' in effect:
        effects.append('drug concentrations')
    if 'istradefylline concentrations' in effect:
        effects.append('drug concentrations')
    if 'eliglustat' in effect:
        effects.append('drug concentrations')
    if 'levels of this medication' in effect:
        effects.append('drug concentrations')
    if 'MMAE' in effect:
        effects.append('plasma concentration')
    if 'plasma concentrations' in effect:
        effects.append('plasma concentration')
    if 'the risk of developing an ulcer' in effect:
        effects.append('ulcer')
    if 'gastrointestinal bleed' in effect:
        effects.append('Gastrointestinal Hemorrhage')
    if 'GI bleeding' in effect:
        effects.append('Gastrointestinal Hemorrhage')
    if 'osmotic demyelination syndrome' in effect:
        effects.append('osmotic demyelination syndrome')
    if 'metabolism' in effect:
        effects.append('metabolizm')
    if 'lipid' in effect:
        effects.append('blood lipid')
    if 'efficacy' in effect:
        effects.append('effectiveness')
    if 'effectiveness' in effect:
        effects.append('effectiveness')
    if 'warfarin efficacy' in effect:
        effects.append('effectiveness')
    if 'effects of alcohol' in effect:
        effects.append('alcohol effects')
    if "alcohol's effects" in effect:
        effects.append('alcohol effects')
    if "disulfiram effect" in effect:
        effects.append('alcohol effects')
    if 'aminophylline clearance' in effect:
        effects.append('serum concentration')
    if 'the clearance' in effect:
        effects.append('clearance')
    if 'glucose' in effect:
        effects.append('Glycemic Control')
    if 'Vitamin B6' in effect:
        effects.append('Vitamin B6 measurement')
    if "skin's sensitivity" in effect:
        effects.append("skin's sensitivity")
    if 'CNS stimulation' in effect:
        effects.append('Central nervous system stimulation')
    if 'CNS depressive' in effect:
        effects.append('Central Nervous System Depressants')
    if 'CNS depressant' in effect:
        effects.append('Central Nervous System Depressants')
    if 'CNS depression' in effect:
        effects.append('Central Nervous System Depressants')
    if 'CNS effects' in effect:
        effects.append('CNS effects')
    if "dose-dumping" in effect:
        effects.append("drug concentrations")
    if "uncontrolled hypertensive" in effect:
        effects.append("uncontrolled hypertension")
    if "hypertensive crisis" in effect:
        effects.append("hypertension")
    if 'anticoagulant/antiplatelet' in effect:
        effects.append('anticoagulant')
    if 'such as copper' in effect:
        effects.append('')
    if 'aluminum toxicity' in effect:
        effects.append('toxicity')
    if 'hepatoxicity' in effect:
        effects.append('hepatoxicity')
    if 'serum' in effect:
        effects.append('serum concentration')
    if 'serum' in effect:
        effects.append('serum concentration')
    if 'lisdexamfetamine elimination' in effect:
        effects.append('drug efficacy')
    if 'efficacy of mobocertinib' in effect:
        effects.append('drug efficacy')
    if 'arrhythmias' in effect:
        effects.append('cardiac Arrhythmia')
    if 'ability to detect ischemic changes' in effect:
        effects.append('ischemic changes')
    if 'caused by' in effect:
        effects.append('')
    if 'sedative' in effect:
        effects.append('Sedation procedure')
    if 'sedation' in effect:
        effects.append('Sedation procedure')
    if 'vasodilatory' in effect:
        effects.append('Vasodilator Agents')
    if 'myalgia' in effect:
        effects.append('myalgia')
    if 'drug concentrations' in effect:
        effects.append('drug concentrations')
    if 'ketoconazole concentrations' in effect:
        effects.append('drug concentrations')
    if 'eliglustat' in effect:
        effects.append('drug concentrations')
    if 'effects of melatonin' in effect:
        effects.append('drug efficacy')
    if 'additive effect' in effect:
        effects.append('additive drug effects')
    if 'signs and symptoms of overdose' in effect:
        effects.append('additive drug effects')
    if 'absorption' in effect:
        effects.append('drug Absorption')
    if 'insulin' in effect:
        effects.append('insulin')
    if 'drowsiness' in effect:
        effects.append('drowsiness')
    if 'somnolence' in effect:
        effects.append('drowsiness')
    if 'dizziness' in effect:
        effects.append('dizziness')
    if 'tachycardia' in effect:
        effects.append('tachycardia')
    if 'hypotension' in effect:
        effects.append('hypotension')
    if 'hypertension' in effect:
        effects.append('hypertension')
    if 'significant elevation in blood pressure' in effect:
        effects.append('hypertension')
    if 'bioavailability' in effect:
        effects.append('Biological Availability')
    if 'high-fat' in effect:
        effects.append('Biological Availability')
    if 'bleeding' in effect:
        effects.append('Hemorrhage')
    if 'flushing' in effect:
        effects.append('flushing')
    if 'gastric' in effect:
        effects.append('Gastric irritation')
    if 'gastrointestinal' in effect:
        effects.append('Gastrointestinal irritation')
    if 'birth' in effect:
        effects.append('Congenital Abnormality')
    if 'kidney' in effect:
        effects.append('Kidney Calculi')
    if 'nausea' in effect:
        effects.append('nausea')
    if 'vomiting' in effect:
        effects.append('vomiting')
    if 'sweating' in effect:
        effects.append('sweating')
    if 'palpitations' in effect:
        effects.append('palpitations')
    if 'headaches' in effect:
        effects.append('headaches')
    if 'with excess/chronic alcohol consumption' in effect:
        effects.append('pancreatitis')
    if 'AUC' in effect:
        effects.append('Area Under Curve')
    if 'this infection' in effect:
        effects.append('chronic hepatitis C')
    if 'liver' in effect:
        effects.append('liver injury')
    if 'when taken with foods' in effect:
        effects.append('drug Absorption')
    if 'chance of flushing and pruritus' in effect:
        effects.append('pruritus')
    if 'dose of ponatinib' in effect:
        effects.append('')
    if 'by the co-administration of alcohol' in effect:
        effects.append('')
    if 'by co-administration with alcohol' in effect:
        effects.append('')
    if 'levels of both iron and acetohydroxamic acid' in effect:
        effects.append('acetohydroxamic acid')
    if 'risk of serious side effects' in effect:
        effects.append('Adverse effects')

    if 'risk of' in effect:
        effects.append(re.search(r'risk of (\w+)', effect).group(1))
    if 'risk for' in effect:
        effects.append(re.search(r'risk for (\w+)', effect).group(1))
    if not effects:
        effects.append(re.sub(r'^(the|a)\s', '', effect))

    return effects



with open('extracted_patterns1.csv', 'r', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    fieldnames = ['Drug ID', 'Drug Label', 'Interaction', 'Food', 'Impact', 'Effect']

    
    with open('extracted_patterns2.csv', 'w', newline='', encoding='utf-8') as newcsvfile:
        writer = csv.DictWriter(newcsvfile, fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            food = row['Food']

            if food in food_mapping:
                food = food_mapping[food]

            impact = row['Impact']

            if impact in impact_mapping:
                impact = impact_mapping[impact]

            effects = map_effect(row['Effect'])

            for effect in effects:
                writer.writerow({
                    'Drug ID': row['Drug ID'],
                    'Drug Label': row['Drug Label'],
                    'Interaction': row['Interaction'],
                    'Food': food,
                    'Impact': impact,
                    'Effect': effect
                })

print("Extraction and transformation completed successfully.")



