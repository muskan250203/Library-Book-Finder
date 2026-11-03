import sys
BOOKS = [
    (1045, "Data Structures"),
    (1012, "Operating Systems"),
    (1099, "Computer Networks"),
    (1003, "Database Systems"),
    (1067, "Design and Analysis of Algorithms"),
    (1030, "Python Programming"),
    (1088, "Software Engineering"),
    (1021, "Discrete Mathematics"),
]

def bubble_sort(books):
    a = books[:]
    comparisons = 0
    n = len(a)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            comparisons += 1
            if a[j][0] > a[j + 1][0]:  # wrong order -> swap
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:                # already sorted, stop early
            break
    return a, comparisons

def linear_search(books, target_id):
    comparisons = 0
    for i, (book_id, _) in enumerate(books):
        comparisons += 1
        if book_id == target_id:
            return i, comparisons
    return -1, comparisons

def binary_search(books, target_id):
    low, high = 0, len(books) - 1
    comparisons = 0
    while low <= high:
        mid = (low + high) // 2
        comparisons += 1
        if books[mid][0] == target_id:
            return mid, comparisons
        elif books[mid][0] < target_id:
            low = mid + 1              # look in right half
        else:
            high = mid - 1             # look in left half
    return -1, comparisons

def show(books, heading):
    print(f"\n{heading}")
    for book_id, title in books:
        print(f"  {book_id}  {title}")

def report(name, books, index, comparisons, target):
    if index == -1:
        print(f"  {name:14s}: Book {target} NOT found  ({comparisons} comparisons)")
    else:
        print(f"  {name:14s}: Found '{books[index][1]}' at position {index + 1}  "
              f"({comparisons} comparisons)")

def compare_searches(unsorted_books, sorted_books, target):
    print(f"\nSearching for Book ID {target}")
    i, c = linear_search(unsorted_books, target)
    report("Linear Search", unsorted_books, i, c, target)
    i, c = binary_search(sorted_books, target)
    report("Binary Search", sorted_books, i, c, target)

def demo():
    print("=== Library Book Finder (demo) ===")
    show(BOOKS, "Catalogue (unsorted):")
    sorted_books, comps = bubble_sort(BOOKS)
    show(sorted_books, f"Catalogue after Bubble Sort ({comps} comparisons):")
    compare_searches(BOOKS, sorted_books, 1067)   # present
    compare_searches(BOOKS, sorted_books, 1099)   # present, last in sorted order
    compare_searches(BOOKS, sorted_books, 1050)   # absent

def menu():
    sorted_books, _ = bubble_sort(BOOKS)
    while True:
        print("\n=== Library Book Finder ===")
        print(" 1. Show catalogue (unsorted)")
        print(" 2. Sort catalogue (Bubble Sort)")
        print(" 3. Search a book (Linear vs Binary)")
        print(" 0. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            show(BOOKS, "Catalogue (unsorted):")
        elif choice == "2":
            result, comps = bubble_sort(BOOKS)
            show(result, f"Sorted catalogue ({comps} comparisons):")
        elif choice == "3":
            try:
                target = int(input("Enter Book ID: "))
            except ValueError:
                print("Please enter a number.")
                continue
            compare_searches(BOOKS, sorted_books, target)
        elif choice == "0":
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    demo() if "--demo" in sys.argv else menu()