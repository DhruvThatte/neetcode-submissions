class Solution:

  def validWordAbbreviation(self, word: str, abbr: str) -> bool:
    i, j = 0, 0
    m, n = len(word), len(abbr)

    while i < m and j < n:
      if abbr[j].isdigit():
        # Check for invalid leading zero
        if abbr[j] == '0':
          return False

        # Parse the complete number
        num = 0
        while j < n and abbr[j].isdigit():
          num = num * 10 + int(abbr[j])
          j += 1

        # Advance the word pointer by the parsed length
        i += num
      else:
        # Characters must match exactly
        if word[i] != abbr[j]:
          return False
        i += 1
        j += 1

    # Both pointers must reach the end exactly
    return i == m and j == n
