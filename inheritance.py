class Parent(object):
  def __init__(self,lastname, eyecolor):
    print("Parent here");
    self.lastname = lastname
    self.eyecolor = eyecolor

class Child(Parent):
  """docstring for ClassName"""
  def __init__(self, lastname, eyecolor, nooftoys):
    print("Child here")
    super(Child, self).__init__(lastname,eyecolor)
    self.nooftoys = nooftoys
    
if __name__ == '__main__':
  billycyrus = Parent("cyrus","blue");
  print billycyrus.eyecolor
  ponycyrus  = Child("cyrus","blue",3);
  print ponycyrus.eyecolor