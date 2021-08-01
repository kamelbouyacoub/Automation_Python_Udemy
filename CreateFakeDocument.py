import os
nbr_document = 50
doc_number =0
documentCommunName ="document"
filesDirectory = "fakeFiles"

currentDir = os.path.curdir
path  = os.path.join(currentDir, filesDirectory)
try:
    os.mkdir(path)
except FileExistsError:
    print("Directory already exists")



for i in range(nbr_document):
    f = open(f"./{filesDirectory}/{documentCommunName}{doc_number}.java", "a")
    f = open(f"./{filesDirectory}/{documentCommunName}{doc_number}.py", "a")
    f = open(f"./{filesDirectory}/{documentCommunName}{doc_number}.txt", "a")
    doc_number+= 1
