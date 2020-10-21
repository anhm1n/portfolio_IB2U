# Author: Anh-Minh Nguyen
# Date: 05/03/2020

# biobash
biobash <- function(x) {
  #
  # weakness/asthenia not classified
  if(x %in% c('General weakness','Weakness','Asthenia', 'Muscle weakness')) {
    return('Weakness/Asthenia')
    # Don't need Labored respiration
    # Air hunger don't include
    # Difficulty period referring to period 
    # Exertional dyspnea don't include 
  } else if(x %in% c('Shortness of breath', 'Dyspnea', 'Dyspnoea',
                     'Paroxysmal nocturnal dyspnea', 'Nocturnal dyspnea', 
                     'Dyspnea on exertion', 'Difficulty breathing','Labored breathing')) {
    return('Shortness of breath/Dyspnea')
    # Don't include facial swelling
    # Edema located under perinatal
    # Can include ankle swelling and leg swelling
    # Don't include dependent edema
    # Not fluid overload
  } else if(x %in% c('Ankle swelling', 'Swollen feet', 'Pedal edema', 
                     'Edema', 'Oedema','Fluid retention', 'Swelling')) {
    return('Edema/Swelling') 
    # Confusional State is a mental illness, don't include
  } else if(x %in% c('Confusion', 'Delirium', 'Confused')) {
    return('Confusion/Delirium')
    # Complicated/most controversial
    # Arrhythmia not classified
  } else if(x %in% c('Irregular heart beat', 'Irregular heart rate', 'Arrhythmia', 
                     'Cardiac arrhythmia','Cardiac arrhythmias', 'Abnormal heart beat', 
                     'Palpitations')) {
                     #'Rapid heart beat', 'Tachycardia', 'Bradyarrhythmia',
                     #'Ventricular arrhythmia', 'Atrial arrhythmia', 'Tachyarrhythmia',
                     #'Atrial tachycardia', 'Ventricular tachycardia', 'Bradycardia',
                     #'Paroxysmal tachycardia', 'Paroxysmal supraventricular tachycardia',
                     #'Paroxysmal ventricular tachycardia', 'Paroxysmal atrial tachycardia',
                     #'Supraventricular tachycardia', 'Rapid atrial fibrillation',
                     #'Paroxysmal atrial tachycardia', 'Paroxysmal atrial flutter',
                     #'Paroxysmal atrial fibrillation', 'Atrial fibrillation', 
                     #'Atrial dysrhythmia', 'Ventricular dysrhythmia', 
                     #'Nonsustained ventricular tachycardia')) {
    return('Irregular heartbeat/Palpitations')
    # Muscle fatigue != fatigue
    # Don't include loss of energy, not specific
    # ICD classififes lethargy as fatigue
    # Loss of energy/Lethargic not classified
    # Tired is classified under something else
  } else if(x %in% c('Fatigue', 'Fatigability', 'Exhaustion', 'Extreme exhaustion',
                     'Lack of energy', 'Lethargy', 'Lethargic', 'Loss of energy')) {
    return('Fatigue/Lethargy')
    # Itching is pruritus under ICD
    # Itch/Itchy not classififed
    # Don't include pruritic rash
  } else if(x %in% c('Itching', 'Itch', 'Itchy', 'Pruritus')) {
    return('Pruritus/Itchiness')
    # Cramping/twitch not classififed: Crampy, twitching, muslce spasm
    # Removed Cramping pain
  } else if(x %in% c('Muscle cramps', 'Cramping', 'Crampy', 'Spasm', 
                     'Muscle twitching', 'Muscle twitch', 'Twitch', 'Muscle Spasm',
                     'Twitching')) {
    return('Cramping/Twitching/Spasm')
    # Nauseated/Nauseous not classified
  } else if(x %in% c('Nausea', 'Nauseated', 'Nauseous')) {
    return('Nausea')
    # Bilious vomiting/emesis != vomiting
    # Don't include coffee ground emesis
    # Hyperemesis != emesis (for babies)
  } else if(x %in% c('Vomiting','Vomit',
                     'Throwing up', 'Emesis')) {
    return('Vomiting/Emesis')
    # INTERESTING ANOREXIA NOT CLASSIFIED AS ANOREXIA??!
  } else if(x %in% c('Loss of appetite', 'Anorexia', 'Anorexic')) {
    return('Loss of appetite/Anorexia')
  } else if(x %in% c('Chest pain', 'Chest wall pain', 'Pleuritic chest pain', 
                     'Pressure in chest', 'Angina', 'Chest wall tenderness',
                     'Chest discomfort', 'Chest tightness', 'Noncardiac chest pain',
                     'Pleuritic pain')) {
    return('Chest pain')
    # Clonic/Generalized/partial seizure not classified
  } else if(x %in% c('Seizure', 'Seizure disorder', 'Partial seizures',
                     'Generalized seizure', 'Clonic seizure')) {
    return('Seizure')
    # None of nose bleed classified
  } else if(x %in% c('Nosebleed', 'Epistaxis', 'Nose bleed')) {
    return('Nosebleed/Epistaxis')
    # Fever classified not under fever
    # low grade/neutropenic fever/Febrile not classified
  } else if(x %in% c('Fever', 'Fever Symptoms', 'Low grade fever', 
                     'Neutropenic fever', 'Spiking fever', 'Febrile')) {
    return('Fever/Febrile')
    # Stomach cramps under abdominal pain
    # Abdominal cramps not classified
  } else if(x %in% c('Stomach pain', 'Abdominal pain', 'Epigastric discomfort',
                     'Abdominal cramps','Stomach ache','Stomach cramps', 
                     'Abdominal discomfort')) {
    return('Stomach/Abdominal pain')
    # Back pain/ache not classified
    # Don't includde thoracic back pain
    # lumbar pain not classified
  } else if(x %in% c('Back pain', 'Back ache', 'Low back pain',
                     'Backache', 'Lumbar pain' )) {
    return('Back pain')
    # Loose bowel/bowel incontinence not classified
    # Functional/secretory diarrhea not included
    # liquid/some stools (like singular versions) not classified
  } else if(x %in% c('Diarrhea', 'Diarrhoea', 'Loose bowel movement', 
                     'Bowel incontinence', 'Loose stools', 'Loose stool', 
                     'Liquid stool', 'Liquid stools', 'Watery stool', 
                     'Watery stools')) {
    return('Diarrhea/Loose stools')
    # Many rash not classified, skin, bullous, urticarial, bullous, maculopapular
    # Scarlatiniform
    # Pruritic rash is not skin rash, some sort of disease
  } else if(x %in% c('Skin rash', 'Generalised rash', 'Malar rash',
                     'Maculopapular rash', 'Bullous rash', 'Scarlatiniform rash',
                     'Urticarial rash', 'Butterfly rash')) {
    return('Skin rash')
    # None of the runny nose is classified in ICD
  } else if (x %in% c('Runny nose', 'Rhinorrhea', 'Rhinorrhoea', 
                      'Rhinitus')) {
    return('Runny nose/Rhinorrhea')
    # Coughing/Unprodutive cough not classified
    # Not including productive cough since it refers
    # to mucus production, and patients usually report cough as well
  } else if (x %in% c('Coughing', 'Cough', 'Dry cough',
                      'Painful cough', 'Unproductive cough')) {
    return('Cough')
    # Didn't include migraine cuz it's a neurological conidtion
    # Didn't include shooting/throbbing pain even tho classified under headache
    # Tension headache not classified
  } else if (x %in% c('Headache', 'Unilateral headache','Sinus headache', 
                      'Throbbing headache','Occipital headache', 'Frontal headache',
                      'Tension headache', 'Hacking cough', 'Effective cough')) {
    return('Headache')
    # Maybe underreported, but it appears that sinus pain can be NOT
    # associated with sinus infections
  } else if (x %in% c('Sinus infection', 'Sinusitis')) {
    return('Sinus infection/Sinusitis')
    # All of them classified under unspecified pain
    # painful not specified
  } else if (x %in% c('Pain',  'Aching pain', 'Night pain', 'Sharp pain',
                      'Spontaneous pain', 'Uncontrolled pain', 'Deep pain',
                      'Painful', 'Mild pain')) {
    return('Pain')
    # Arguably different to pain
  } else if (x  == 'Tenderness') {
    return('Tenderness')
    # Hemorrhage not classified
    # Bruising/Bruise not classified
    # Must be careful what type of bleeding
  } else if (x %in% c('Bleeding', 'Hemorrhage', 'Bruise', 'Bruising', 
                      'Ecchymosis', 'Easy bruising', 'Petechiae')) {
    return('Bleeding/Bruising') 
    #Chills/Shivering/Rigor not classified
  } else if (x %in% c('Chills', 'Shivering', 'Rigors', 'Rigor', 'Chill')) {
    return('Chills/Rigors')
    # Congestion/Sinus congestion not classified
  } else if (x %in% c('Congestion', 'Sinus congestion', 'Nasal congestion')) {
    return('Congestion')
    # not including paresthesia
    # tingling/tingling sensation
  } else if (x %in% c('Numbness', 'Perioral Numbness')) {
    return('Numbness')
  } else if (x %in% c('Tingling', 'Tingling senstation')) {
    return('Tingling')
    # if giddiness existed ,we would trow it in
    # loss of balance can be part of another thing
  } else if (x %in% c('Dizziness', 'Lightheadedness', 'Postural dizziness',
                      'Vertigo', 'Dizzy spells', 'Giddiness')) {
    return('Dizziness')
  } else if (x == 'Dysuria') {
    return('Dysruia')
    # Sweats not classified
  } else if (x %in% c('Night sweats', 'Cold sweat', 'Excessive sweating', 'Sweating',
                     'Sweats')) {
    return('Night sweats/Hyperhidrosis')
    # Hematuria not classified
  } else if (x %in% c('Hematuria', 'Frank hematuria', 'Blood in urine')) {
    return('Hematuria')
    # Tired is like an everyday occurence, whereas fatigue is not
  } else if (x %in% c('Tired', 'Feeling tired', 'Tiredness')) {
    return('Tiredness')
    #Anxiousness, Feeling anxious, nervously anxious not classified
  } else if (x %in% c('Anxiety', 'Anxiety attack', 'Apprehension', 'Anxiety reaction',
                      'Anxiousness', 'Feeling anxious', 'Nervously anxious')) {
    return('Anxiety')
    # Sore throat not classified
  } else if (x %in% c('Sore throat', 'Pharyngitis')) {
    return('Sore throat')
    # NOTE THIS
  } else if (x == 'Appetite') {
    return('Appetite')
    # Peripheral neuropathy not 
  } else if (x %in% c('Neuropathy', 'Peripheral neuropathy', 'Polyneuropathy')) {
    return('Neuropathy') 
    # Probably only one of the ulcerations
  } else if (x == 'Mucositis') {
    return('Mucositis')
    # different vs melena, melena is black stool
    # bloody/blood in stool not classified
  } else if (x %in%  c('Hematochezia', 'Blood in stool', 'Bloody stool', 
             'Blood in stools', 'Bloody stools')) {
    return('Hematochezia')
    # black/dark stools not classified
  } else if (x %in% c('Melena', 'Black stools', 'Dark stools', 'Dark stool',
                      'Tarry stools')) {
    return('Melena')
    # Hardstools/ difficulty not classified
  } else if (x %in% c('Constipation', 'Hard stools', 'Hard stool', 
                      'Difficulty passing stool', 'Constipated', 'Obstipation')) {
    return('Constipation')
    # Redness/Red skins not classified
  } else if (x %in% c('Redness', 'Red skin', 'Erythema')) {
    return('Redness/Erythema')
    #Wheeze/wheezy not classified
  } else if (x %in% c('Wheezing', 'Wheeze', 'Wheezy')) {
    return('Wheezing')
    #Depressed/Depression not classififed
    # Avoid sad/sadness for now
  } else if (x %in% c('Depression', 'Depressed', 'Depressed mood', 
                      'Depressive symptoms')) {
    return('Depression')
    # Loss of weight not classified
  } else if (x %in% c('Weight loss', 'Loss of weight', 'Unintentional weight loss')) {
    return('Weight loss')
  } else if (x == 'Heartburn') {
    return('Heartburn')
    # Burning not classified
    # Really heard to tell what burning means in this case 
  } else if (x == 'Burning') {
    return('Burning') 
  } else if (x %in% c('Weight gain', 'Excessive weight gain')) {
    return('Weight gain')
  } else if (x %in% c('Difficulty swallowing', 'Difficulty swallowing pills',
                     'Dysphagia', 'Unable to swallow')) {
    return('Difficulty swallowing')
    # Rigors not classified
  } else if (x %in% c('Malaise', 'Discomfort')) {
    return('Malaise/Discomfort')
  } else if (x %in% c('Distress', 'Distressed')) {
    return('Distress')
  } else if (x == 'Afebrile') {
    return('Afebrile')
  } else if (x == 'Bowel sounds') {
    return('Bowel sounds')
    # Swollen lymph nodes/enlarged/adenopathy not classified
  } else if (x %in% c('Lymphadenopathy', 'Cervical lymphadenopathy', 'Adenopathy',
                      'Femoral lymphadenopathy', 'Swollen lymph nodes', 
                      'Enlarge lymph nodes')) {
    return('Lymphadenopathy/Adenopathy')
  } else if (x %in% c('Cyanosis', 'Acrocyanosis')) {
    return('Cyanosis')
  } else if (x %in% c('Heart murmur', 'Murmur', 'Systolic murmur')) {
    return('Murmur')
  } else if (x %in% c('Hepatosplenomegaly', 'Splenomegaly')) {
    return('Hepatosplenomegaly')
  } else if (x == 'Anicteric') {
    return('Anicteric')
    # respiratory effort not classified
  } else if (x == 'Respiratory effort') {
    return('Respiratory effort')
    # rhonchi not classified
  } else if (x == 'Rhonchi') {
    return('Rhonchi')
    # clubbing not classified
  } else if (x == 'Clubbing') {
    return('Clubbing')
    # breath sounds not classified
  } else if (x == 'Breath sounds') {
    return('Breath sounds')
    # Rales not classified
  } else if (x %in% c('Rales', 'Fine rales')) {
    return('Rales')
    # Drainage not classified
  } else if (x == 'Drainage') {
    return('Drainage')
    # blood loss anemia
  } else if (x %in% c('Anemia', 'Blood loss anemia')) {
    # Anemia not classified
    return('Anemia')
    # Lesion not classified
  } else if (x %in% c('Lesion')) {
    return('Lesion')
    # Engraftment not classified
  } else if (x == 'Engraftment') {
    return('Engraftment')
    # Toxicity not classified
  } else if (x == 'Toxicity') {
    return('Toxicity')
  } else if (x %in% c('Hypertension', "High blood pressure")) {
    return('Hypertension')
  } else if (x %in% c('Neutropenia', 'Agranulocytosis', 'Autoimmune neutropenia')) {
    return('Neutropenia')
  } else if (x == 'Drowsiness') {
    return('Drowsiness')
  } else if (x == 'Dehydration') {
    return('Dehydration')
  } else if (x %in% c('Fracture', 'Stress fracture', 'Pathologic fracture')) {
    return('Fracture')
  } else if (x == 'Thrombocytopenia') {
    return('Thrombocytopenia')
  } else if (x == 'Pneumonitis') {
    return('Pneumonitis')
  } else if (x %in% c('Pneumonia', 'Atypical pneumonia', 'Bronchopneumonia',
                      'Lingular pneumonia')) {
    return('Pneumonia')
    # Hypokalemia
  } else if (x == 'Hypokalemia') {
    return('Hypokalemia')
    # Hypothyroid not classified
  } else if (x %in% c('Hypothyroidism', 'Hypothyroid')) {
    return('Hypothyroidism')
  } else if (x %in% c('Cataracts', 'Cataract')) {
    return('Cataracts')
    # Acute graft versus host disease not classified
  } else if (x %in% c('Graft versus host disease', 'Acute graft versus host disease')) {
    return('Graft versus host disease')
    # Hypomagnesaemi not classified
    # low magnesium
  } else if (x %in% c('Hypomagnesemia', 'Hypomagnesaemia')) {
    return('Hypomagnesemia')
  } else {
    return('Other')
  }
}
