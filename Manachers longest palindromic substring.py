#Refernce Geeks for Geeks code by BHAVYA JAIN

def findLongestPalindromicString(text):
    n = len(text)
    if n == 0:
        print 'LPS of empty string : no character in string'
        return 
    N = 2*n+1    # Position count
    L = [0] * N
    L[0] = 0
    L[1] = 1
    C = 1     # centerPosition of the current palindromic string
    R = 2     # center Right edge
    i = 2    # currentRightPosition
    iMirror = 0     # currentLeftPosition
    maxLPSLength = 0
    maxLPSCenterPosition = 0
    start = -1
    end = -1
    diff = -1
  
   
    for i in xrange(2,N):
      
        # get currentLeftPosition iMirror for currentRightPosition i
        iMirror = i - (2 * (i - C))
        L[i] = 0
        diff = R - i
        # If currentRightPosition i is within centerRightPosition R
        if diff > 0:
            L[i] = L[iMirror]
  
        # Attempt to expand palindrome centered at currentRightPosition i
        # Here for odd positions, we compare characters and
        # if match then increment LPS Length by ONE. Overall, one odd and one even positions on both left
        #and right side will increase LPS Length by TWO
        # If even position, LPS is zero, except when the mirror values (actual characters in case of even length string)are identical(i.e., palindrone)
        try:
            while ((i+L[i]) < N and (i-L[i]) > 0) and (((i+L[i]+1) % 2 == 0) or  (text[(i+L[i]+1)/2] == text[(i-L[i]-1)/2])):
                L[i]+=1
        except Exception as e:
            pass
        if L[i] > maxLPSLength: # Track maxLPSLength
            maxLPSLength = L[i]
            maxLPSCenterPosition = i
  
        # If palindrome centered at  i
        # expand beyond centerRightedge R,
        # adjust centerPosition C based on expanded palindrome.
        if i + L[i] >R: 
            C = i
            R = i + L[i]
  
   
    start = (maxLPSCenterPosition - maxLPSLength) / 2
    end = start + maxLPSLength - 1
    print "LPS of string " + text + " is : ",
    print text[start:end+1],
    print "\n",
    print L
  

text1 = "aa"
findLongestPalindromicString(text1)
#Returned value of even length palindrome-  LPS of string apple is :  pp

  
text2 = ""
findLongestPalindromicString(text2)
#Returned value- LPS of empty string : no character in string
  
text3 = "aba"
findLongestPalindromicString(text3)
# Returned value of odd length palindrome- LPS of string apaple is:  apa 
  

# 

