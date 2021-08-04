class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        word_counter = Counter()

        new_word = [word for word in re.sub('[^\w]', ' ', paragraph).lower().split() if word not in banned]

        for word in new_word:
            word_counter[word] += 1

        return word_counter.most_common()[0][0]