def fsm_search(pattern, text):
    n = len(text)
    m = len(pattern)
    transitions = compute_transitions(pattern)
    state = 0
    positions = []

    for i in range(n):
        while state > 0 and text[i] != pattern[state]:
            state = transitions[state - 1]
        if text[i] == pattern[state]:
            state += 1
        if state == m:
            positions.append(i - m + 1)
            state = transitions[state - 1]

    return positions


def compute_transitions(pattern):
    m = len(pattern)
    transitions = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and pattern[k] != pattern[q]:
            k = transitions[k - 1]
        if pattern[k] == pattern[q]:
            k += 1
        transitions[q] = k
    return transitions
