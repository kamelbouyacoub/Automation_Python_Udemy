from genericpath import isdir, isfile
import os;
import argparse;

parser = argparse.ArgumentParser(description= "Clean up directory and put file into according folders.")

parser.add_argument("--path",
                    type= str,
                    default=".",
                    help ="Directory path of the to be cleaned up directory")

args = parser.parse_args()
path = args.path

print(f"Cleaning up directory {path}")

dir_content = os.listdir(path)
path_dir_content = [os.path.join(path, doc) for doc in dir_content]
docs = [doc for doc in path_dir_content if os.path.isfile(doc)]
folders = [folder for folder in path_dir_content if os.path.isdir(folder)]
created_folder = []
print(folders)
moved = 0

print(f"Cleaning up {len(docs)} of {len(dir_content)} elements.")

for doc in docs:
    full_doc_path, filetype = os.path.splitext(doc)
    doc_path = os.path.dirname(full_doc_path)
    doc_name = os.path.basename(full_doc_path)

    if doc_name == "directory_clean":
        continue
    subfolder_path = os.path.join(path, filetype[1:].lower())
    print(subfolder_path)
    print(subfolder_path)
    if subfolder_path not in folders:
        try:
            os.mkdir(subfolder_path)
            created_folder.append(subfolder_path)
        except  FileExistsError as err:
            print(err)
    new_doc_path = os.path.join(subfolder_path, doc_name) + filetype
    os.rename(doc, new_doc_path)
    moved += 1

    print(f"Moved file {doc} to {new_doc_path}")

print(f"Renamed {moved} of {len(docs)} files.")