from subprocess import check_output as A;import sys;G=Exception#git.io/JUVEE
class VersionError(G):0
class InstallError(G):0
E="Couldn't auto-install ";F=[sys.executable,"-m","pip","install"]
def requireit(B):
	for C in B:
		J=C if isinstance(C,str)else C[0]
		try:from importlib import import_module as L
		except ImportError:raise VersionError("⬆🐍")
		try: globals()[J]=L(J)
		except ModuleNotFoundError if sys.version_info.minor > 5 else ImportError:
			try:A(F+[C]) if isinstance(C,str)else A(F+[C[1]]);globals()[J]=L(J)
			except G:raise InstallError(E+J)
