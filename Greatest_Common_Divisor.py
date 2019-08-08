class Solution:
	# @param A : integer
	# @param B : integer
	# @return an integer
	def gcd(self, A, B):
	    if A==0:
	        return B
	    elif B==0:
	        return A
	    elif A==B:
	        return A
	    else:
	        return self.gcd(B,A%B)
