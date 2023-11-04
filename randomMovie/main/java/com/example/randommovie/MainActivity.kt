package com.example.randommovie

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.Button
import android.widget.TextView

import kotlin.random.Random

class MainActivity : AppCompatActivity() {

    private val movies: Array<String> by lazy {
        resources.getStringArray(R.array.movies)
    }

    private var usedMovies: MutableList<String> = mutableListOf()

    val movieText = findViewById<TextView>(R.id.textView)
    val showButton = findViewById<Button>(R.id.next)
    val resetButton = findViewById<Button>(R.id.reset)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

    }

    private fun showRandomMovie() {
        if (usedMovies.size == movies.size) {
            movieText.text = "Больше нет фильмов!"
            return
        }

        var randomMovie: String
        do {
            randomMovie = movies.random()
        } while (usedMovies.contains(randomMovie))

        usedMovies.add(randomMovie)
        movieText.text = randomMovie
    }

    private fun resetMovies() {
        usedMovies.clear()
        movieText.text = ""
    }
}