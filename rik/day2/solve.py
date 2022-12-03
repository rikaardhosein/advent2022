
R,P,S = (1,2,3)
L,D,W = (0,3,6)

win_cons = {R:S, P:R, S:P}
lose_cons = {v:k for k,v in win_cons.items()}

def tr(c):
    if c in "AX": 
        return R 
    elif c in "BY":
        return P
    else:
        return S

def out_tr(c):
    tr_mat = {"X": L, "Y": D, "Z": W}
    return tr_mat[c]

def rps(opp, you):
    if you == opp:
        return D
    
    for w in win_cons:
        if you == w and opp == win_cons[w]:
            return W
    return L

def find_move(outcome, opp):
    if outcome == D:
        return opp       
    if outcome == L:
        return win_cons[opp]
    if outcome == W:
        return lose_cons[opp]



with open("input.txt", "r") as f:
    total_score = 0
    for line in f:
        opp, you = tr(line[0]), tr(line[2])
        total_score += you + rps(opp, you)

    print(total_score)

with open("input.txt", "r") as f:
    total_score = 0
    for line in f:
        opp, outcome = tr(line[0]), out_tr(line[2])
        total_score += outcome + find_move(outcome, opp)

    print(total_score)