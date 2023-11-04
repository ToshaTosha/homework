package com.example.movies

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View

import android.widget.TextView

class MainActivity : AppCompatActivity() {

    private val movies: Array<String> by lazy {
        resources.getStringArray(R.array.movies)
    }

    private val usedMovies: MutableList<String> = mutableListOf()

    private lateinit var movieText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        movieText = findViewById<TextView>(R.id.movieText)
        movieText.setText("Нажмите на кнопку, чтобы получить случайный фильм")
    }

    fun onNext(view: View) {
        if (usedMovies.size == movies.size) {
            movieText.setText("Больше нет фильмов!")
            return
        }

        var randomMovie: String
        do {
            randomMovie = movies.random()
        } while (usedMovies.contains(randomMovie))

        usedMovies.add(randomMovie)
        movieText.setText(randomMovie)
    }

    fun onReset(view: View) {
        usedMovies.clear()
        movieText.setText("Нажмите на кнопку, чтобы получить случайный фильм")
    }
}