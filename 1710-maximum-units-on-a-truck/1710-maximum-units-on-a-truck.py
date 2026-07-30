class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        res = 0
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        for box in boxTypes:
            if truckSize >= box[0]:
                res += box[0]*box[1]
                truckSize -= box[0]
            else:
                res += truckSize * box[1]
                break
        
        return res