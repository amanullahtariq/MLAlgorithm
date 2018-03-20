def solve(a,b):
    score = [ai - bi for ai,bi in zip(a,b)]
    alice = len([x for x in score if x > 0])
    bob = len([x for x in score if x < 0])
    return  alice , bob




a = [5,6,7,8,2]
b = [3,6,10,4,9]

print (' '.join(map(str,solve(a,b))))
