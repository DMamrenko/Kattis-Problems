inp = input()
ts = ""
gs = ""
cs = ""
for letter in inp:
    if letter == "T":
        ts+="T"
    elif letter == "G":
        gs += "G"
    else:
        cs += "C"
print(len(ts)**2 + len(gs)**2 + len(cs)**2 + min([len(ts), len(gs), len(cs)])*7)
