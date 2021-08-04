class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        items = defaultdict(list)

        for item in strs:
            items[''.join(sorted(item))].append(item)

        return list(items.values())