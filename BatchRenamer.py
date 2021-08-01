from genericpath import isfile
import os;
 
search = "document"
replace = "file"
type_filter = ".txt"

dir_content = os.listdir('fakeFiles')
 
docs = [doc for doc in dir_content if os.path.isfile(f"./fakeFiles/{doc}")]
renamed = 0


print(f"{len(docs)} of {len(dir_content)} elements are files.")
for doc in docs:
    doc_name, filetype = os.path.splitext(doc)
    # print(f"doc_name == {doc_name} && filetype == {filetype}")
    if filetype == type_filter:
        if search in doc:
            new_name = doc_name.replace(search, replace)+ filetype
           
            os.rename(f"./fakeFiles/{doc}", f"./fakeFiles/{new_name}")
            renamed += 1
            print(f"Renamed file {doc} to {new_name}")

print(f"Renamed {renamed} of {len(docs)} files")