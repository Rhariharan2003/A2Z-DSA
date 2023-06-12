class Solution:
	def topK(self, nums, k):
		#Code here
		nums = list(map(int, input().strip().split()))
		k = int(input().strip())
        l = {}
        res =[]
        for i in nums:
            if i in l:
                l[i] +=1
            else:
                l[i] = 1
        #s2 = list(l.values())
        map = sorted(l.items() , key = lambda x : (-x[1] , -x[0]))
        print(map)
        for i in range(k):
            res.append(map[i][0])
        return res
#{ 
 # Driver Code Starts
		
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
    	a = list(map(int, input().strip().split()))
    	n = a[0]
    	nums = a[1:]
    	k = int(input().strip())
    	obj = Solution()
    	ans = obj.topK(nums, k)
    	for i in ans:
    		print(i, end = " ")
    	print()
# } Driver Code Ends
