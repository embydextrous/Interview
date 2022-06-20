package bookmyshow.repository;

import java.util.HashMap;
import java.util.Map;

import bookmyshow.exceptions.NotFoundException;
import bookmyshow.model.Movie;

public class MovieRepositoryImpl implements MovieRepository {

    private final Map<String, Movie> movies;

    public MovieRepositoryImpl() {
        this.movies = new HashMap<>();
    }

    @Override
    public Movie getMovie(String id) {
        if (!movies.containsKey(id)) {
            throw new NotFoundException();
        }
        return movies.get(id);
    }

    @Override
    public void addMovie(Movie movie) {
        movies.put(movie.getId(), movie);
    }
}
