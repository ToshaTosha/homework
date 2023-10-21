class Rect(var x: Int, var y: Int, var width: Int, var height: Int) : Movable, Figure(0), Transforming {
    var color: Int = -1
    lateinit var name: String
    constructor(rect: Rect) : this(rect.x, rect.y, rect.width, rect.height)

    override fun move(dx: Int, dy: Int) {
        x += dx
        y += dy
    }

    override fun area(): Float {
        return (width * height).toFloat()
    }

    override fun resize(zoom: Int) {
        width *= zoom
        height *= zoom
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

        val rem = width
        width = height
        height = rem

    }
}
