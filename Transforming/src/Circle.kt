class Circle(var x: Int, var y: Int, var radius: Int) : Figure(0), Transforming {
    override fun area(): Float {
        return (Math.PI * radius * radius).toFloat()
    }

    override fun resize(zoom: Int) {
        radius *= zoom
    }

    override fun rotate(direction: RotateDirection, centerX: Int, centerY: Int) {
        val translatedX = x - centerX
        val translatedY = y - centerY

        x = centerX
        y = centerY

        if (direction == RotateDirection.Clockwise) {
            x += translatedY
            y -= translatedX
        } else {
            x -= translatedY
            y += translatedX
        }
    }
}