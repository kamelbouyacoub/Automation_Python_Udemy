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
    f = open(f"./{filesDirectory}/{documentCommunName}{doc_number}.py", "x")
    doc_number+= 1
