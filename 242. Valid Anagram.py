#Approach 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
#Approach 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = sorted(s)
        s2 = sorted(t)
        return s1 == s2

#Approach 3
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)
        for i in s:
            count[i] = count[i] + 1
        for j in t:
            count[j] = count[j] - 1
        for k in count.values():
            if k != 0:
                return False
        return True

#Approach 4
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for i in s:
            count[ord(i) - ord('a')] += 1
        for j in t:
            count[ord(j) - ord('a')] -= 1
        for k in count:
            if k != 0:
                return False
        return True
