class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # no change

        # 20

        #20: 3 - 5,  1 - 10 + 1-5
        # 10:  1 - 5

        change = defaultdict(int)

        for bill in bills:
            change[bill] += 1

            if bill == 10:
                if change[5] < 1:
                    return False
                change[5] -= 1
            elif bill == 20:
                if change[5] >= 1 and change[10] >= 1:
                    change[5] -= 1
                    change[10] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        return True