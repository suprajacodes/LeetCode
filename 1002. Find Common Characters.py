'''
Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]
Example 2:

Input: words = ["cool","lock","cook"]
Output: ["c","o"]
'''


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        count = Counter(words[0])

        for i in words:
            count = count & Counter(i)
        return count.elements()


