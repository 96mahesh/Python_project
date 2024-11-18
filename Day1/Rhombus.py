for i in range(0,5):
    for j in range(0,5):
        if((j==1 or j==5) and i==3 or i==2 and(j==2 or j==4) or i==3 and (j==1 or j==5) or i==4 and (j==2 or j==4)):
          print(" *", end=" ")

        else:
            print(" ",end=" ")
    print()