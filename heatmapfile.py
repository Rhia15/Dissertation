##this piece of code provides the inputs for the excel file for creating a heatmap 
##it provides a list of outputs: decrease, in increase or none (neither increased or decreased) for the list of species and nodes in the input 
##The output were copied and pasted manually into the excel sheet for the R script input (heatmap.r) 


##make a function taking in the label, gene family and the text file path 
def find_gene_status(label, gene_family, data_file):
    with open(data_file, 'r') as file:
        lines = file.readlines()


##track if gene family has increased or not 
    status_dict = {}
    is_increased = False

##loop through each line and distinguish info through patterns 
    for line in lines:
        line = line.strip().split(':')
        if line[0] == 'Label':
            current_label = line[1]
        elif line[0] == 'increased':
            is_increased = True
        elif line[0] == 'decreased':
            is_increased = False
        elif line[0].startswith('OG'):
            gene_id = line[0]
            if current_label == label:
                status_dict[gene_id] = is_increased

    if gene_family in status_dict:
        if status_dict[gene_family]:
            return "increased"
        else:
            return f"decreased"
    else:
        return f"none"

##add labels in the order of tree 
label_names = [
    "Aquilachrysaetos",
    "<3>",
    "Taeniopygiaguttata",
    "<7>",
    "Nipponianippon",
    "<11>",
    "Rissatridactyla",
    "<19>",
    "cuculuscanorus",
    "<10>",
    "<20>",
    "Apusapus",
    "<41>",
    "Columbalivia",
    "Numidameleagris",
    "<48>",
    "Dromaiusnovaehollandiae",
    "<58>",
    "Alligatormississippiensis",
    "<64>",
    "Gopherusevgoodei",
    "Varanuskomodoensis",
    "<43>",
    "<73>",
    "Pogonavitticeps",
    "<51>",
    "Pseudonajatextilis",
    "<61>",
    "Eublepharismacularius",
    "Sphenodonpunctatus",
    "Susscrofa",
    "<17>",
    "Balaenopteramusculus",
    "<26>",
    "Ceratotheriumsimum",
    "<75>",
    "<37>",
    "Desmodusrotundus",
    "<46>",
    "Gorillagorilla",
    "<24>",
    "Tupaiachinensis",
    "<36>",
    "<64>",
    "Nannosplalaxgalili",
    "Elephasmaximum",
    "<71>",
    "<47>",
    "Choloepusdidactylus",
    "<72>",
    "Sarcophilusharrisi",
    "Ornithorhynchusanatinus",
    "Ranatemporaria",
    "<20>",
    "Nanoranaparkeri",
    "Bufobufo",
    "<44>",
    "Leptobrachiumleishanense",
    "<33>",
    "Speabombifrons",
    "<52>",
    "XenopusTropicalis",
    "<45>",
    "<62>",
    "XenopusLaevis",
    "<70>",
    "Bombinabombina",
    "Pleurodeleswatl",
    "<74>",
    "Microcaeciliauniclour",
    "<56>",
    "Geotrypetesseraphini",
    "<66>",
    "Rhinatremabivittatum"
]

##run against one gene family at a time 
gene_family = 'OG0001255'

##path to text file in a specific format 
file_path = '/Users/rhianah/Documents/Dissertation/Changed_IDs_analysis_2_0.05.txt'

for label_name in label_names:
    result = find_gene_status(label_name, gene_family, file_path)
    print(result)

