# create a 3-D projection of a torus using maths.

### project is not an original idea but this is my implementation.


By using projection of 3-d points across the surface of a spinning torus, we then project the torus onto a virtual 2-d screen.

By doing so, we are able to get a printout of the torus on the command line.

We shade the points based on their normal projection towards the camera, parts of the torus facing the camra are denser ASCII
characters ('#','@', etc.), and one facing nearly perpendicular to the screen are shaded lightly ('.', ',', etc.)

Parts of the torus behind other portions of the torus, and faces facing away from the camera are not drawn.
