import numpy
import os
import argparse

def calculate_distance(atom1_coord, atom2_coord):
    """
    Calculate the distance between two three-dimensional points.
    """
    x_distance = atom1_coord[0] - atom2_coord[0]
    y_distance = atom1_coord[1] - atom2_coord[1]
    z_distance = atom1_coord[2] - atom2_coord[2]
    atom_distance = numpy.sqrt(x_distance ** 2 + y_distance ** 2 + z_distance ** 2)
    return atom_distance

def bond_check(atom_distance, minimum_length=0, maximum_length=1.5):
    
   
    if atom_distance > minimum_length and atom_distance <= maximum_length:
        return True
    else:
        return False

if __name__=="__main__":
    
    parser=argparse.ArgumentParser(description="This script analyzes a user given xyz file and outputs the length of the bonds.")
    parser.add_argument('xyz_file',help="The filepath for the xyz file to analyze.")
    args=parser.parse_args()

    def open_xyz(xyz_filename):
        xyz_file= numpy.genfromtxt(fname=xyz_filename, skip_header=2, dtype='unicode')
        symbols = xyz_file[:,0]
        coordinates = xyz_file[:, 1:]
        coordinates = coordinates.astype(numpy.float)
        return symbols, coordinates

    xyzfilename=args.xyz_file
    symbols, coords = open_xyz(xyzfilename)
    num_atoms = len(symbols)
    for num1 in range(0,num_atoms):
        for num2 in range(0,num_atoms):
            if num1<num2:
                atom_distance = calculate_distance(coords[num1],coords[num2])
                if bond_check(atom_distance) is True:
                    print(F'{symbols[num1]} to {symbols[num2]}: {atom_distance:.3f}') 