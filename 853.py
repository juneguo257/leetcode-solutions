class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(reverse=True)

        carStack = []

        for i in range(len(cars)):
            finishTime = (float(target)-cars[i][0]) / float(cars[i][1])
            if (len(carStack) == 0):
                carStack.append(finishTime)
            else:
                if finishTime > carStack[-1]:
                    carStack.append(finishTime)
        
        return len(carStack)