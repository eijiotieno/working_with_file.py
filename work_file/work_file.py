import os
import shutil
import datetime
import time
from datetime import date, time, timedelta
from os import path


def main():

    # Create a file
    f = open("guru99.txt", "w+")

    # Add data into file
    for i in range(10):
        f.write("This is line %d\r\n" % (i + 1))
    # Append data
    f = open("guru99.txt", "a+")
    for i in range(2):
        f.write("Append line %d\r\n" % (i + 1))

    f = open("guru99.txt", "r")
    if f.mode == "r":
        content = f.read()
    for i in range(2):
        f.write("Append line %d\r\n" % (i + 1))
    print(content)
    # Close app
    f.close()
    # Readlines in the file
    f1 = f.readlines()
    for x in f1:
        print(x)
    # Copy file
    if path.exists("guru99.txt"):
        src = path.realpath("guru99.txt")

    head, tail = path.split(src)
    print("path: " + head)
    print("file: " + tail)

    dst = src + ".bak"

    shutil.copy(src, dst)
    shutil.copystat(src, dst)
    t = time.ctime(path.getmtime("guru99.txt.bak"))
    print(t)
    print(datetime.datetime.fromtimestamp(path.getmtime("guru99.txt.bak")))


if __name__ == "__main__":
    main()
