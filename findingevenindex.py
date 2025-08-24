#Print characters present at an even index number
def evenindex(x):
    for i in range(len(x)):
        if i%2==0:
            print(f"interation {i},{x[i]}")
            
evenindex("prabesh")