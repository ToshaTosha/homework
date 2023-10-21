class Square(var x: Int, var y: Int, var side: Int) : Movable, Figure(0), Transforming {
    override fun area(): Float {
        return (side * side).toFloat()
    }

    override fun resize(zoom: Int) {
        side *= zoom
    }

    override fun move(dx: Int, dy: Int) {
        x += dx; y += dy
    }

    override fun rotate(direction: RotateDirection, centerX: Int, centerY: Int) {
        val translatedX = x - centerX
        val translatedY = y - centerY

        if (direction == RotateDirection.Clockwise) {
            x = centerX + translatedY
            y = centerY - translatedX
        } else {
            x = centerX - translatedY
            y = centerY + translatedX
        }
    }
}