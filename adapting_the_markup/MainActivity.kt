package com.example.portraitlandscapepresentk2023

import android.os.Bundle
import android.view.View
import android.widget.AdapterView
import android.widget.ArrayAdapter
import android.widget.ImageView
import android.widget.Spinner
import android.widget.Toast
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity(),AdapterView.OnItemSelectedListener {
    private lateinit var adapter: ArrayAdapter<CharSequence>
    private lateinit var pictures: IntArray
    private var currentPosition = 0
    private lateinit var iv: ImageView
    lateinit var spinner: Spinner

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        pictures = intArrayOf(R.drawable.car1, R.drawable.car2, R.drawable.car3)

        if (savedInstanceState != null) {
            currentPosition = savedInstanceState.getInt("savedCurrentPosition", 0)
        };
        iv = findViewById(R.id.picture)
        iv.setImageResource(pictures[currentPosition])


        adapter = ArrayAdapter.createFromResource(this, R.array.pictures, R.layout.item)
        spinner = findViewById<Spinner>(R.id.pictures_list)
        spinner.adapter = adapter
        spinner.onItemSelectedListener = this
        spinner.setSelection(currentPosition)
    }

    fun onChangePictureClick(v: View) {
        if (!isChangingConfigurations)
        {
            val iv = findViewById<ImageView>(R.id.picture)
            currentPosition = (currentPosition + 1) % pictures.size
            iv.setImageResource(pictures[currentPosition])
            spinner.setSelection(currentPosition)
        }
    }

    override fun onItemSelected(parent: AdapterView<*>?, view: View?, position: Int, id: Long) {
        if (!isChangingConfigurations)
        {
            Toast.makeText(this, "выбран элемент ${position + 1}", Toast.LENGTH_SHORT).show()
            val iv = findViewById<ImageView>(R.id.picture)
            iv.setImageResource(pictures[position])
            currentPosition = position
        }
    }

    override fun onNothingSelected(parent: AdapterView<*>?) {
        Toast.makeText(this, "не выбран элемент", Toast.LENGTH_SHORT ).show()
    }

    override fun onSaveInstanceState(outState: Bundle) {
        super.onSaveInstanceState(outState)
        outState.putInt("savedCurrentPosition", currentPosition)
    }
}