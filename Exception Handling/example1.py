
try:
    f = open('testfile.txt', 'r')
    f.write("Test line")

except TypeError:
    print("There is a type error")

# OS error because file is open only in read mode and we are trying to write
except OSError:
    print("There is an IO error")

finally:
    print("This will always run")