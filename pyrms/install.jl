using Pkg

#get the python path
if !("PyCall" in keys(Pkg.installed()))
    Pkg.add("PyCall")
end
out = Pipe()
proc = run(pipeline(`which python`,stdout=out))
close(out.in)
pypath = chomp(String(read(out)))

#set env variables for installing PyCall
ENV["CONDA_JL_HOME"] = join(split(pypath,'/')[2:end-2],'/')
ENV["PYTHON"] = pypath

Pkg.build("PyCall")

Pkg.develop(PackageSpec(url="https://github.com/ReactionMechanismGenerator/ReactionMechanismSimulator.jl"))
using PyCall
using ReactionMechanismSimulator
