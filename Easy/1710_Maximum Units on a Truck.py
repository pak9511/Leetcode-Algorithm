class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes=sorted(boxTypes,key=lambda x: x[1],reverse=True)
        units=0
    
        for box in boxTypes:
            if box[0]<=truckSize:
                truckSize-=box[0]
                units+=box[0]*box[1]
            else:
                units+=truckSize*box[1]
                truckSize-=truckSize
            if truckSize==0:
                return units
        return units
