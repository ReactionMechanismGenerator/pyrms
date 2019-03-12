import sys
import os
from distutils.spawn import find_executable

#check rmgpy
os.system("conda install -c rmg --yes rmg")

julia_path = find_executable("julia")
if not julia_path:
    if True:
        julia_install_path = ""
        if julia_install_path == "":
            julia_install_path = os.path.join(os.getenv("HOME"),"julia","bin")
        elif not os.path.isfile(julia_install_path):
            raise ValueError("Julia path invalid")

        #install julia
        if os.getenv("OSTYPE") and os.getenv("OSTYPE") == "linux-gnu":
            os.system("""curl -L https://julialang-s3.julialang.org/bin/linux/x64/1.1/julia-1.1.0-linux-x86_64.tar.gz -o "$HOME/Downloads/julia.tar.gz";""")
            os.system("""tar xzf "$HOME/Downloads/julia.tar.gz" -C "$HOME/Downloads";""")
            os.system("""cp -r "$(find "$HOME/Downloads" -maxdepth 2 -name "julia*" -type d | head -n 1)" "{0}";""".format(os.path.join(julia_install_path,'julia')))
        elif os.getenv("OSTYPE") and "darwin" in os.getenv("OSTYPE"):
            os.system("""curl -L https://julialang-s3.julialang.org/bin/mac/x64/1.1/julia-1.1.0-mac64.dmg -o "$HOME/Downloads/julia.dmg";""")
            os.system("""hdiutil attach ~/Downloads/julia.dmg;""")
            os.system("""cp -r /Volumes/Julia*/Julia*/Contents/Resources/julia {0};""".format(os.path.join(julia_install_path,'julia')))
            os.system("""hdiutil detach -force /Volumes/Julia*;""")
        else:
            print("could not identify OS type attempting linux style install")
            os.system("""curl -L https://julialang-s3.julialang.org/bin/linux/x64/1.1/julia-1.1.0-linux-x86_64.tar.gz -o "$HOME/Downloads/julia.tar.gz";""")
            os.system("""tar xzf "$HOME/Downloads/julia.tar.gz" -C "$HOME/Downloads";""")
            os.system("""cp -r "$(find "$HOME/Downloads" -maxdepth 2 -name "julia*" -type d | head -n 1)" "{0}";""".format(os.path.join(julia_install_path,'julia')))

        os.system("export PATH=\"$HOME/julia/bin:$PATH\"")
