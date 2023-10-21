fun main() {

    // Circle

    val circle = Circle(0, 5, 5)
    println("x: ${circle.x}, y: ${circle.y}")
    println("area: ${circle.area()}")

    circle.rotate(RotateDirection.Clockwise, 0, 0)
    println("x: ${circle.x}, y: ${circle.y}")

    circle.rotate(RotateDirection.Clockwise, 0, 0)
    println("x: ${circle.x}, y: ${circle.y}")

    circle.rotate(RotateDirection.CounterClockwise, 0, 0)
    println("x: ${circle.x}, y: ${circle.y}")

    circle.resize(2)
    println("radius: ${circle.radius}")

    // Rec

    var rect = Rect(4, 3, 4, 2)
    println("area: ${rect.area()}")

    rect.move(2, 3)
    println("x: ${rect.x}, y: ${rect.y}")

    rect.rotate(RotateDirection.Clockwise, 3, -3)
    println("x: ${rect.x}, y: ${rect.y}, width: ${rect.width}, height: ${rect.height}")

    rect = Rect(4, 3, 4, 2)
    rect.rotate(RotateDirection.CounterClockwise, 3, -3)
    println("x: ${rect.x}, y: ${rect.y}, width: ${rect.width}, height: ${rect.height}")

    rect.resize(2)
    println("x: ${rect.x}, y: ${rect.y}")

    // Square

    var square = Square(10, 10, 5)
    println("area: ${square.area()}")

    square.resize(2)
    println("side: ${square.side}")

    square.move(2, 3)
    println("x: ${square.x}, y: ${square.y}")

    square.rotate(RotateDirection.Clockwise, 3, -3)
    println("x: ${square.x}, y: ${square.y}, side: ${square.side}")

    square = Square(10, 10, 5)
    rect.rotate(RotateDirection.CounterClockwise, 3, -3)
    println("x: ${square.x}, y: ${square.y}, side: ${square.side}")

}