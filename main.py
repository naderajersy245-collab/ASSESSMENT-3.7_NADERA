full_name = "JERSY NADERA"

# Unsorted array: letters only, no duplicates
unsorted = []
for ch in full_name.upper():
    if ch.isalpha() and ch not in unsorted:
        unsorted.append(ch)

# Selection Sort
sorted_arr = unsorted[:]
for i in range(len(sorted_arr) - 1):
    smallest = i
    for j in range(i + 1, len(sorted_arr)):
        if sorted_arr[j] < sorted_arr[smallest]:
            smallest = j
    sorted_arr[i], sorted_arr[smallest] = sorted_arr[smallest], sorted_arr[i]

print("Unsorted array:", unsorted)
print("Sorted array:  ", sorted_arr)