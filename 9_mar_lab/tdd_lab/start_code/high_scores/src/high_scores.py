def latest(scores):
    return scores[-1]


def personal_best(scores):
    return max(scores)


def personal_top_three(scores):
    top_three = []
    top_three.extend(sorted((scores), reverse=True)[:3])
    return top_three

def ordered_list(scores):
    return sorted(scores, reverse=True)
