class star:
    # [1,1,2,7,5,5,5] num=2
    def findfreqtgtnum(self,arr,num):
        result ={}
        for i in range(0,len(arr)):
            if arr[i] not in result:
                result[arr[i]] = 1
            else:
                result[arr[i]] +=1
        for i in result:
            if result[i]>num:
                print(i)
k=star()
arr =[1,1,2,3,5,5,5]
k.findfreqtgtnum(arr, 2)





