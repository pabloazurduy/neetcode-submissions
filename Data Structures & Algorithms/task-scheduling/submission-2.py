from collections import Counter
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        max_heap = [-cnt for cnt in count.values()]
        heapq.heapify(max_heap) # get the smallest element at the top 

        time = 0
        q = deque()  # pairs of [-cnt, idleTime]
        while max_heap or q:
            time += 1

            if not max_heap:
                time = q[0][1]
            else:
                cnt = 1 + heapq.heappop(max_heap) # will pop the first element (whatever it is, and then will heapify the remaining)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time