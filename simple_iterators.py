from typing import Iterable, Iterator, Generator

people: list[str] = ['Bob', 'John', 'Tom']

people_iter: Iterator[str] = iter(people)

# print(list(people_iter))
print(f"List length: {len(people)}")
for i in range (len(people)):
    print(next(people_iter))
print(f"Check the list: {list(people_iter)}")

def say_hello(names: Iterable[str]) -> None:
    for name in names:
        print(f"Hello, {name}!")

print("Print list")
say_hello(["Bob", "Tom", "Tim", "Don", "Tim"])
print("\n\nPrint tuple")
say_hello(("Bob", "Tom", "Tim", "Don", "Tim"))
print("\n\nPrint set")
say_hello({"Bob", "Tom", "Tim", "Don", "Tim"})
