#第一种解法利用广度优先，代码抄书上的所以变量名有点乱
from collections import deque  
class dd():
    def search(self,start,end,*ad):
        adict = list(ad)
        graph = {}
        adict.insert(0,start)
        for dot in range(0,len(adict)):
            graph[adict[dot]] = []
            for neighbour in range(0,len(adict)):
                xiangsidu = 0
                for i in range(0,len(adict[dot])):
                    if adict[dot][i] == adict[neighbour][i]:
                        xiangsidu += 1 
                    if xiangsidu == len(adict[dot])-1:
                        graph[adict[dot]].append(adict[neighbour])
        for key in graph.keys():
            graph[key] = list(set(graph[key]))
        for key,value in graph.items():
            if start in value:
                graph[key].remove(start)  
            if key in value:
                graph[key].remove(key)
        search_queue = deque()
        search_queue += graph[start]
        searched = [start]
        line = []
        while search_queue :
            person = search_queue.popleft()
            if person not in searched:
                if self.person_is(person,end):
                    while person != start:
                        for key,value in graph.items():
                            if person in value and key in searched :
                                line.append(person)
                                person = key
                                break
                    line.reverse()
                    return line
                else:
                    search_queue += graph[person]
                    searched.append(person)
        return False
    def person_is(self,this_word,end):
        if this_word == end:
            return True
        for letter in range(0,len(this_word)):
            panduan = this_word
            for i in range(0,27):
                panduan = panduan[0:letter] + chr(97+i) +panduan[letter+1:]
                if panduan == end:
                    return True
        return False

a = dd()
print(a.search('hit','cog','hot','dot','dog','lot','log'))
print(a.search('adf','skc','err','adf','cvj','adc','sdc'))






