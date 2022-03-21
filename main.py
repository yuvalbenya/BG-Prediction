# This is a sample Python script.
import pandas as pd


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    df = pd.read_csv("/home/yuval/Desktop/amos/4.txt", skiprows=[0, 1], names=[1, 2, 3],
                     delim_whitespace=True, index_col=False)
    print(df)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
