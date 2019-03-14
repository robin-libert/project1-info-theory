import math

def entropy(pDistrib):
    entropy = 0
    for e in pDistrib:
        if e!=0:
            entropy += -e*math.log2(e)
    return entropy

def joint_entropy(pDistrib1, pDistrib2, joinDistribution):
    joint_entropy = 0
    c1 = 0
    for i in pDistrib1:
        c2 = 0
        for j in pDistrib2:
            if joinDistribution[c2][c1] != 0:
                joint_entropy += -(joinDistribution[c2][c1] * math.log2(joinDistribution[c2][c1]))
            c2 += 1
        c1 += 1
    return joint_entropy

def conditional_entropy(pDistrib1, pDistrib2, joinDistribution):
    conditional_entropy = 0
    c1 = 0
    for i in pDistrib1:
        c2 = 0
        for j in pDistrib2:
            if joinDistribution[c2][c1] != 0:
                conditional_entropy += -(joinDistribution[c2][c1] * math.log2((joinDistribution[c2][c1]/j)))
            c2 += 1
        c1 += 1
    return conditional_entropy

def mutual_information(pDistrib1, pDistrib2, joinDistribution):
    mutual_information = 0
    c1 = 0
    for i in pDistrib1:
        c2 = 0
        for j in pDistrib2:
            if joinDistribution[c2][c1] != 0:
                mutual_information += (joinDistribution[c2][c1] * math.log2((joinDistribution[c2][c1]/(i*j))))
            c2 += 1
        c1 += 1
    return mutual_information
    
def joint_entropy3(pDistrib1, pDistrib2, pDistrib3, joinDistribution):
    joint_entropy = 0
    c1 = 0
    for i in pDistrib1:
        c2 = 0
        for j in pDistrib2:
            c3 = 0
            for k in pDistrib3:
                if joinDistribution[c1][c2][c3] != 0:
                    joint_entropy += -(joinDistribution[c1][c2][c3] * math.log2(joinDistribution[c1][c2][c3]))
                c3 += 1
            c2 += 1
        c1 += 1
    return joint_entropy

if __name__ == "__main__":
    X = [1/4,1/4,1/4,1/4]
    Y = [1/2,1/4,1/8,1/8]
    W = [5/16,11/16]
    Z = [5/16,11/16]

    joinDistribution = [[1/8,1/16,1/16,1/4],
                        [1/16,1/8,1/16,0],
                        [1/32,1/32,1/16,0],
                        [1/32,1/32,1/16,0]]

    joinDistributionWZ = [[0,5/16],
                          [11/16,0]]


    joinDistributionXW = [[3/16,3/16,3/16,3/16],
                          [1/16,1/16,1/16,1/16]]

    joinDistributionXYW = [[[0,1/8], [1/16,0],[1/16,0],[1/4,0]],
                           [[1/16,0],[0,1/8],[1/16,0],[0,0]],
                           [[1/32,0],[1/32,0],[0,1/16],[0,0]],
                           [[1/32,0],[1/32,0],[1/16,0],[0,0]]]

    print("1.   H(X) = " + str(entropy(X)))
    print("     H(Y) = " + str(entropy(Y)))
    print("     H(W) = " + str(entropy(W)))
    print("     H(Z) = " + str(entropy(Z)))
    
    print("2.   H(X,Y) = " + str(joint_entropy(X,Y,joinDistribution)))
    print("     H(X,W) = " + str(joint_entropy(X,W,joinDistributionXW)))#not the same
    print("     H(Y,W) = to do")
    print("     H(W,Z) = " + str(joint_entropy(W,Z,joinDistributionWZ)))
    
    print("3.   H(X|Y) = " + str(conditional_entropy(X, Y, joinDistribution)))
    #print("     H(W|X) = " + str(conditional_entropy(W, X, joinDistributionXW)))
    print("     H(Z|W) = " + str(conditional_entropy(Z, W, joinDistributionWZ)))
    print("     H(W|Z) = " + str(conditional_entropy(W, Z, joinDistributionWZ)))
    
    print("4.   H(X,Y|W) = " + str(None))
    print("     H(W,Z|X) = " + str(None))
    
    print("5.   I(X;Y) = " + str(mutual_information(X,Y,joinDistribution)))
    print("     I(X;W) = " + str(mutual_information(X,W,joinDistributionXW)))
    #print("     I(Y;Z) = " + str(mutual_information(y_z_joint_distribution)))
    print("     I(W;Z) = " + str(mutual_information(W,Z,joinDistributionWZ)))