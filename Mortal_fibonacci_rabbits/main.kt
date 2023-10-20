fun main() {
    val n = readLine()?.toIntOrNull() ?: 0
    val m = readLine()?.toIntOrNull() ?: 0
    val arr = LongArray(m + 1) { 0L }
    arr[0] = 1

    for (i in 1..n-1) {
        for (j in arr.size - 1 downTo 1) {
            arr[j] = arr[j - 1]
        }
        arr[0] = arr.slice(2..arr.size - 1).sum()
    }

    println(arr.slice(0..arr.size - 2).sum())
}
