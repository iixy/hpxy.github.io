#fontTool.py 将所有html文件中的字提取出来
import os

DIR = r"C:\Users\m\Documents\GitHub\hpxy.github.io"

os.chdir(DIR)
SUM = []
for root,path,file in os.walk(DIR):
    if root.startswith(DIR+r"\."): continue;
    
    os.chdir(root)
    for j in file:
        if j.endswith(".html") or j.endswith(".js"): 
            print(j)
            with open(j,"r",encoding="utf-8") as fp:
                for k in fp.readlines():
                    for l in k:
                        if not (l in SUM): SUM.append(l)
os.chdir(DIR+r"\font")
with open("allFont.alt","w",encoding="utf-8") as fp:
    for i in SUM:
        fp.write(i)