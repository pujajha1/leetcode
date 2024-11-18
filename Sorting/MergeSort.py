    def conquer(self,arr,left,mid,right):
        result =[]
        idx1=left
        idx2=mid+1
        while idx1<=mid and idx2 <=right:
            if arr[idx1] <= arr[idx2]:
                result.append( arr[idx1])
                idx1+=1
            else:
                result.append( arr[idx2])
                idx2+=1
        while idx1<=mid:
            result.append(arr[idx1])
            idx1+=1
        while idx2<=right:
            result.append(arr[idx2])
            idx2+=1
        for i, val in enumerate(result):
            arr[left+i] = val

    def divide(self,arr,left,right):
        if left>=right:
            return
        mid = (left+right)//2
        self.divide(arr,left,mid)
        self.divide(arr,mid+1,right)
        self.conquer(arr,left,mid,right)


    def mergesort(self):
        # arr=[12,90,50,8,28]
        arr=[1,20,50,80,28]
        self.divide(arr,0,len(arr)-1)
        print("Sorted Array:")
        print(arr)




bubb= star()
bubb.mergesort()
