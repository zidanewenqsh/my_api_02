import shutil
src = r"./src/a.txt"
dst = r"./dst"
# shutil.copy(src,dst)
shutil.copy2(src,dst)