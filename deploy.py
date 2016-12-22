import os
from glob import glob

home = os.environ["HOME"]

# copy the scripts to the user's home directory
for fn in glob(".*"):
    os.system("cp %s %s" % (fn,
                             os.path.join(home,
                                          fn)))

# create the static XML files
os.system("python3 %s > %s" % (os.path.join(home, ".menu.py"),
                               os.path.join(home, "menu.xml")))

os.system("python3 %s > %s" % (os.path.join(home, ".icons.py"),
                               os.path.join(home, "icons.xml")))
