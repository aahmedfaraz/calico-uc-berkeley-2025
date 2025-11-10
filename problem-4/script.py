# Reading input file
with open("input.txt", "r") as file:
    lines = file.readlines()
    lines = [line for line in lines if line.strip()]

# Required variables
test_cases = int(lines.pop(0))
results = []

# All Functions
def is_blocked_by_other_pieces(piece1, piece2, all_pieces):
    type1, i1, j1 = piece1
    type2, i2, j2 = piece2

    if type1 == "R":  # Rook
        if i1 == i2:  # Same row
            for k in range(min(j1, j2) + 1, max(j1, j2)):
                if any(p[1] == i1 and p[2] == k for p in all_pieces if p != piece1 and p != piece2):
                    return True
        elif j1 == j2:  # Same column
            for k in range(min(i1, i2) + 1, max(i1, i2)):
                if any(p[1] == k and p[2] == j1 for p in all_pieces if p != piece1 and p != piece2):
                    return True

    elif type1 == "B":  # Bishop
        if abs(i1 - i2) == abs(j1 - j2):
            step_i = 1 if i2 > i1 else -1
            step_j = 1 if j2 > j1 else -1
            for k in range(1, abs(i1 - i2)):
                if any(p[1] == i1 + k * step_i and p[2] == j1 + k * step_j for p in all_pieces if p != piece1 and p != piece2):
                    return True

    elif type1 == "Q":  # Queen
        if i1 == i2 or j1 == j2:
            return is_blocked_by_other_pieces(( "R", i1, j1), (type2, i2, j2), all_pieces)
        elif abs(i1 - i2) == abs(j1 - j2):
            return is_blocked_by_other_pieces(( "B", i1, j1), (type2, i2, j2), all_pieces)

    return False

def is_attacking(piece1, piece2, all_pieces):
    if is_blocked_by_other_pieces(piece1, piece2, all_pieces):
        return False

    type1, i1, j1 = piece1
    type2, i2, j2 = piece2

    if type1 == "R":  # Rook
        return i1 == i2 or j1 == j2
    elif type1 == "B":  # Bishop
        return abs(i1 - i2) == abs(j1 - j2)
    elif type1 == "Q":  # Queen
        return i1 == i2 or j1 == j2 or abs(i1 - i2) == abs(j1 - j2)
    return False

# Main processing loop
for i in range(1, test_cases + 1):
    total_attacks = 0
    all_pieces = []
    m, n = map(int, lines.pop(0).strip().split())
    total_pieces = int(lines.pop(0).strip())
    # print("Case", i, ": ", "m =", m, ", n =", n, ", total pieces =", total_pieces)

    for piece in range(total_pieces):
        t, r, c = lines.pop(0).strip().split()
        r, c = int(r), int(c)
        # print("Piece", piece + 1, ": Type =", t, ", r =", r, ", c =", c)
        all_pieces.append((t, r, c))
    # print("All pieces for Case", i, ":", all_pieces)

    for p1 in range(len(all_pieces)):
        for p2 in range(len(all_pieces)):
            if p1 != p2:
                if is_attacking(all_pieces[p1], all_pieces[p2], all_pieces):
                    total_attacks += 1

    # Writing output file
    results.append(total_attacks)

with open("output.txt", "w") as file:
    file.write("\n".join(map(str, results)))
