import com.opencsv.CSVReaderBuilder
import com.google.gson.Gson
import java.io.FileReader
import java.text.SimpleDateFormat
import java.io.FileWriter
import com.google.gson.JsonObject
import java.util.*

data class AppInfo(
    val name: String,
    val category: String,
    val rating: String,
    val reviews: String,
    val size: String,
    val installs: Int,
    val type: String,
    val price: Boolean,
    val contentRating: String,
    val genres: List<String>,
    val lastUpdated: String,
    val currentVer: String,
    val androidVer: String
)

fun main() {
    val reader = CSVReaderBuilder(FileReader("src/main/kotlin/googleplaystore.csv")).withSkipLines(1).build()
    val apps = mutableListOf<AppInfo>()
    reader.forEach { line ->
        try {
            val app = parseCsvLine(line)
            apps.add(app)
        } catch (e:Exception){
            println("")
        }
    }

    val groupedApps = apps.groupBy { it.category }

    groupedApps.forEach { (category, appsInCategory) ->
        println("Category: $category")
        appsInCategory.forEach { app ->
            println("  Name: ${app.name} installs: ${app.installs}")
        }
    }

    val jsonResult = JsonObject()
    groupedApps.forEach { (category, appsInCategory) ->
        val jsonCategory = JsonObject()
        jsonCategory.add("apps", Gson().toJsonTree(appsInCategory))
        jsonResult.add(category, jsonCategory)
    }
    val outputFile = "src/main/kotlin/output.json"
    FileWriter(outputFile).use { fileWriter ->
        Gson().toJson(jsonResult, fileWriter)
    }
}

fun parseCsvLine(line: Array<String>): AppInfo {
    return AppInfo(
        name = line[0],
        category = line[1],
        rating = line[2],
        reviews = line[3],
        size = line[4],
        installs = convertInstalls(line[5]),
        type = line[6],
        price = line[7] != "free",
        contentRating = line[8],
        genres = line[9].split(";"),
        lastUpdated = convertDate(line[10]),
        currentVer = line[11],
        androidVer = line[12]
    )
}

fun convertInstalls(installs: String): Int {
    val digitsOnly = installs.replace("[^\\d]".toRegex(), "")
    return if (digitsOnly.isNotEmpty()) {
        digitsOnly.toInt()
    } else {
        0
    }
}

fun convertDate(dateString: String): String {
    val date = SimpleDateFormat("MMMM d, yyyy", Locale.ENGLISH).parse(dateString)
    return SimpleDateFormat("yyyy-MM-dd", Locale.ENGLISH).format(date)
}
