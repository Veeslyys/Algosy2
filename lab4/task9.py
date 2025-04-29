def compress_string(s):
    n = len(s)
    if n <= 1:
        return s

    dp = [""] * (n + 1)
    dp[0] = ""

    for i in range(1, n + 1):
        dp[i] = dp[i - 1] + s[i - 1]

        for l in range(1, i // 2 + 1):
            substring = s[i - l:i]
            count = 1
            j = i - l

            while j - l >= 0 and s[j - l:j] == substring:
                count += 1
                j -= l

            original_length = count * l
            compressed_part = f"{substring}*{count}" if count > 1 else substring
            compressed_length = len(compressed_part)
            total_length = len(dp[j]) + compressed_length

            if total_length < len(dp[i]):
                dp[i] = dp[j] + ("+" if j > 0 else "") + compressed_part

    return dp[n]


def main():
    import sys
    s = sys.stdin.readline().strip()
    print(compress_string(s))


main()