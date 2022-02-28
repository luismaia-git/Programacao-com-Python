arq = open("candidatos.txt", "r")

results = {}

for line in arq.readlines():
    
    names = line.strip()
  
    if "Ã©" in names:
        nameMod = names.replace("Ã©", "é")
        results[nameMod] = 0
    elif "Ã£" in names:
        nameMod = names.replace("Ã£", "ã")
        results[nameMod] = 0
    else:
        results[names] = 0
    
arq.close()

arq2 = open("votos.txt", "r")
votes = []

for line in arq2.readlines():
    votes.append(int(line.strip()))
    
list_names = []  

for key in results.keys():
    list_names.append(key)
    
arq2.close()

for i in range(len(list_names)):
    results[list_names[i]] = votes[i]

most_votes = 0

for item in sorted(results):
    print(f"{item}: {results[item]} voto(s)")
    
    if results[item] > most_votes:
        victory = item
        most_votes = results[item]
    
print(f"Vitória: {victory}")