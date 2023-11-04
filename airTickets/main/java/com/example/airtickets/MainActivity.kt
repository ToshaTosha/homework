package com.example.airtickets

import android.annotation.SuppressLint
import android.app.DatePickerDialog
import android.icu.text.SimpleDateFormat
import android.icu.util.Calendar
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.NumberPicker
import android.widget.TextView
import java.util.Locale

class MainActivity : AppCompatActivity() {
    private lateinit var datePickerFrom : TextView
    private lateinit var datePickerTo : TextView

    private lateinit var adultCount : NumberPicker
    private lateinit var childrenCount : NumberPicker
    private lateinit var babyCount : NumberPicker

    @SuppressLint("MissingInflatedId")
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        datePickerFrom = findViewById<TextView>(R.id.datePickerFrom)
        datePickerTo = findViewById<TextView>(R.id.datePickerTo)

        adultCount = findViewById<NumberPicker>(R.id.adultCount)
        adultCount.setMaxValue(9);
        adultCount.setMinValue(0);
        adultCount.descendantFocusability = NumberPicker.FOCUS_BLOCK_DESCENDANTS

        childrenCount = findViewById<NumberPicker>(R.id.childrenCount)
        childrenCount.setMaxValue(6);
        childrenCount.setMinValue(0);
        childrenCount.descendantFocusability = NumberPicker.FOCUS_BLOCK_DESCENDANTS

        babyCount = findViewById<NumberPicker>(R.id.babyCount)
        babyCount.setMaxValue(4);
        babyCount.setMinValue(0);
        babyCount.descendantFocusability = NumberPicker.FOCUS_BLOCK_DESCENDANTS

        val myCalendar = Calendar.getInstance()
        
        val datePickerDialogFrom = DatePickerDialog.OnDateSetListener { _, year, month, dayOfMonth ->
            myCalendar.set(Calendar.YEAR, year)
            myCalendar.set(Calendar.MONTH, month)
            myCalendar.set(Calendar.DAY_OF_MONTH, dayOfMonth)
            updateLabel(myCalendar, datePickerFrom)
        }

        val datePickerDialogTo = DatePickerDialog.OnDateSetListener { _, year, month, dayOfMonth ->
            myCalendar.set(Calendar.YEAR, year)
            myCalendar.set(Calendar.MONTH, month)
            myCalendar.set(Calendar.DAY_OF_MONTH, dayOfMonth)
            updateLabel(myCalendar, datePickerTo)
        }

        datePickerFrom.setOnClickListener {
            DatePickerDialog(this, datePickerDialogFrom, myCalendar.get(Calendar.YEAR), myCalendar.get(Calendar.MONTH),
            myCalendar.get(Calendar.DAY_OF_MONTH)).show()
        }

        datePickerTo.setOnClickListener {
            DatePickerDialog(this, datePickerDialogTo, myCalendar.get(Calendar.YEAR), myCalendar.get(Calendar.MONTH),
                myCalendar.get(Calendar.DAY_OF_MONTH)).show()
        }
    }

    private fun updateLabel(myCalendar: Calendar?, direction: TextView) {
        val myFormat = "dd-MM-yyyy"
        val sdf = SimpleDateFormat(myFormat, Locale.UK )
        if (myCalendar != null) {
            direction.setText(sdf.format(myCalendar.time))
        }
    }
}
