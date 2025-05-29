from collections import deque

def check_polindrome(word):
    ### polindrome it's if the same backward and forward
    d = deque(word)
    # print(f"POP: {d.pop()}")
    # print(f"POPLEFT: {d.popleft()}")
    # print(f"D:{d}")
    while len(d)>1:
        print(f"Word: {d}")
        print(f"Length in iteration: {len(d)}")
        if d.pop() != d.popleft():
            return False
    return True   


def main():
    word = "tac0cat"
    print(check_polindrome(word))

if __name__== "__main__":
    main()