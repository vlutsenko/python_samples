from collections import namedtuple, defaultdict

from pprint import pprint

def get_dict(list_to_cat):
    res = defaultdict(lambda: set())
    for item in list_to_cat:
        cat = item.identifier[0:3]
        match cat:
            case "STA":
                res["starter"].add(item)
            case "BEV":
                res["beverage"].add(item)
            case "SAL":
                res["salad"].add(item)
            case "ENT":
                res["entree"].add(item)
    return res


def main():
    Food = namedtuple("Food", ["identifier","name"])

    menu_list = [
        Food("STA001", "asasdasd 1"),
        Food("STA002","asdads 2"),
        Food("STA003", "asdrwerwr 3"),
        Food("SAL001", "asasdasd 4"),
        Food("SAL002","asdads 5"),
        Food("SAL003", "asdrwerwr 6"),
        Food("ENT001", "asasdasd 7"),
        Food("ENT002","asdads 8"),
        Food("ENT003", "asdrwerwr 9"),
        Food("BEV001", "asasdasd 10"),
        Food("BEV002","asdads 11"),
        Food("BEV003", "asdrwerwr 12")
    ]

    pprint(dict(get_dict(menu_list)))

if __name__=="__main__":
    main()

