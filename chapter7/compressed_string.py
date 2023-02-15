def solve(compressed_string):
    res = []
    count = 1
    for i in range(1, len(compressed_string)):
        if compressed_string[i - 1] == compressed_string[i]:
            count += 1
        else:
            for x in compressed_string:
                res = res.append(compressed_string) + compressed_string[i - 1]
                if count > 1:
                    res += count
                count = 1
        res = res + compressed_string[-1]
        if count > 1:
        res += count
    return res


s = ['a', 'b', 'd', 'd''d', 'e', 'a', 'a', 'b', 'd']
print(solve(s))
