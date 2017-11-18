import media
import fresh_tomatoes

if __name__ == "__main__":
  toystory = media.Movie("Toystory", "i will update", 55, 4, "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc");
  #print(toystory.storyline);

  avatar = media.Movie("Avatar","This is a crazy af movie", 210, 7, "https://media.vanityfair.com/photos/58c2f5aa0a144505fae9e9ee/master/pass/avatar-sequels-delayed.jpg",
                          "https://www.youtube.com/watch?v=5PSNL1qE6VY");
  #print(avatar.storyline);
  #avatar.show_trailer();

  bahubali = media.Movie("bahubali", "Magnum Opus: brothers, love betryal", 150, 9,
                         "https://www.chitramala.in/wp-content/gallery/bahubali-movie-latest-posters/Baahubali-50-Days-Poster.jpg",
                         "https://www.youtube.com/watch?v=qD-6d8Wo3do")
  
  baywatch = media.TvShow("Baywatch", "Sexy Shenanigns", 30,7, "http://photogallery.indiatimes.com/photo/56305531.cms", 1, "ABC")
  flash    = media.TvShow("Flash", "Fastest man alive", 40, 8, "https://i.redd.it/u5vcqikck3yy.jpg", 4, 'ABC')

  videos = [toystory, avatar, bahubali, flash, baywatch]

  fresh_tomatoes.open_movies_page(videos);
