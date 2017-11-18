import urllib

def read_file(filename=None):
  filedescrp = open(filename,'r')
  filecontents = filedescrp.read();
  filedescrp.close();
  return filecontents;


def check_profanity(text):
  conn = urllib.urlopen(" http://www.wdylike.appspot.com/?q="+text);
  output = conn.read();
  conn.close();
  if "true" in output:
    print "Profanity Alert!!";
  elif "false" in output:
    print "No curse words dear."
  else:
    print "cannot scan the document"


check_profanity(read_file("quotes.txt"));