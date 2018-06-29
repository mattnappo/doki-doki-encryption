import os
def clean(directory):
    directory = directory.lower()
    files = os.listdir(directory)
    for x in range(len(files)):
        f = files[x]
        if os.path.isdir(directory + "/" + f) == True:
            clean(directory + "/" + f)
        else:
            rem = directory + "/" + f
            os.remove(rem)
            print("Removed: " + rem)
    print("Done!")
