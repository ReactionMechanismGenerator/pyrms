import os
import subprocess

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
