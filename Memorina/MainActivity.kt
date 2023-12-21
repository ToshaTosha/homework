package com.example.memorinak

import android.app.ActionBar
import android.graphics.Color
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.AttributeSet
import android.util.Log
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.LinearLayout
import android.widget.Toast
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.GlobalScope
import kotlinx.coroutines.delay
import kotlinx.coroutines.launch

val sprites = arrayOf(R.drawable.img1,R.drawable.img2,
    R.drawable.img3,R.drawable.img4,R.drawable.img5,
    R.drawable.img6,R.drawable.img7,R.drawable.img8)

private val cardsImagesIndices = (0..7).flatMap { listOf(it, it) }.shuffled().toTypedArray()

private var firstCard: ImageView? = null
private var secondCard: ImageView? = null
private var matchedPairs = 0

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        //setContentView(R.layout.activity_main)
        val layout = LinearLayout(applicationContext)
        layout.orientation = LinearLayout.VERTICAL

        val params = LinearLayout.LayoutParams(0, LinearLayout.LayoutParams.WRAP_CONTENT)
        params.weight = 1.toFloat() // единичный вес

        val catViews = ArrayList<ImageView>()
        for (i in 1..16) {
            catViews.add( // вызываем конструктор для создания нового ImageView
                ImageView(applicationContext).apply {
                    setImageResource(R.drawable.squarecat)
                    layoutParams = params
                    tag = "$i"
                    setOnClickListener(colorListener)
                }
            )
        }

        catViews.shuffle()

        val rows = Array(4, { LinearLayout(applicationContext)})

        var count = 0
        for (view in catViews) {
            val row: Int = count / 4
            rows[row].addView(view)
            count ++
        }
        for (row in rows) {
            layout.addView(row)
        }
        setContentView(layout)
    }

    suspend fun setBackgroundWithDelay(v: ImageView) {
        val clickedIndex = v.tag.toString().toInt() - 1
        v.setImageResource(sprites[cardsImagesIndices[clickedIndex]])
        delay(500)
    }

    suspend fun openCards() {
        if (firstCard != null && secondCard != null) {
            if (cardsImagesIndices[firstCard?.tag.toString().toInt() - 1] ==
                cardsImagesIndices[secondCard?.tag.toString().toInt() - 1]) {
                // Pair matched
                firstCard = null
                secondCard = null
                matchedPairs++
                if (matchedPairs == sprites.size) {
                    Toast.makeText(this, "Победа!", Toast.LENGTH_LONG).show()
                }
            } else {
                delay(1000)
                firstCard?.setImageResource(R.drawable.squarecat)
                secondCard?.setImageResource(R.drawable.squarecat)
                firstCard = null
                secondCard = null
            }
        }
    }

    // обработчик нажатия на кнопку
    val colorListener = View.OnClickListener() { view ->
        val clickedCard = view as ImageView
        if (firstCard == null) {
            firstCard = clickedCard
            GlobalScope.launch(Dispatchers.Main) {
                setBackgroundWithDelay(firstCard!!)
            }
        } else if (secondCard == null && firstCard !== clickedCard) {
            secondCard = clickedCard
            GlobalScope.launch(Dispatchers.Main) {
                setBackgroundWithDelay(secondCard!!)
                openCards()
            }
        }
    }
}