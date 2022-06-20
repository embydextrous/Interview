package bookmyshow.repository;

import bookmyshow.model.Movie;

public interface MovieRepository {
    Movie getMovie(String id);
    void addMovie(Movie movie);
}
