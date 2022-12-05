def getNumSrcDst(s):
    words = s.split(' ')
    num_to_move = int(words[1])
    src = int(words[3])
    dst = int(words[5])
    return num_to_move, src, dst

def cratemover9000(mat,n,s,d):
    for i in range(n):
        ch = mat[s][-1]
        mat[s] = mat[s][:-1]
        mat[d] += ch
        
def cratemover9001(mat,n,s,d):
    ch = mat[s][-n:]
    mat[s] = mat[s][:-n]
    mat[d] += ch

def main():
    mat = [""]*10
    mat[0] = ""
    mat[1] = "TPZCSLQN"
    mat[2] = "LPTVHCG"
    mat[3] = "DCZF"
    mat[4] = "GWTDLMVC"
    mat[5] = "PWC"
    mat[6] = "PFJDCTSZ"
    mat[7] = "VWGBD"
    mat[8] = "NJSQHW"
    mat[9] = "RCQFSLV"
    
    with open("input.txt") as f:
        all_operations = f.read().strip().split("\n\n")        
        individual_ops = all_operations[1].split("\n")
        for op in individual_ops:
            n,s,d = getNumSrcDst(op)
            #cratemover9000(mat,n,s,d)
            cratemover9001(mat,n,s,d)

    result = ""
    for r in mat[1:]:
        result += r[-1]
    print(result)
            
            
            

if __name__=="__main__":
    main()
