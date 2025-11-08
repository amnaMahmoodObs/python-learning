# GitHub Copilot
# Examples covering list slicing in Python

L = list(range(10))            # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print("L =", L)

# Basic slices: [start:stop) semantics
print("L[2:5] ->", L[2:5])     # [2, 3, 4]
print("L[:3]  ->", L[:3])      # [0, 1, 2]
print("L[5:]  ->", L[5:])      # [5, 6, 7, 8, 9]

# Step parameter: [start:stop:step]
print("L[::2] ->", L[::2])     # every 2nd element
print("L[1::2] ->", L[1::2])   # every 2nd starting at index 1
print("L[2:8:3] ->", L[2:8:3]) # step of 3

# Negative indices
print("L[-3:] ->", L[-3:])     # last 3 elements
print("L[:-3] ->", L[:-3])     # up to but not including last 3

# Reversing
print("L[::-1] ->", L[::-1])   # reversed list

# Negative step with explicit bounds
print("L[7:2:-1] ->", L[7:2:-1])  # elements 7 down to 3

# Slice object
s = slice(2, 9, 2)
print("slice(2,9,2) ->", L[s])

# Copying a list
copy1 = L[:]       # shallow copy
copy2 = L.copy()   # also a shallow copy
print("copy1 == L ->", copy1 == L, "but is copy1 L? ->", copy1 is L)

# Assigning to slices (can change list length)
A = [0,1,2,3,4,5,6]
print("A =", A)
A[2:5] = ['a', 'b']    # replaces elements 2..4 with 2 new items (length changes)
print("After A[2:5] = ['a','b'] ->", A)

# Deleting a slice
del A[1:3]
print("After del A[1:3] ->", A)

# Assigning to extended slice (step != 1) requires matching lengths
B = list(range(10))
print("B before ->", B)
B[::2] = [100]*5       # there are 5 positions in B[::2], so assignment length must match
print("B after B[::2] = [100]*5 ->", B)

# If lengths don't match you'll get ValueError:
try:
    B[::2] = [1,2]     # wrong length
except ValueError as e:
    print("ValueError (expected):", e)

# Practical: extract a window (safe with boundaries)
def window(lst, center, radius):
    start = max(0, center - radius)
    end = center + radius + 1
    return lst[start:end]

print("window(L, 5, 2) ->", window(L, 5, 2))  # [3,4,5,6,7]