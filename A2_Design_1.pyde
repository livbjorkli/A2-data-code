#size of the canvas
size(800, 500);

#resize flower to middle
translate(width/2 - 100, height/2 - 100)

#paint background white
background (255, 255, 255)


#draw stem of flower - https://happycoding.io/tutorials/processing/calling-functions/flower
line(96, 96, 96, 400);
line(105, 105, 105, 400);


#leafs of flower
ellipse(110, 200, 15, 15);
ellipse(91, 225, 15, 15);


#change thick petal outline to thin black line
strokeWeight(1);

#draw petals
fill(255, 255, 255);
ellipse(50, 50, 100, 100);
ellipse(150, 50, 100, 100);
ellipse(50, 150, 100, 100);
ellipse(150, 150, 100, 100);

#draw flower head (middle part of flower)
fill(255, 255, 255);
ellipse(100, 100, 100, 100);


#Putting in text (colour and front size)
#Black text color
fill(0) 
#Text size 
textSize(20)  

#Number "1" in each petal
# In top-left petal
text("1", 30, 50) 
# In top-right petal  
text("1", 155, 45)
# In bottom-left petal  
text("1", 30, 150)
# In bottom-right petal  
text("1", 155, 145) 

#Number "2" in the middle part of the flower 
text("2", 95, 108)

#Number "3" in stem 
#adjusting text size 
textSize (17)
text("3", 96, 280)

#Number "4" in the leafs 
text ("4", 86, 230)
#In right leaf 
text ("4", 106, 206)




#Right flower 
# stem of right flower 
line (96 + 250, 96, 96 + 250, 400);
line (105 + 250, 105, 105 + 250, 400);

#draw petals of right flower 
fill (255, 255, 255)
#left petal 
ellipse (50 + 250, 50, 100, 100);
ellipse (150 + 250, 50, 100, 100);
ellipse (50 + 250, 150, 100, 100);
ellipse (150 + 250, 150, 100, 100);

#middle centre of right flower 
fill (255, 255, 255)
ellipse (100 + 250, 100, 100, 100)

#Putting in text (colour and front size) for right flower 
#Black text color
fill(0) 
#Text size 
textSize(20)  

#right flower numbers 
#number 1 in top left petal 
text("1", 40 + 250, 50) 
# number 1 in top right petal 
text ("1", 155 + 250, 50)
# number 1 in bottom left petal 
text ("1", 40 + 250, 150)
#number 1 in bottom right petal 
text ("1", 155 + 250, 150)

#number 2 in centre of right flower 
text ("2", 95 + 250, 105)

#number 3 on the stem of right flower 
#adjusting text size 
textSize (17)
text("3", 96, 280)
text ("3", 96 + 250, 270)




#left flower 
#stem of left flower 
line (96 - 250, 96, 96 -  250, 400);
line (105 -  250, 105, 105 -  250, 400);

#draw petals of left flower 
fill (255, 255, 255)
#left petal 
ellipse (50 -  250, 50, 100, 100);
ellipse (150 -  250, 50, 100, 100);
ellipse (50 -  250, 150, 100, 100);
ellipse (150 -  250, 150, 100, 100);

#middle centre of left flower 
fill (255, 255, 255)
ellipse (100 - 250, 100, 100, 100)

#Putting in text (colour and front size) for left flower 
#Black text color
fill(0) 
#Text size 
textSize(20)  

#left flower numbers 
#number 1 in top left petal 
text("1", 40 -  250, 50) 
# number 1 in top right petal 
text ("1", 155 -  250, 50)
# number 1 in bottom left petal 
text ("1", 40 - 250, 150)
#number 1 in bottom right petal 
text ("1", 155 - 250, 150)

#number 2 in centre of left flower 
text ("2", 95 - 250, 105)

#number 3 on the stem of left flower 
#adjusting text size 
textSize (17)
text("3", 96, 280)
text ("3", 96 - 250, 270)
