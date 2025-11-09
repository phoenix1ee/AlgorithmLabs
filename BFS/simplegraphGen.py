from pathlib import Path
import random
import csv
curdir = str(Path.cwd().absolute())

size = [5]

V = [x for x in range(1,size[0]+1)]
print(f'V:{V}')
output = []

for i in range(size[0]):
    Vcopy = [x for x in V]
    adjacent = random.randint(1,size[0])
    for j in range(adjacent):
        output.append((i+1,Vcopy.pop(random.randint(0,len(Vcopy)-1))))

out_path = Path(curdir + "\\simplegraph" + ".txt")
output_f = out_path.open('w')
for k in output:
    output_f.write(f'{k[0]},{k[1]}\n')
output_f.close()

readin=dict()
in_path = Path(curdir + "\\simplegraph" + ".txt")
with open(in_path, mode='r', encoding='utf-8', newline='') as file:
    reader = csv.reader(file, delimiter=',')  # Change delimiter if needed
    for row in reader:
        if row:
            if row[0] not in readin:
                readin.update({row[0]:[row[1]]})
            else:
                readin[row[0]].append(row[1])
print(readin)