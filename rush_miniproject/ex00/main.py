# main.py
from checkmate import is_king_in_check

def main():
    try:
        board = []
        while True:
            line = input().rstrip('\n')
            if not line:   # ถ้าเจอแถวว่าง ให้หยุดอ่าน
                break
            board.append(line)
    except EOFError:
        pass

    if not board:
        print("Fail")  # ไม่มีข้อมูล

    else:
        if is_king_in_check(board):
            print("Success")
        else:
            print("Fail")

if __name__ == "__main__":
    main()