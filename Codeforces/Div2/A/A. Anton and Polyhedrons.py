# https://codeforces.com/problemset/problem/785/A
n = int(input()); count = 0
for i in range(n):
    polyhedrons = input()
    # polyhedrons[0] == "T"
    if polyhedrons == "Tetrahedron":
        count += 4
    elif polyhedrons == "Cube":
        count += 6
    elif polyhedrons == "Octahedron":
        count += 8
    elif polyhedrons == "Dodecahedron":
        count += 12
    elif polyhedrons == "Icosahedron":
        count += 20
print(count)