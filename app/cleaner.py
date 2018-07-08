import os
def clean(directory):
    directory = directory.lower()
    files = os.listdir(directory)
    try:
        files.remove("bootstrap")
    except:
        pass
    for x in range(len(files)):
        f = files[x]
        if os.path.isdir(directory + "/" + f) == True:
            clean(directory + "/" + f)
        else:
            rem = directory + "/" + f
            os.remove(rem)
            print("Removed: " + rem)
    print("Done!")
def new(dir_name):
    with open("static/" + dir_name + "/.placeholder", "w+") as f:
        pass
dirs = ["encrypted", "decrypted", "uploads"]
for dir in dirs:
    new(dir)
