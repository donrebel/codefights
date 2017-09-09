def firstDuplicate(a):
    d = [None] * len(a)
    min_idx = len(a)
    first_duplicate = -1
    for i in range(len(a)):
        if d[a[i] - 1]:
            if i < min_idx:
                min_idx = i
                first_duplicate = a[i]
        else:
            d[a[i] - 1] = True
    return first_duplicate

def firstNotRepeatingCharacter(s):
    order = []
    counts = {}
    res = '_'
    for c in s:
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
            order.append(c)
    i = 0
    found = False
    while i < len(order) and not found:
        if counts[order[i]] == 1:
            found = True
            res = order[i]
        i += 1
    return res

def rotateImage(a):
    n = len(a)
    for layer in range(len(a) // 2):
        first = layer
        last = n - 1 - layer
        for i in range(first, last):
            offset = i - first
            temp = a[first][i]
            a[first][i] = a[last - offset][first]
            a[last - offset][first] = a[last][last - offset]
            a[last][last - offset] = a[i][last]
            a[i][last] = temp
    return a

def sudoku2(grid):
    n = len(grid)
    m = len(grid[0])
    ts = 0
    # checking rows and columns
    for i in range(n):
        t_str = [None] * n
        t_col = [None] * n
        for j in range(n):
            ws = grid[i][:]
            wc = [x[j] for x in grid]
            v_str = grid[i][j]
            v_col = grid[j][i]
            if v_str != '.':
                if t_str[int(v_str) - 1]:
                    return False
                else:
                    t_str[int(v_str) - 1] = True
                    ts += int(v_str)
            if v_col != '.':
                if t_col[int(v_col) - 1]:
                    return False
                else:
                    t_col[int(v_col) - 1] = True
                    ts += int(v_col)
    # checking blocks 3x3
    for ks in range(n // 3):
        for kc in range(n // 3):
            s_offset = ks * 3
            c_offset = kc * 3
            t = [None] * n
            for i in range(3):
                for j in range(3):
                    v = grid[s_offset + i][c_offset + j]
                    if v != '.':
                        if t[int(v) - 1]:
                            return False
                        else:
                            t[int(v) - 1] = True
                            ts += int(v)
    return True


def isCryptSolution(crypt, solution):
    d = {}
    for s in solution:
        d[s[0]] = s[1]

    ces = []
    for c in crypt:
        ce = encrypt(c, d)
        if ce[0] == '0' and len(ce) > 1:
            return False
        else:
            ces.append(int(ce))

    return ces[0] + ces[1] == ces[2]

def encrypt(w, d_sol):
    res = ''
    for c in w:
        res += d_sol[c]
    return res


# ====================================
a = [2, 3, 3, 1, 5, 2]
assert firstDuplicate(a) == 3
a = [2, 4, 3, 5, 1]
assert firstDuplicate(a) == -1


s = "abacabad"
assert firstNotRepeatingCharacter(s) == 'c'
s = "abacabaabacaba"
assert firstNotRepeatingCharacter(s) == '_'


a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
assert rotateImage(a) == [[7, 4, 1],
                          [8, 5, 2],
                          [9, 6, 3]]


grid = [['.', '.', '.', '1', '4', '.', '.', '2', '.'],
        ['.', '.', '6', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '1', '.', '.', '.', '.', '.', '.'],
        ['.', '6', '7', '.', '.', '.', '.', '.', '9'],
        ['.', '.', '.', '.', '.', '.', '8', '1', '.'],
        ['.', '3', '.', '.', '.', '.', '.', '.', '6'],
        ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
        ['.', '.', '.', '5', '.', '.', '.', '7', '.']]
assert sudoku2(grid) == True
grid = [['.', '.', '.', '.', '2', '.', '.', '9', '.'],
        ['.', '.', '.', '.', '6', '.', '.', '.', '.'],
        ['7', '1', '.', '.', '7', '5', '.', '.', '.'],
        ['.', '7', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '8', '3', '.', '.', '.'],
        ['.', '.', '8', '.', '.', '7', '.', '6', '.'],
        ['.', '.', '.', '.', '.', '2', '.', '.', '.'],
        ['.', '1', '.', '2', '.', '.', '.', '.', '.'],
        ['.', '2', '.', '.', '3', '.', '.', '.', '.']]
assert sudoku2(grid) == False


crypt = ["SEND", "MORE", "MONEY"]
solution = [['O', '0'],
            ['M', '1'],
            ['Y', '2'],
            ['E', '5'],
            ['N', '6'],
            ['D', '7'],
            ['R', '8'],
            ['S', '9']]
assert isCryptSolution(crypt, solution) == True
crypt = ["TEN", "TWO", "ONE"]
solution = [['O', '1'],
            ['T', '0'],
            ['W', '9'],
            ['E', '5'],
            ['N', '4']]
assert isCryptSolution(crypt, solution) == False