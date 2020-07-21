import os
import subprocess

script_dir = os.path.dirname(os.path.realpath(__file__))

def install():
    """
    Install Julia packages required for diffeqpy.
    """
    import julia
    import diffeqpy
    julia.install()
    diffeqpy.install()
    from julia.api import Julia
    jl = Julia(compiled_modules=False)
    from julia import Pkg
    Pkg.add("ReactionMechanismSimulator")
    from julia import ReactionMechanismSimulator
    
