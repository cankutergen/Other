def partitionLabels(S: str):

    # a:8, b:5, ....., e: 15, ...., j:23
    # ababcbacadefegdehijhklij
    # 012345678      15         

    dict = {}
    for i, char in enumerate(S):
        dict[char] = i
        
    left, right = 0, 0


    result = []
    for i, char in enumerate(S):

        right = max(right, dict[char])

        if i == right:
            result += [right - left + 1]
            left = i + 1

    return result
