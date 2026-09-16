print("a b c d e f g h|F|")
cnto = 0
cntz = 0
knf = "("
dnf = "("
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                data = [a, b, c, d, e, f, g, h]
                                dstr = "abcdefgh"
                                F = int((not a or b) and (not(c and d)) and (not(e or f)) and (g or h))
                                if F == 1:
                                    cnto += 1
                                    #print(a, b, c, d, e, f, g, h, F)
                                    for i in range(8):
                                        if data[i] == 0:
                                            if i == 0:
                                                knf = knf +  "(not " + dstr[i] + ")"
                                            else:
                                                knf = knf + " and (not " + dstr[i] + ")"
                                        else:
                                            if i == 0:
                                                knf += dstr[i]
                                            else:   
                                                knf += " and " + dstr[i]
                                    knf = knf + ") or ("
                                else:
                                    for i in range(8):
                                        if data[i] == 1:
                                            if i == 0:
                                                dnf = dnf +  "(not " + dstr[i] + ")"
                                            else:
                                                dnf = dnf + " or (not " + dstr[i] + ")"
                                        else:
                                            if i == 0:
                                                dnf += dstr[i]
                                            else:   
                                                dnf += " or " + dstr[i]
                                    dnf = dnf + ") and ("
                                    #print(a, b, c, d, e, f, g, h, F) 
knf = knf[:-5]
dnf = dnf[:-5]
print ("SKNF: ", knf)
#print ("SDNF: ", dnf)
for a in range(2):
    for b in range(2):
        for c in range(2):
            for d in range(2):
                for e in range(2):
                    for f in range(2):
                        for g in range(2):
                            for h in range(2):
                                F = ((not a) and (not b) and (not c) and (not d) and (not e) and (not f) and (not g) and h) or\
                                    ((not a) and (not b) and (not c) and (not d) and (not e) and (not f) and g and (not h)) or \
                                    ((not a) and (not b) and (not c) and (not d) and (not e) and (not f) and g and h) or \
                                    ((not a) and (not b) and (not c) and d and (not e) and (not f) and (not g) and h) or \
                                    ((not a) and (not b) and (not c) and d and (not e) and (not f) and g and (not h)) or \
                                    ((not a) and (not b) and (not c) and d and (not e) and (not f) and g and h) or\
                                    ((not a) and (not b) and c and (not d) and (not e) and (not f) and (not g) and h) or\
                                    ((not a) and (not b) and c and (not d) and (not e) and (not f) and g and (not h)) or \
                                    ((not a) and (not b) and c and (not d) and (not e) and (not f) and g and h) or \
                                    ((not a) and b and (not c) and (not d) and (not e) and (not f) and (not g) and h) or\
                                    ((not a) and b and (not c) and (not d) and (not e) and (not f) and g and (not h)) or\
                                    ((not a) and b and (not c) and (not d) and (not e) and (not f) and g and h) or\
                                    ((not a) and b and (not c) and d and (not e) and (not f) and (not g) and h) or\
                                    ((not a) and b and (not c) and d and (not e) and (not f) and g and (not h)) or\
                                    ((not a) and b and (not c) and d and (not e) and (not f) and g and h) or \
                                    ((not a) and b and c and (not d) and (not e) and (not f) and (not g) and h) or \
                                    ((not a) and b and c and (not d) and (not e) and (not f) and g and (not h)) or \
                                    ((not a) and b and c and (not d) and (not e) and (not f) and g and h) or \
                                    (a and b and (not c) and (not d) and (not e) and (not f) and (not g) and h) or \
                                    (a and b and (not c) and (not d) and (not e) and (not f) and g and (not h)) or \
                                    (a and b and (not c) and (not d) and (not e) and (not f) and g and h) or \
                                    (a and b and (not c) and d and (not e) and (not f) and (not g) and h) or \
                                    (a and b and (not c) and d and (not e) and (not f) and g and (not h)) or \
                                    (a and b and (not c) and d and (not e) and (not f) and g and h) or \
                                    (a and b and c and (not d) and (not e) and (not f) and (not g) and h) or \
                                    (a and b and c and (not d) and (not e) and (not f) and g and (not h)) or \
                                    (a and b and c and (not d) and (not e) and (not f) and g and h)
                                #print(a, b, c, d, e, f, g, h, F)