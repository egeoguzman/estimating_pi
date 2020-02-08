## Estimating Pi with Python ###

![estimating_pi_graph](https://user-images.githubusercontent.com/32989239/74083540-4b692600-4a76-11ea-9241-ce892319cf18.png)

##Explanation

<ul>
<li>Unit circle with radius 'r'</li>
<li>The square which is enclosing the unit circle</li>
<li>The points inside the circle and outside the circle(inside the square)</li>
<li>Red spots represent the points inside the circle</li>
<li>Blue points represent the points outside the circle</li>
<li>points (x,y) where x and y random uniform distribution in interval (0,1)</li>
<li>πr^2 is calculation of the number of points inside the circle(num_points_circle)</li>
<li>(2r)^2 is the calculation of the points inside the square.Also it represents the sum of the number of all red and blue points (num_points_total)</li>
<li>num_points_circle/num_points_total = πr^2/(2r)^2	</li>
<li>π = 4*num_points_circle/num_points_total</li>
</ul>

####If n number(parameter of function)increases estimate rate increases 

##Run
<ol>
<li>Clone the repo</li>
<li>Run the estimating_pi.py</li>

</ol>

