import pandas as pd

f = open("4.txt", "r")
txt = f.read()
new_txt = txt.replace("\t", " ").strip().split("\n")
num_lines = sum(1 for line in open('4.txt'))
rows = []
# print((num_lines))
for i in range(num_lines):
    # print(new_txt[i])
    # print(i)
    split = new_txt[i].split(" ")
    rows.append(split)
# print(rows)

count = 0
vectors = []
# print()
for i in range(6, num_lines):
    # print(i)
    new_row = [rows[i][0], rows[i][1], [rows[i - 3][2], rows[i - 2][2], rows[i - 1][2], rows[i][2]]]
    vectors.append(new_row)
    # vectors.replace(vectors[i][2],[])
    # for j in range(4):
    # vectors[i][2].append(rows[i + 1][2])
    # vectors[i][2].append()
# print(vectors)
for i in vectors:
    print(i)
