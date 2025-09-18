# checkmate.py

def is_king_in_check(board):
   
    n = len(board)
    # หา King
    king_pos = None
    for r in range(n):
        for c in range(n):
            if board[r][c] == 'K':
                king_pos = (r, c)
                break
        if king_pos:
            break
    if not king_pos:
        # ไม่มี King บนกระดาน
        return False

    kr, kc = king_pos

    def in_bounds(r, c):
        return 0 <= r < n and 0 <= c < n

    #  ตรวจ Rook / Queen (แนวตรง)
    directions_rook = [(-1,0),(1,0),(0,-1),(0,1)]
    for dr, dc in directions_rook:
        r, c = kr + dr, kc + dc
        while in_bounds(r, c):
            ch = board[r][c]
            if ch != '.':
                if ch in ('R','Q'):
                    return True
                break
            r += dr
            c += dc

    #  ตรวจ Bishop / Queen (แนวทแยง)
    directions_bishop = [(-1,-1),(-1,1),(1,-1),(1,1)]
    for dr, dc in directions_bishop:
        r, c = kr + dr, kc + dc
        while in_bounds(r, c):
            ch = board[r][c]
            if ch != '.':
                if ch in ('B','Q'):
                    return True
                break
            r += dr
            c += dc

    #  ตรวจ Knight (N ล้อม 8 ทิศ) — ไม่ได้ใช้ในโจทย์ แต่เพิ่มไว้เผื่อ
    knight_moves = [(-2,-1),(-2,1),(-1,-2),(-1,2),
                    (1,-2),(1,2),(2,-1),(2,1)]
    for dr, dc in knight_moves:
        r, c = kr + dr, kc + dc
        if in_bounds(r, c) and board[r][c] == 'N':
            return True

    #  ตรวจ Pawn (สมมุติ Pawn เดินจากบนลงล่าง)
    for dr, dc in [(-1,-1),(-1,1)]:
        r, c = kr + dr, kc + dc
        if in_bounds(r, c) and board[r][c] == 'P':
            return True

    return False
