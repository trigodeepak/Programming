#Program for palindrome partitioning
def minPalPartition(string):
    length = len(string)
    dp_cuts = [[0 for i in range(length)]for x in range(length)]
    #This matrix is to determine that the given substring is palindrome or not
    p = [[False for i in range(length)]for x in range(length)]
    #This loop is to access the matrix diagonally from left to right
    for k in range(length):
        i = 0
        j = k
        while(i<length-k):
            #First 3 conditions are to check if substring is palindrome
            if i == j:
                p[i][j] = True
                dp_cuts[i][j] = 0
            elif k+1 == 2:
                p[i][j] = (string[i] == string[j])
            else:
                p[i][j] = (string[i] == string[j]) and p[i+1][j-1]
            #Following conditions are to find the minimum cut  
            if (p[i][j]==True):
                dp_cuts[i][j] = 0
            else:
                dp_cuts[i][j] = float('inf')
                #Make a cut at every possible location and get the minimum cost
                for x in range(i,j):
                    dp_cuts[i][j] = min(dp_cuts[i][j],dp_cuts[i][x]+dp_cuts[x+1][j]+1)
            i+=1
            j+=1
    #Uncomment below lines to print the matrix obtained
##    for row in dp_cuts:
##        print row

    #returning the minimum cut value
    return dp_cuts[0][length-1]

#Driver program
string = "ababbbabbababa"#raw_input().strip() #to take user input
print "Minimum cuts to form a palindrome is :",minPalPartition(string)

