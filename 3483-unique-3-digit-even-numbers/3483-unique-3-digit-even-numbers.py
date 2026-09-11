from collections import Counter
from typing import List


class Solution:

  def totalNumbers(self, digits: List[int]) -> int:
    available = Counter(digits)
    count = 0

    # Iterate through all 3-digit even numbers
    for num in range(100, 1000, 2):
      d1 = num // 100
      d2 = (num // 10) % 10
      d3 = num % 10

      needed = Counter([d1, d2, d3])

      # Verify that we have enough of each digit available
      if all(available[d] >= freq for d, freq in needed.items()):
        count += 1

    return count