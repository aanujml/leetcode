from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter(s)
        result=""

        heap = []

        for ch, count in freq.items():
            heapq.heappush(heap, (-count, ch))
        for i in range(len(s)):

            count, ch = heapq.heappop(heap)
            if result and ch == result[-1]:
                if not heap:
                    return ""
                count2, ch2 = heapq.heappop(heap)
                result += ch2
                if count2 != -1:
                    heapq.heappush(heap, (count2 + 1, ch2))
                heapq.heappush(heap, (count , ch))
            else:
                result +=ch
                if count != -1:
                    heapq.heappush(heap, (count + 1, ch))
        return result