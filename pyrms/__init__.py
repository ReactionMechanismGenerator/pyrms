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
    subprocess.check_call(['julia', os.path.join(script_dir, 'install.jl')])
