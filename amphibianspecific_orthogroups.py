#import modules 
import csv
# amphibianspecific_orthogroups.py 


# list of our 39 species 
species_names =     ['Alligatormississippiensis', 'Apusapus', 'Aquilachrysaetos', 
                     'Balaenopteramusculus', 'Ceratotheriumsimum', 'Choloepusdidactylus',
                      'Columbalivia', 'Desmodusrotundus', 'Dromaiusnovaehollandiae',
                      'Elephasmaximum', 'Eublepharismacularius', 'Gopherusevgoodei',
                      'Gorillagorilla', 'Nannosplalaxgalili', 'Nipponianippon',
                      'Numidameleagris', 'Ornithorhynchusanatinus', 'Pogonavitticeps',
                      'Pseudonajatextilis', 'Rissatridactyla', 'Sarcophilusharrisi',
                      'Sphenodonpunctatus', 'Susscrofa', 'Taeniopygiaguttata',
                      'Tupaiachinensis', 'Varanuskomodoensis', 'cuculuscanorus',
                      'Microcaeciliauniclour', 'Geotrypetesseraphini', 'Rhinatremabivittatum',
                      'Bombinabombina', 'Bufobufo', 'Leptobrachiumleishanense',
                      'Nanoranaparkeri', 'Ranatemporaria', 'Rhinatremabivittatum', 'Speabombifrons',
                      'XenopusLaevis', 'XenopusTropicalis', 'Pleurodeleswatl']


# input the gene count TSV file which forms the output for orthofinder (no filtering)
with open('/Users/rhianah/Documents/Dissertation/orthofinder_names_protein_ple/OrthoFinder/Results_Jun13_1/Orthogroups/Orthogroups.GeneCount.tsv', 'r') as file:
    reader = csv.DictReader(file, delimiter='\t')
##start the count for number of orthogroups 
    count = 0 

    orthogroups =[]


# Loop the rows in the list 
    for row in reader:
        # Check if they meet our considtions. 
        all_conditions_met = all(row[species] == '0' for species in species_names[0:26]) #no amniotes present 
        any_condition_met_1 = any(int(row[species]) >= 1 for species in species_names[27:29]) #caecilians 
        any_condition_met_2 = any(int(row[species]) >= 1 for species in species_names[30:38]) #frogs 
        any_condition_met_3 = any(int(row[species]) >= 1 for species in species_names[39:]) #newt

        if all_conditions_met and any_condition_met_1 and any_condition_met_2 and any_condition_met_3:
            # Increment the counter
            count += 1
            # Add the orthogroup to the list
            orthogroups.append(row['Orthogroup'])

    # Print number of orthogroups
    print("Number of orthogroups:", count)
    # Print list of orthogroups
    print("Orthogroups:", orthogroups)
