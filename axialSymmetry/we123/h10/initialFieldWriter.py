

import sys
arg = str(sys.argv[1])
n=int( arg)
f = open('0/alpha.water','w')

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

f.write(");\n\n")

f.write("boundaryField\n")
f.write("{\n")
f.write("    symmetryAxis\n")
f.write("    {\n")
f.write("        type           symmetryPlane;\n")
f.write("    }\n")
f.write("    rightWall\n")
f.write("    {\n")
f.write("        type            zeroGradient;\n")
f.write("    }\n")
f.write("    lowerWall\n")
f.write("    {\n")
f.write("        type            zeroGradient;\n")
f.write("    }\n")
f.write("    atmosphere\n")
f.write("    {\n")
f.write("        type            inletOutlet;\n")
f.write("        inletValue      uniform 0;\n")
f.write("        value           uniform 0;\n")
f.write("    }\n")
f.write("    frontAndBack\n")
f.write("    {\n")
f.write("        type            empty;\n")
f.write("    }\n")
f.write("}\n")
f.write("\n\n// ************************************************************************* //")

f.close()
