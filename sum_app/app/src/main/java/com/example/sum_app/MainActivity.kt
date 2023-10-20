package com.example.sum_app

import java.lang.Math

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.view.View
import android.widget.EditText
import android.widget.TextView
import android.widget.Toast

fun Double.isWhole(): Boolean {
    return this % 1 == 0.0
}

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
    }

    fun onClick(v: View) {
        val etA = findViewById<EditText>(R.id.numA)
        val etB = findViewById<EditText>(R.id.numB)
        val tvSum = findViewById<TextView>(R.id.sum)

        val strA = etA.text.toString()
        val strB = etB.text.toString()

        if (strA.isEmpty() || strB.isEmpty()) {
            Toast.makeText(this, "Поле не должно быть пустым!", Toast.LENGTH_LONG).show()
            return
        }

        val sum = Math.round((strA.toDouble() + strB.toDouble()) * 10000.0) / 10000.0
        val strSum = if (sum.isWhole()) sum.toInt().toString() else sum.toString()
        tvSum.text = strSum
    }
}