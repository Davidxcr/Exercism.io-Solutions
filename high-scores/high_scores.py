def latest(scores):
    return scores[-1]


def personal_best(scores):
    best = max(scores)
    return best


def personal_top_three(scores):
    top_three = sorted(scores, reverse=True)[:3]
    return top_three