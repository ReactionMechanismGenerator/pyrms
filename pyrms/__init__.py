import shutil
from subprocess import run
# juliacall must be loaded after `_ensure_julia_installed()` is run,
# so this import is in `load_julia_packages()`
# from juliacall import Main

def _find_julia():
    return shutil.which("julia")

def _ensure_julia_installed():
    if not _find_julia():
        print("No Julia version found. Installing Julia.")
        run("juliaup update")
        if not _find_julia():
            raise RuntimeError(
                "Julia installed with jill but `julia` binary cannot be found in the path"
            )

# TODO: upstream this function or an alternative into juliacall
def load_julia_packages(*names):
    """
    Load Julia packages and return references to them, automatically installing julia and
    the packages as necessary.
    """
    # This is terrifying to many people. However, it seems SciML takes pragmatic approach.
    _ensure_julia_installed()

    script = """import Pkg
    Pkg.activate(\"pyrms\", shared=true)
    try
        import {0}
    catch e
        e isa ArgumentError || throw(e)
        Pkg.add([{1}])
        import {0}
    end
    {0}""".format(", ".join(names), ", ".join(f'"{name}"' for name in names))

    # Unfortunately, `seval` doesn't support multi-line strings
    # https://github.com/JuliaPy/PythonCall.jl/issues/433
    script = script.replace("\n", ";")

    # Must be loaded after `_ensure_julia_installed()`
    from juliacall import Main
    return Main.seval(script)
