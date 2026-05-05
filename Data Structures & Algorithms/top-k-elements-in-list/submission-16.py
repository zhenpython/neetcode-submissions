class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
            
        sorted_dict = {k: v for k, v in sorted(count.items(), key=lambda item: item[1],reverse=True)}
        sorted_list = list(sorted_dict.keys())
        my_list = []
        for i in range(k):
            my_list.append(int(sorted_list[i]))
        return my_list