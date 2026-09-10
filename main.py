
#1 
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            print(f"{int(A)} : {int(B)} : {int(C)} : {int(not (A and B) or not (A or C))}")

#2
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            print(f"{int(A)} : {int(B)} : {int(C)} : {int((A and B) or (not B and C))}")

#3
for A in [0,1]:
    for B in [0,1]:
        for C in [0,1]:
            print(f"{int(A)} : {int(B)} : {int(C)} : {int((A and B) or not C)}")

