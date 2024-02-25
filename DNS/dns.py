import csv

# Ouvrir le fichier d'entrée en mode lecture
with open('student.csv', mode='r') as infile:
    reader = csv.reader(infile, delimiter=';')
    
    # Ouvrir le fichier de sortie en mode écriture
    with open('DNS_pret.csv', mode='w') as outfile:
        writer = csv.writer(outfile, delimiter=';')
        
        # Lire chaque ligne du fichier d'entrée
        for row in reader:
            if len(row) >= 4:
                # Récupérer les informations nécessaires
                IP = row[0]
                nom = row[1]
                
                # Construire la ligne pour le fichier de sortie
                dns_line = f"address=/{nom}.lan/10.10.0.{IP}"
                
                # Écrire la ligne dans le fichier de sortie
                writer.writerow([dns_line])

print("Opération terminée avec succès.")
