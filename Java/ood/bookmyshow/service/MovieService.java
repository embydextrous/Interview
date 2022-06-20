package bookmyshow.service;

import bookmyshow.model.Movie;
import bookmyshow.repository.MovieRepository;

public class MovieService {
    private final MovieRepository movieRepository;

    public MovieService(MovieRepository movieRepository) {
        this.movieRepository = movieRepository;
    }

    public Movie getMovie(String id) {
        return movieRepository.getMovie(id);
    }

    public Movie addMovie(String name) {
        Movie movie = new Movie(name);
        movieRepository.addMovie(movie);
        return movie;
    }
}
