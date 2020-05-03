# Author: Anh-Minh Nguyen
# Date: 05/03/2020

# biobash
biobash <- function(x) {
  if(x %in% c('Facial weakness','General weakness','Muscle weakness','Weakness',
              'Asthenia', 'Muscle fatigue', 'Muscular fatigue')) {
    return('Weakness/Asthenia')
  } else if(x %in% c('Shortness of breath', 'Dyspnea', 'Dyspnoea', 'Air hunger',
                     'Paroxysmal nocturnal dyspnea', 'Nocturnal dyspnea', 
                     'Exertional dyspnea', 'Dyspnea on exertion')) {
    return('Shortness of breath/Dyspnea')
  } else if(x %in% c('Lethargy', 'Lethargic')) {
    return('Lethargy')
  } else if(x %in% c('Ankle swelling', 'Swollen feet', 'Pedal edema', 'Leg edema', 
                     'Edema', 'Oedema','Fluid retension', 'Fluid overload', 
                     'Swollen Leg', 'Dependent edema', 'Dependent oedema')) {
    return('Edema/Fluid retention') 
  } else if(x %in% c('Confusion', 'Confusional State', 'Delirium', 'Confused')) {
    return('Confusion/Delirium')
  } else if(x %in% c('Irregular heart beat', 'Irregular heart rate', 'Arrhythmia', 
                     'Cardiac arrhythmia','Cardiac arrhythmias', 'Abnormal heart beat', 
                     'Palpitations', 'Rapid heart beat', 'Tachycardia',
                     'Ventricular arrhythmia', 'Atrial arrhythmia', 'Tachyarrhythmia',
                     'Atrial tachycardia', 'Ventricular tachycardia',
                     'Paroxysmal tachycardia', 'Paroxysmal supraventricular tachycardia',
                     'Paroxysmal ventricular tachycardia', 'Paroxysmal atrial tachycardia',
                     'Supraventricular tachycardia', 'Rapid atrial fibrillation',
                     'Paroxysmal atrial tachycardia', 'Paroxysmal atrial flutter',
                     'Paroxysmal atrial fibrillation', 'Atrial fibrillation', 
                     'Atrial dysrhythmia', 'Ventricular dysrhythmia', 
                     'Nonsustained ventricular tachycardia')) {
    return('Arrhythmia/Tachycardia')
  } else if(x %in% c('Fatigue', 'Fatigability', 'Exhaustion', 'Extreme exhaustion',
                     'Loss of energy')) {
    return('Fatigue')
  } else if(x %in% c('Itching', 'Itch', 'Itchy', 'Generalized Pruritus', 'Pruritus')) {
    return('Pruritus/Itchiness')
  } else if(x %in% c('Muscle cramps', 'Cramping', 'Cramping pain', 'Crampy',
                     'Foot cramps', 'Hand cramps', 'Leg cramps', 'Menstrual cramps')) {
    return('Cramping')
  } else if(x %in% c('Muscle twitching', 'Muscle twitch', 'Twitch', 'Twitching')) {
    return('Twitching')
  } else if(x %in% c('Nausea', 'Nauseated', 'Nauseous')) {
    return('Nausea')
  } else if(x %in% c('Vomiting', 'Uncontrollable vomiting', 'Vomit',
                     'Vomitus', 'Bilious vomit','Bilious vomiting', 'Throwing up',
                     'Emesis', 'Coffee ground emesis', 'Bilious emesis', 'Hyperemesis')) {
    return('Vomiting/Emesis')
  } 
  if(x %in% c('Loss of appetite', 'Anorexia', 'Anorexic')) {
    return('Loss of appetite/Anorexia')
  } else if(x %in% c('Chest pain', 'Chest wall pain', 'Pleuritic chest pain', 
                     'Exertional chest pain', 'Pressure in chest', 'Angina', 
                     'Chest discomfort', 'Chest tighness', 'Noncardiac chest pain')) {
    return('Chest pain/discomfort')
  } else if(x %in% c('Seizure', 'Seizure disorder', 'Partial seizures', 'Partial seizures',
                     'Generalized seizure', 'Clonic seizure')) {
    return('Seizure')
  } else if(x %in% c('Nosebleed', 'Epistaxis', 'Nose bleed')) {
    return('Nosebleed/Epistaxis')
  } else if(x %in% c('Fever', 'Fever Symptoms', 'Low grade fever', 
                     'Neutropenic fever','Feeling feverish', 'Spiking fever')) {
    return('Fever')
  } else if(x %in% c('Stomach pain', 'Abdominal pain', 
                     'Abdominal cramps','Stomach ache','Stomach cramps')) {
    return('Stomach pain')
  } else if(x %in% c('Back pain', 'Back ache', 'Low back pain', 'Thoracic back pain',
                     'Backache', 'Lumbar pain' )) {
    return('Back pain')
  } else if(x %in% c('Diarrhea', 'Diarrhoea', 'Loose bowel movement', 
                     'Bowel incontinence', 'Bloody diarrhea', 'Functional diarrhea',
                     'Secretory diarrhea')) {
    return('Diarrhea')
  } else if(x %in% c('Skin rash', 'Pruritic rash', 'Generalised rash', 'Malar rash',
                     'Maculopapular rash', 'Bullous rash', 'Scarlatiniform rash',
                     'Urticarial rash')) {
    return('Skin rash')
  } else {
    return('Sorry')
  }
}