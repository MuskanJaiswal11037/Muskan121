

''' Two dice are thrown . The events A,B and C are as follows:
A: getting an even number on the first dice
B:getting an odd number on the first dice
C: getting the sum of the numbers on the dice that is less than or equal to 5

The sample space for two dice thrown are:-
 '''
S=[(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(2,1),(2,2),(2,3),(2,4),(2,5),(2,6),
   (3,1),(3,2),(3,3),(3,4),(3,5),(3,6),(4,1),(4,2),(4,3),(4,4),(4,5)
        ,(4,6),(5,1),(5,2),(5,3),(5,4),(5,5),(5,6),(6,1),(6,2),(6,3),(6,4),(6,5),(6,6)]
A=[]
B=[]
C=[]
count=1
for i in S:
    for j in i:
        p=j

        count=int(int(count)+1)
        if(int(count)%2==0):
            if(p%2==0):


             A=A+[i]
            elif(p%2!=0):
                B=B+[i]
            if(i[0]+i[1]<=5):
                C=C+[i]
print("A=" + str(A))
print("B=" + str(B))
print("C=" + str(C))

X=input("Enter the event out of the following events :- 1.A' 2.not B 3.A or B 4.A and B 5.A but not C 6.B or C 7.B and C 8. A and B' and C'" )
if(X=="A'"):

   print("A'=",list(set(S)-set(A)))
elif(X=="not B"):

    print("not B=" ,list(set(S)-set(B)) )
elif(X=="A or B"):
    print("A or B = ",(list(set(A)|set(B))))
elif(X=="A and B"):
    print("A and B =" ,(list(set(A)&set(B))))
elif(X=="A but not C"):
    D=set(S)-set(C)
    print("A but not C= " + str(list(set(A)-set(D))))
elif(X=="B or C"):
    print(" B or C = " + str(list(set(B)|set(C))))
elif(X=="B and C"):
    print(" B and C = " + str(list(set(B)&set(C))))
elif(X=="A and B' and C'"):
    D=set(S)-set(B)
    E=set(S)-set(C)
    print("A and B' and C'=" + str(list(set(A)&D&E)))



