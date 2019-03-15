import sys
import os
from distutils.spawn import find_executable

#check python version
t='{v[0]}'.format(v=list(sys.version_info[:2]));sys.stdout.write(t)

if t != '2':
    raise ValueError("current python is not python 2, pyrms can only be installed on python 2")

#check rmgpy
try:
    import rmgpy
except:
    x = raw_input("could not find rmg in PYTHONPATH, if you have rmg installed from source this could be a problem, \
                  should we do a binary install? indicate yes with 'y'")
    if x != 'y':
        raise ValueError("stopping install so you can add rmgpy to PYTHONPATH")
    else:
        os.system("conda install -c rmg --yes rmg")

append_pyrms = raw_input("Would you like pyrms appended to PYTHONPATH in your .bashrc (linux) .bash_profile (osx)? (recommended) \
              indicate yes with 'y'")

if append_pyrms  == 'y':
    print("appending pyrms to path")
    path=os.getcwd()
    homepath = os.getenv("HOME")
    ostype = sys.platform
    if "darwin" in ostype:
        bpath = os.path.join(homepath,".bash_profile")
    else:
        bpath = os.path.join(homepath,".bashrc")
    st = "#pyrms\nexport PYTHONPATH=$PYTHONPATH:{0}".format(path)
    with open(bpath, 'a') as bfile:
        bfile.write(st)

julia_path = find_executable("julia")
if not julia_path:
    install_julia = raw_input("julia not appended to path, do you want pyrms to install julia?  indicate yes with 'y'")
    if install_julia == 'y':
        julia_install_path = raw_input("At what absolute path would you like julia installed? blank defaults to $HOME")
        if not julia_install_path:
            julia_install_path = os.path.join(os.getenv("HOME"))#,"julia","bin")
        elif not os.path.isfile(julia_install_path):
            raise ValueError("Julia path invalid")

        append_julia = raw_input("Would you like julia appended to path in your .bashrc (linux) .bash_profile (osx)? (recommended)\
                      indicate yes with 'y'")

        #install julia
        if sys.platform and "linux" in sys.platform:
            os.system("""curl -L https://julialang-s3.julialang.org/bin/linux/x64/1.1/julia-1.1.0-linux-x86_64.tar.gz -o "$HOME/Downloads/julia.tar.gz";""")
            os.system("""tar xzf "$HOME/Downloads/julia.tar.gz" -C "$HOME/Downloads";""")
            os.system("""mkdir -p {0}""".format(os.path.join(julia_install_path,'julia')))
            os.system("""cp -r "$(find "$HOME/Downloads" -maxdepth 2 -name "julia*" -type d | head -n 1)" "{0}";""".format(os.path.join(julia_install_path,'julia')))
        elif sys.platform and "darwin" in sys.platform:
            os.system("""curl -L https://julialang-s3.julialang.org/bin/mac/x64/1.1/julia-1.1.0-mac64.dmg -o "$HOME/Downloads/julia.dmg";""")
            os.system("""hdiutil attach ~/Downloads/julia.dmg;""")
            os.system("""mkdir -p {0}""".format(os.path.join(julia_install_path,'julia')))
            os.system("""cp -r /Volumes/Julia*/Julia*/Contents/Resources/julia {0};""".format(os.path.join(julia_install_path,'julia')))
            os.system("""hdiutil detach -force /Volumes/Julia*;""")
        else:
            print("could not identify OS type attempting linux style install")
            os.system("""curl -L https://julialang-s3.julialang.org/bin/linux/x64/1.1/julia-1.1.0-linux-x86_64.tar.gz -o "$HOME/Downloads/julia.tar.gz";""")
            os.system("""tar xzf "$HOME/Downloads/julia.tar.gz" -C "$HOME/Downloads";""")
            os.system("""mkdir -p {0}""".format(os.path.join(julia_install_path,'julia')))
            os.system("""cp -r "$(find "$HOME/Downloads" -maxdepth 2 -name "julia*" -type d | head -n 1)" "{0}";""".format(os.path.join(julia_install_path,'julia')))

        if append_julia == 'y':
            print("appending julia to path julia")
            homepath = os.getenv("HOME")
            ostype = sys.platform
            if ostype and "darwin" in ostype:
                bpath = os.path.join(homepath,".bash_profile")
            else:
                bpath = os.path.join(homepath,".bashrc")
            st = "#julia\nexport PATH=\"{0}:$PATH\"".format(os.path.join(homepath,"julia","bin"))
            with open(bpath, 'a') as bfile:
                bfile.write(st)
        else:
            raise ValueError("Cannot continue installation without appending julia to path")
    else:
        raise ValueError("append your julia executable to path")
