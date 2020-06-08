#Akash S Pawar

L = [[0,2,0,4,6],
     [0,0,0,8,9],
     [0,1,0,3,8]]

for i in L:
    
            print(i)
            

def getIndexPositions(listOfElements, element):
    
    zero = []
    indexPos = 0
    while True:
        try:
           
            indexPos = listOfElements.index(element, indexPos)
           
            zero.append(indexPos)
            indexPos += 1
        except ValueError as e:
            break
 
    return zero




s = ([sum(x) for x in zip(*L)])
zero = getIndexPositions(s, 0)

print("\n Zero columns are: ", zero)

p=0
while p < len(zero):

                    for col in L:
                                del col[p]
                    p +=1

for y in L:
            print(y)

                    


            
          
          
            





