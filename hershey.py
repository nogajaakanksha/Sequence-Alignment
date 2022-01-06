from needleman import *

def hirschberg(X,Y):
    overall_penalty = 0
    align1 = ""
    align2 = ""
    l1 = len(X)
    l2 = len(Y)

    if l1 == 0:
        for i in range(l2):
            align1 += '_'
            align2 += Y[i]
            overall_penalty += delta

    elif l2 == 0:
        for i in range(l1):
            align1 = align1 + X[i]
            align2 = align2 + '_'
            overall_penalty += delta

    elif l1 == 1 or l2 == 1:
        penalty, n1, n2 = needleman(X,Y)
        overall_penalty += penalty
        align1 += n1
        align2 += n2

    else:
        # Divide
        xmid = int(l1/2)
        scoreL = scores(X[:xmid], Y)
        scoreR = scores(X[xmid:][::-1], Y[::-1])
        ymid = get_mid(scoreL, scoreR)

        # Conquer
        hleft = hirschberg(X[:xmid], Y[:ymid])
        hright = hirschberg(X[xmid:], Y[ymid:])

        # Combine
        overall_penalty = hleft[0] + hright[0]
        align1 = hleft[1] + hright[1]
        align2 = hleft[2] + hright[2]

    return overall_penalty, align1, align2

def scores(seqa, seqb):
        lena = len(seqa)+1
        lenb = len(seqb)+1
        pre_row = [0] * lenb
        cur_row = [0] * lenb

        for j in range(1, lenb):
            pre_row[j] = pre_row[j - 1] + delta

        for i in range(1, lena):
            cur_row[0] = delta + pre_row[0]
            for j in range(1, lenb):
                mismatch = pre_row[j - 1] + alpha(seqa[i - 1], seqb[j - 1])
                insert = cur_row[j - 1] + delta
                delete = pre_row[j] + delta
                cur_row[j] = min(mismatch, insert, delete)
            pre_row = cur_row
            cur_row = [0] * lenb
        return pre_row

def get_mid(scoreL, scoreR):
    scoreR.reverse()
    row = [l + r for l, r in zip(scoreL, scoreR)]
    maxidx, maxval = min(enumerate(row), key=lambda a: a[1])
    return maxidx
