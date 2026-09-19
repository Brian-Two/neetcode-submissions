class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # #get a hash of the freqencies
        # freq = {}
        # for num in nums:
        #     freq[num] = freq.get(num, 0) + 1

        # # heapify the (freqency, number) 
        #     # go trhough the hash
        #     # since heapify is min -> largest keep heappushing and poping until you get to the end of the frequencues making sure 
        # top_k = []
        # for number, frequency in freq.items():
        #     heapq.heappush(top_k, (frequency, number))
        #     if len(top_k) > k:
        #         heapq.heappop(top_k)
        # print(top_k)
        # return [item[1] for item in top_k]

        # # time - o(nlogk): heap push pop is o (m logk) m being # diff freq which could be n 
        # # space - o (n + k): n is worse case for hasmap, k is for the return statement 

        #BUCKET SORT

        freq = {}

        count = [[] for i in range (len(nums) + 1)]
    

        for num in nums:
            freq[num] = freq.get(num, 0) +1 
        for num, frequency in freq.items():
            count[frequency].append(num)
        res = []
        for i in range(len(count) -1, 0, -1):
            for num in count[i]:
                res.append(num)
                if len(res) == k:
                    return res
            
        


