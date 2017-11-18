import webbrowser
class Movie(object):
  def __init__(self, movie_title, storyline, poster_url, trailer_url):
    self.title = movie_title
    self.storyline = storyline
    self.poster_url = poster_url
    self.trailer_url = trailer_url

  def __del__(self):
    #Do dome destructive stuff
     pass

  def show_trailer(self):
    
    webbrowser.open(self.trailer_url);

  def __cmp__(self, other):
      if isinstance(other,Movie):
        pass
      else:
        pass