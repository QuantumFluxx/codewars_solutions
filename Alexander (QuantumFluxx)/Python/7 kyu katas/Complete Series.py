def complete_series(seq):
    return list(range(0, max(seq)+1)) if len(set(seq)) == len(seq) else [0]