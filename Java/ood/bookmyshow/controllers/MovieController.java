package bookmyshow.controllers;

import bookmyshow.service.MovieService;

public class MovieController {
    final private MovieService movieService;

    public MovieController(MovieService movieService) {
        this.movieService = movieService;
    }

    public String createMovie(String movieName) {
        return movieService.addMovie(movieName).getId();
    }
}
