class star:
    # [[9,1,7],[8,9,2],[3,4,6]]
    def findrepeatingmissing(self,arr):
        result=[]
        final =[]
        size = len(arr)
        real_sum= 0
        expected_sum = ((size*size)*(size*size+1))//2
        # real_sum = expected_sum - required_num
        for i in range(0,len(arr)):
            for j in range(0,len(arr)):
                real_sum  += arr[i][j]
                if arr[i][j] not in result:
                    arr[i][j]
                    result.append(arr[i][j])
                else:
                    final.append( arr[i][j])
        print(expected_sum,real_sum, final[0])
        required_num = (expected_sum + final[0]) - real_sum
        final.append(required_num)
        print(final)



k = star()
k.findrepeatingmissing([[9,1,7],[8,9,2],[3,4,6]])




