import webbrowser

class Video(object):
  """docstring for Video class"""
  def __init__(self, title, storyline, runtime, rating, poster_url):
    self.title = title
    self.storyline = storyline
    self.runtime   = runtime
    self.rating    = rating
    self.poster_url = poster_url

class TvShow(Video):
  """docstring for TvShow"""
  def __init__(self, title, storyline, runtime, rating, poster_url ,episode, network):
    super(TvShow, self).__init__(title, storyline, runtime, rating, poster_url)
    self.episode = episode
    self.network = network
    

class Movie(Video):
  def __init__(self, movie_title, storyline, runtime, rating, poster_url, trailer_url):
    super(Movie,self).__init__(movie_title, storyline, runtime, rating, poster_url)
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