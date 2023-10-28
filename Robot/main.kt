enum class Direction {
    UP, DOWN, LEFT, RIGHT
}

fun moveRobot(r: Robot, toX: Int, toY: Int) {
    while (r.x != toX || r.y != toY) {
        if (toX > r.x) {
            while (r.direction != Direction.RIGHT) {
                r.turnRight()
            }
        } else if (toX < r.x) {
            while (r.direction != Direction.LEFT) {
                r.turnLeft()
            }
        } else if (toY > r.y) {
            while (r.direction != Direction.UP) {
                r.turnRight()
            }
        } else if (toY < r.y) {
            while (r.direction != Direction.DOWN) {
                r.turnLeft()
            }
        }
        r.stepForward()
    }
}

fun main() {
    val r1 = Robot(3, 4, Direction.RIGHT)
    val r2 = Robot(0, 0, Direction.DOWN)

    println("Начальная позиция робота r1: ${r1}")
    println("Начальная позиция робота r2: ${r2}")

    r1.turnLeft()
    println("Робот r1 повернул налево: ${r1}")

    r2.turnRight()
    println("Робот r2 повернул направо: ${r2}")

    moveRobot(r1, 2, 3)
    println("Робот r1 переместился в точку (2, 3): ${r1}")

    moveRobot(r2, -1, -1)
    println("Робот r2 переместился в точку (-1, -1): ${r2}")
}
