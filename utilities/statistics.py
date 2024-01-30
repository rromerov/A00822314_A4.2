class statistics:

    def __init__(self, data):
        self.data = data
    
    def mean(self):
        return sum(self.data) / len(self.data)

    def median(self):
        sortedData = sorted(self.data)
        n = len(sortedData)
        if n % 2 == 0:
            return (sortedData[n//2 - 1] + sortedData[n//2]) / 2
        else:
            return sortedData[n//2]

    def mode(self):
        counts = {}
        for x in self.data:
            if x in counts:
                counts[x] += 1
            else:
                counts[x] = 1
        if counts:
            mode_value = max(counts, key=counts.get)
            if list(counts.values()).count(counts[mode_value]) == 1:
                return mode_value
            else:
                return "There is no mode"
        
    def standard_deviation(self):
        mean = self.mean()
        return (sum([(x - mean)**2 for x in self.data]) / len(self.data))**0.5
    
    def variance(self):
        mean = self.mean()
        return sum([(x - mean)**2 for x in self.data]) / len(self.data)

