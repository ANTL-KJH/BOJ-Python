def solution(slice, n):
    answer = n // slice + 1 if n%slice != 0 else n//slice
    return answer