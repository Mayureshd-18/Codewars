def sum_of_intervals(intervals):
        intervals = list(map(list, intervals))
        intervals.sort()
        stack = []
        stack.append(intervals[0])
        for i in intervals[1:]:
            if stack[-1][0] <= i[0] <= stack[-1][-1]:
                stack[-1][-1] = max(stack[-1][-1], i[-1])
            else:
                stack.append(i)
        res = 0
        for i in range(len(stack)):
            res+= stack[i][1] - stack[i][0]
        return res
