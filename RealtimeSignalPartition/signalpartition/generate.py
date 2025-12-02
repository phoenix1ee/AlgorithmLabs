from pathlib import Path
import random
x = "101"
y = "010"
n = [1000,2000,4000,8000]
cwd = Path.cwd()

for item in n:
    remaning = item
    outpath = cwd / f"blackbox{str(item)}.txt"
    with outpath.open(mode="w") as file:
        xc=0
        yc=0
        file.write(f"BB{item},")
        while remaning>0:
            pick = random.randint(0,1)
            if pick == 0:
                file.write(x[xc])
                xc = (xc+1)%len(x)
            else:
                file.write(y[yc])
                yc = (yc+1)%len(y)
            remaning-=1
        file.write(","+x+","+y+"\n")