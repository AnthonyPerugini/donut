# create a 3-D projection of a torus using maths.

### project is not an original idea but this is my implementation.


By using maths, we can render a bunch of points along the surface of a virtual torus, we then project the points onto a virtual 2-D screen and do more maths to spin them.

We can then shade the points based on their normal projection towards the camera, parts of the torus facing the camra are rendered with denser ASCII
characters ('#','@', etc.), and one facing nearly perpendicular to the screen are rendered with less density ('.', ',', etc.).

Points with normal vectors pointing away from the screen and ones behind other portions of the torus are not rendered to improve performance and to keep the torus from 'bleeding though' itself.

In doing so, we can get a printout of the torus on the command line, spinning in all it's glory.
