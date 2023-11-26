package com.example.guess_the_number

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.EditText
import android.widget.Toast

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        val beginInput = findViewById<EditText>(R.id.begin)
        val endInput = findViewById<EditText>(R.id.end)
        val startButton = findViewById<Button>(R.id.button)

        fun onClick() {
            if (beginInput.text.toString().isEmpty() || endInput.text.toString().isEmpty()) {
                Toast.makeText(this, "Поле не должно быть пустым!", Toast.LENGTH_LONG).show()
                return
            }

            val begin:Int = Integer.parseInt(beginInput.text.toString())
            val end:Int = Integer.parseInt(endInput.text.toString())

            if (begin == end) {
                Toast.makeText(this, "Начало и конец диапазона не могут быть одинаковыми!", Toast.LENGTH_LONG).show()
                return
            }

            if (begin > end) {
                Toast.makeText(this, "Конец диапазона не может быть меньше начала", Toast.LENGTH_LONG).show()
                return
            }

            val intent = Intent(this, GameActivity::class.java)
            intent.putExtra("begin", begin)
            intent.putExtra("end", end)
            startActivity(intent)
        }

        startButton.setOnClickListener {
            onClick()
        }

    }
}