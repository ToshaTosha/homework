fun main() {
    var maxPeriod = 0
    var desiredD = -1

    for (d in 2 until 1000) {
        var remainder = 1
        val remainders = mutableListOf<Int>()

        while (!remainders.contains(remainder)) {
            if (remainder == 0) {
                break
            }

            remainders.add(remainder)
            remainder = remainder * 10 % d
        }

        if (remainders.size - remainders.indexOf(remainder) > maxPeriod) {
            maxPeriod = remainders.size - remainders.indexOf(remainder)
            desiredD = d
        }
    }

    println(desiredD)
}
