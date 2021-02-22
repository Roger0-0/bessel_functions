#bessel_functions

###################################################
This is a interactive program that allows the user
to visualize the Bessel functions. In particular 
the program calculates the integral representation 
of the Bessel functions.

-Simply adjust the parameters under the 
constants section in the bessel.py file.
Then run the file by: python3 bessel.py
The Constants are explained below
###################################################

-For example adjust the MinX and MaxX values to 
change x range on the graph. The steps parameter
is the number of points to be plotted between 
MinX and MaxX, the higher the value the more 
"smooth" the plot appears at the cost of run time.

-MinM and MaxM to adjust the amount of Bessel 
functions plotted ie. F_m(x).

-The Simpson's rule parameters are probably best 
left alone, the a and b parameters will change 
the lower and upper bounds of the integral which 
will not change the shape of the function but rather
the y value range. The N parameter will change the 
iterations of Simpson's rule, reducing this value 
will decrease the accuracy of the integral, while 
increasing the value will increase the accuracy 
of the integral at the cost of run time. Don't 
change the h value as this is needed for Simpson's
rule to work any change will lead to unexpected 
results.

-Everything below the constants section is the code
that makes the program work I tried to add the 
necessary comments, but I do presume a prior 
knowledge of python, but feel free to hack away!

