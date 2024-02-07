def maxNumberOfBalloons(text: str) -> int:
    def max_patterns(pattern):
        ans = float('inf')
        text_freq = [0] * 26
        pattern_freq = [0] * 26

        for i in range(len(pattern)):
            pattern_freq[ord(pattern[i]) - ord('a')] += 1

        for i in range(len(text)):
            text_freq[ord(text[i]) - ord('a')] += 1

        for i in range(len(text_freq)):
            if pattern_freq[i] > 0:
                ans = min(ans, text_freq[i] // pattern_freq[i])

        return ans

    ptrn = 'balloon'
    return max_patterns(ptrn)


if __name__ == '__main__':
    text = "leetcode"
    print(maxNumberOfBalloons(text))
