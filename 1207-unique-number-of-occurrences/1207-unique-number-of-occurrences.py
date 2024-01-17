class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # approach -> if we look at the constraints. 
        """  make an frequency array (like hashmap) of length 0 to 2000 (bcz of constraints) -1000 val will be sotred at index 0 and so on.
        then sort that array to check duplicates. 

        Tc O(nlogn) sc O(1) 
        """ 
        freq_arr = [0]*2000
        for i in arr:
            new_i = i + 1000   # to make negatives to positive.
            freq_arr[new_i] +=1    # incrementing the frequencey.
        
        freq_arr.sort()  
        for i in range(1999):  # value should not be 0. and cant have duplicate.
            if freq_arr[i] != 0 and freq_arr[i] == freq_arr[i+1]:
                return False
        
        return True
        



