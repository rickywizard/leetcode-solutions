class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix)-1
        while top <= bot:
            vmid = top + (bot - top)//2

            if target > matrix[vmid][-1]:
                top = vmid + 1
            elif target < matrix[vmid][0]:
                bot = vmid - 1
            else:
                break 

        if top > bot:
            return False
            
        row = top + (bot - top)//2

        print(row)

        l, r = 0, len(matrix[0])
        while l <= r:
            hmid = (l+r)//2

            if target > matrix[row][hmid]:
                l = hmid + 1
            elif target < matrix[row][hmid]:
                r = hmid - 1
            else:
                return True

        return False
        
