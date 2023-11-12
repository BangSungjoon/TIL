def count_score(cards, target_range):
    n = len(cards)
    count = 0

    for i in range(1 << n):
        score = 0
        for j in range(n):
            if i & (1 << j):  
                score -= cards[j]
            else:
                score += cards[j]

        if target_range[0] <= score <= target_range[1]:
            count += 1

    return count