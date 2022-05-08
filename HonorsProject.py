import random

def GenerateMatches(perfect_matches=[], no_matches=[]):
    def GenerateMatches_h(L=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]):
        L2=[]
        for i in range(len(L)):
            b=random.choice(L)
            L2.append(b)
            L.remove(b)

        return L2
    
    def redundant_match(l, no_matches):
        for i in range(0, len(l), 2):
            for j in range(len(no_matches)):
                if l[i]==no_matches[j][0] and l[i+1]==no_matches[j][1] or l[i]==no_matches[j][1] and l[i+1]==no_matches[j][0]:
                    return True
        else:
            return False
    
    m1=GenerateMatches_h()

    if len(perfect_matches)>0:
        for i in range(len(perfect_matches)):
            m1.remove(perfect_matches[i])

    if len(no_matches)>0:
        while redundant_match(m1, no_matches):
            m1=GenerateMatches_h(m1)
    
    L3=[]
    for i in range(0, len(m1), 2):
        L3.append((m1[i], m1[i+1]))
    return L3
    


def Match_perfect(Match, Perfect_Matches):
    PM_2=[]
    for match in Perfect_Matches:
        PM_2.append((match[0], match[1]))
        PM_2.append((match[1], match[0]))
    return Match in PM_2


def change_text(text):
    n=[]
    for i in range(len(text)-1):
        if i>0:
            if text[i].isnumeric():
                if text[i+1].isnumeric():
                    entry=int(text[i:i+2])
                    n.append(entry)
                elif not text[i-1].isnumeric():
                    n.append(int(text[i]))
    return n
      
PM=[]
NM=[]
rounds=0
P_Matches=GenerateMatches(PM, NM)
correct_matches=0

if __name__=='__main__':
    while len(PM)<16:
        Matches=GenerateMatches(PM, NM)
        rounds+=1
        print("Week: {}".format(rounds))

        for matches in Matches:
            if Match_perfect(matches, P_Matches):
                correct_matches+=1

        i=random.randint(0,len(Matches)-1)
        couple=Matches[i]
        if Match_perfect(couple, P_Matches):
            print("{} and {} are a match".format(couple[0], couple[1]))
            PM.append(couple[0])
            PM.append(couple[1])
        else:
            print("{} and {} are not a match".format(couple[0], couple[1]))
            NM.append(couple)

    

    else:
        print("All matches found!")