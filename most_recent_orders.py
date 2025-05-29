from collections import deque

def main():
    #define length of the deque
    foods = deque(maxlen=5)
    #add first order
    foods.append("STA001")
    #add set of orders
    ordered_foods = ["DES001","DES002","STA002","ENT001"]
    foods.extend(ordered_foods)
    #add one more order
    foods.append("DES005")
    print(foods)
    #append to the left
    foods.appendleft("SAL011")
    print(foods)
    return
if __name__ == "__main__":
    main()