class star:
    def twosum(self,arr,target):
        dict = {}
        result = []
        for i in range(0,len(arr)):
            first = arr[i]
            find_item = target - first

            if first in dict:
                result.append(dict[first])
                result.append( i)
            else:
                dict[find_item] = i
        return result
bubb= star()
print(bubb.twosum([1,1,44,10,12],54))
