import media

if __name__ == "__main__":
  toystory = media.Movie("Toystory", "i will update", "https://en.wikipedia.org/wiki/Toy_Story#/media/File:Toy_Story.jpg",
                         "https://www.youtube.com/watch?v=KYz2wyBy3kc");
  print(toystory.storyline);

  avatar = media.Movie("Avatar","This is a crazy af movie", "https://media.vanityfair.com/photos/58c2f5aa0a144505fae9e9ee/master/pass/avatar-sequels-delayed.jpg",
                          "https://www.youtube.com/watch?v=5PSNL1qE6VY");
  print(avatar.storyline);
  avatar.show_trailer();
