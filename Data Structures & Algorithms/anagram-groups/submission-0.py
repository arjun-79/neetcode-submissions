class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        new = [(sorted(strs[i]),i) for i in range(n)]
        new.sort()
        clubs = []
        group = [new[0][1]]
        for i in range(1,n):
            if (new[i][0] == new[i-1][0]):
                group.append(new[i][1])
            else:
                clubs.append(group)
                group = [new[i][1]]
        clubs.append(group)
        for i in range(len(clubs)):
            for j in range(len(clubs[i])):
                clubs[i][j] = strs[clubs[i][j]]
        return clubs

