from collections import Counter

class Statistics:
    def mean(lst: list) -> float:
        length = len(lst)
        sum = 0
        for i in lst:
            sum += int(i.strip())

        return sum/length

    def median(lst: list):
        length = len(lst)
        if(length % 2 == 0):
            l = length / 2
            return (lst[l] + lst[l-1]) / 2
        else:
            return lst[int((length-1) /2)]

    def mode(lst: list):
        return Counter(lst).most_common(1)[0][0]



