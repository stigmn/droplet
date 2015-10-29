

import sys
arg = str(sys.argv[1])
n=int( arg)
f = open('alpha.water','w')

f.write( "/*--------------------------------*- C++ -*----------------------------------*\\n")
f.write( "| =========                 |                                                 |\n")
f.write( "| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |\n")
f.write( "|  \\    /   O peration     | Version:  2.4.0                                 |\n")
f.write( "|   \\  /    A nd           | Web:      www.OpenFOAM.org                      |\n")
f.write( "|    \\/     M anipulation  |                                                 |\n")
f.write( "\*---------------------------------------------------------------------------*/\n")
f.write( "FoamFile\n")
f.write( "{\n")
f.write( "    version     2.0;\n")
f.write( "    format      ascii;\n")
f.write( "    class       volScalarField;\n")
f.write( "    location    0;\n")
f.write( "    object      alpha.water;\n")
f.write( "}\n")
f.write( "// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //\n")
f.write("\n")
f.write( "dimensions      [0 0 0 0 0 0 0];\n")
f.write( "internalField   nonuniform List<scalar>\n")
f.write( str(n))
f.write( "\n")
f.write( "( \n")

# Loop to write correct number of zeros!



i=0;
while i<n:
    f.write("0\n")
    i=i+1;

f.write(") ")
f.close()


