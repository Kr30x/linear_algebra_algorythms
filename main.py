from numpy import transpose
from core.algo.find_basis import find_basis
from core.io.cli import mprint
from core.io.file import input_vectors, input_matrix
from core.sv import to_usv
from fractions import Fraction

a = input_vectors("matrix.txt", dtype = Fraction)

b = find_basis(a, indexing = True)
mprint(b)
