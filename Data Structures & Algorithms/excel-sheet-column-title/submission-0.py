class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        sheet = []

        while columnNumber:
            columnNumber -= 1
            nxt = columnNumber // 26
            mod = columnNumber % 26

            sheet.append(chr(ord('A') + mod))
            columnNumber = nxt

        return ''.join(reversed(sheet))