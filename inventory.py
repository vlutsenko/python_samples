from collections import Counter

def main():
    # initial inventory
    inventory = Counter(STA001=10, SAL002=20, ENT004=13)
    # sales per week
    sales = Counter(SAL002=2, ENT004=1)
    inventory = inventory - sales
    #inventory update
    shiped_in = {"STA001":5, "STA002":17, "ENT005":33}
    inventory.update(shiped_in)
    ##actual stock
    print(inventory)

if __name__ == "__main__":
    main()