class Parent(object):
  def __init__(self,lastname, eyecolor):
    print("Parent here");
    self.lastname = lastname
    self.eyecolor = eyecolor

  def show_info(self):
    print("Last Name: " + self.lastname)
    print("Eye Color: " + self.eyecolor)

class Child(Parent):
  """docstring for ClassName"""
  def __init__(self, lastname, eyecolor, nooftoys):
    print("Child here")
    super(Child, self).__init__(lastname,eyecolor)
    self.nooftoys = nooftoys
  
  def show_info(self):
    super(Child,self).show_info();
    print("Number of toys "+ str(self.nooftoys));

if __name__ == '__main__':
  billycyrus = Parent("cyrus","blue");
  billycyrus.show_info();

  ponycyrus  = Child("cyrus","blue",3);
  ponycyrus.show_info();