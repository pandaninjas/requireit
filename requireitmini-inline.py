exec('from subprocess import check_output as A;import sys;G=Exception\nclass VersionError(G):0\nclass InstallError(G):0\nE="Couldn\'t auto-install ";F=[sys.executable,"-m","pip","install"]\ndef requireit(B):\n\tfor C in B:zJ=C if isinstance(C,str)else C[0]ztry:from importlib import import_module as Lzexcept ImportError:raise VersionError("⬆🐍")ztry: globals()[J]=L(J)zexcept ModuleNotFoundError if sys.version_info.minor > 5 else ImportError:z\ttry:A(F+[C]) if isinstance(C,str)else A(F+[C[1]]);globals()[J]=L(J)z\texcept G:raise InstallError(E+J)'.replace("z", "\n\t\t"))#git.io/JUVEE
