package com.example.json_parser

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import com.google.gson.Gson

import android.widget.TextView

class MainActivity : AppCompatActivity() {
    private val usedMovies: MutableList<Movie> = mutableListOf()

    private lateinit var movieText: TextView
    private lateinit var year: TextView
    private lateinit var genres: TextView
    private lateinit var country: TextView
    private lateinit var rating: TextView
    private lateinit var movies: List<Movie>

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        movieText = findViewById<TextView>(R.id.movieText)
        year = findViewById<TextView>(R.id.year)
        genres = findViewById<TextView>(R.id.genres)
        country = findViewById<TextView>(R.id.country)
        rating = findViewById<TextView>(R.id.rating)
        movieText.setText("Нажмите на кнопку, чтобы получить случайный фильм")
        movies = parseMovies(R.raw.movies)
    }

    fun onNext(view: View) {
        if (usedMovies.size == movies.size) {
            movieText.setText("Больше нет фильмов!")
            clearTextViews()
            return
        }

        val availableMovies = movies.filter { !usedMovies.contains(it) }
        if (availableMovies.isEmpty()) {
            movieText.setText("Больше нет фильмов!")
            clearTextViews()
            return
        }

        val randomMovie = availableMovies.random()
        usedMovies.add(randomMovie)
        movieText.setText(randomMovie.title)
        year.setText(randomMovie.year)
        genres.setText(randomMovie.genres.joinToString(", "))
        country.setText(randomMovie.country)
        rating.setText(randomMovie.rating)
    }

    private fun clearTextViews() {
        year.text = ""
        genres.text = ""
        country.text = ""
        rating.text = ""
    }

    fun onReset(view: View) {
        usedMovies.clear()
        movieText.setText("Нажмите на кнопку, чтобы получить случайный фильм")
    }

    data class Movie(
        val title: String,
        val year: String,
        val genres: List<String>,
        val country: String,
        val rating: String
    )

    data class Movies(val movies: Collection<Movie>)

    private fun parseMovies(id: Int): List<Movie> {
        val json = resources.openRawResource(id).bufferedReader().use { it.readText() }
        return Gson().fromJson(json, Movies::class.java).movies.toList()
    }
}

