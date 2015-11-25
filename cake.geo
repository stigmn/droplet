Point(1) = {0, 0, 0, 1.0};
Point(2) = {50, 0, 0, 1.0};
Line(1) = {1, 2};
Rotate {{0, 0, 1}, {0, 0, 0}, -0.04363323129985824} {
  Line{1};
Layers{1};
Recombine;
}
Extrude {{0, 0, 1}, {0, 0, 0}, 0.08726646259971647} {
  Line{1};
//Layers{1};
}
Extrude {0, 0, 100} {
  Surface{4};
 // Layers{1};
 // Recombine;
}
Physical Surface("top") = {21};
Physical Surface("front") = {16};
Physical Surface("bottom") = {4};
Physical Surface("left") = {12};
Physical Surface("right") = {20};
Physical Volume("volume") = {1};