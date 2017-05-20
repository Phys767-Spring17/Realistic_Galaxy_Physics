# Unrealistic Galaxy Physics

## Repository Purpose

The essential aim of this project was to make a visualization of two spiral galaxies rotating in opposite directions
in 3 dimensional space with some degree of thickness. All of these aims are fulfilled in "ThickGalaxies.mp4".

## Important Notes

The main functions used in this code are drawn from Mr. Zingale's spiral_windup tutorial found at:
https://github.com/zingale/astro_animations/blob/master/galaxies/spiral_windup/spiral_windup.py

Spirals.py produces 500 png images. To transform them into an animation, I used the following command:

'''
ffmpeg -r 60 -f image2 -s 1920x1080 -i Spirals_%04d.png -vcodec libx264 -crf 25 -pix_fmt yuv420p ThickGalaxies.mp4
'''

## Repository Components

This repository contains a directory named "ThickGalaxy". Inside this directory is the main code "Spirals.py"
and the associated test "test_Spirals.py". Aside from this directory, there are 10 .mp4 files, which are animations
resulting from simulations due to different stages of my Spirals.py code. A brief explanation of how these other
.mp4 files are obtained is given in the comments of Spirals.py. Currently, the only .mp4 file that corresponds to
Spirals.py is "ThickGalaxies.mp4"

## Project Process and Phases

I began by using Mr. Zingale's tutorial, which revealed that one could make a two dimensional visualization of a
spiral by simply varying the velocity of points with radii (higher velocity to the center and lower velocity further
out) and by plotting the x and y coordinates as functions of cosine and sine respectively.

I created redgalaxy.mp4 by changing the solid blue line in the tutorial into 10 red dots. I did this in order to
represent stars. I then created galaxy.mp4 by plotting 3 different colored lines, each composed of 10 dots, to
represent different stars in a galaxy. Next, I changed the number of dots for each of the three lines and this
resulted in star_distribution.mp4. By changing the location of the lines, I was able to show three galaxies spiraling
in the same direction, which is the result 3Galaxy.mp4. Opposite.mp4 is the result of removing one of the galaxies
and making the two galaxies rotate in opposite directions.

The next step was to make my 2-d visualization into 3-d. My original plan was to add more lines to each galaxy to show
other colors and depth. However, as one can see in AzimuthView.mp4, where the camera rotates 360 degrees around along
the azimuth-direction, there seem to be some bugs. This problem continued in Galaxies.mp4, where the camera moves 360
degrees along elevation-direction, where the code does not work in the way it is supposed to. Ultimately, I chose to
simply stick to the idea of two galaxies made of solid lines and this resulted, after removing the axis, in
SpiralGalaxies.mp4. When I reincorporated the grid and rectified the z-axis ambiguity, GalaxyGrid.mp4 resulted. Finally,
I gave thickness to each of the galaxies and this became ThickGalaxies.mp4.








