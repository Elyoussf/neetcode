from collections import *

class Solution:
    def findAllPeople(self,n : int ,meetings : list[list[int]],firstPerson : int) ->list[int]:
        # n is the number of persons 
        who_know = [False for i in range(n)]
        who_know[0] = True
        who_know[firstPerson] = True
        meetings.sort(key = lambda x: x[2]) # sorted based on the time 
        time = meetings[0][2]
        allMeetingFinished = []
        i = 0
        m = len(meetings) # This si the number of meetings i have in total
        while i < m:
            #print(meetings[i])
            if time != meetings[i][2]:
                for p in allMeetingFinished:
                    if who_know[p]:
                        for p in allMeetingFinished:
                            who_know[p] = True
                        break
                allMeetingFinished = []
                time = meetings[i][2]
            person1 = meetings[i][0]
            person2 = meetings[i][1]

            if person1 not in allMeetingFinished:
                allMeetingFinished.append(person1)
            if person2 not in allMeetingFinished:
                allMeetingFinished.append(person2)
            i+=1
        if allMeetingFinished:
            for p in allMeetingFinished:
                if who_know[p]:
                    for p in allMeetingFinished:
                        who_know[p] = True
                    break
        res = [] 
        for i in range(len(who_know)):
            if who_know[i] :
                res.append(i)
        return res


            
s = Solution()
res = s.findAllPeople(6,[[1,2,5],[2,3,8],[1,5,10]],1)
print(res)
