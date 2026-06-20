class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        arr = list(zip(heights,names))
        arr.sort(reverse=True)
        return [name[1] for name in arr]

        