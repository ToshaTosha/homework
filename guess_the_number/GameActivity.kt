package com.example.guess_the_number

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView

class GameActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_game)
        val yesButton = findViewById<Button>(R.id.yesButton)
        val noButton = findViewById<Button>(R.id.noButton)
        val question = findViewById<TextView>(R.id.question)
        var begin = intent.getIntExtra("begin", 0)
        var end = intent.getIntExtra("end", 100)
        var potentialNumber:Int = 0

        fun updateQuestion(){
            if (end > begin) {
                if (end - begin > 1){
                    potentialNumber = (end + begin) / 2
                    val questionString = "Это число больше$potentialNumber ?"
                    question.text = questionString
                } else {
                    potentialNumber =  end
                    val questionString = "Вы загадали число $potentialNumber"
                    question.text = questionString
                }
            }
        }

        yesButton.setOnClickListener {
            begin = potentialNumber
            updateQuestion()
        }

        noButton.setOnClickListener {
            end = potentialNumber
            updateQuestion()
        }
        updateQuestion()
    }
}