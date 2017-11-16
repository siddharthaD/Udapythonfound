#hrllo
import turtle

def draw_square(banda):
  
  banda.speed(10);
  banda.shape('turtle');
  banda.color("red", "blue");

  for x in xrange(1,5):
    banda.forward(100);
    banda.right(90);
  #banda.shapesize(5);
  

#  prada = turtle.Turtle();
 # prada.shape("arrow");
  #prada.circle(100);
  #print 'Hello'

  #triag = turtle.Turtle();
  #triag.home();
  #triag.begin_poly();
  #triag.fd(40);
  #triag.left(60);
  #triag.fd(50);
  #triag.left(150);
  #triag.fd(70);
  #triag.end_poly();
  

window = turtle.Screen();
window.bgcolor('green');
banda = turtle.Turtle();
for i in xrange(1,30):
  banda.right(18)
  draw_square(banda)
window.exitonclick();