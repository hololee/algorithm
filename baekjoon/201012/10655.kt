import kotlin.math.abs

class CheckPoint(val x: Int, val y: Int) {
    fun getDistance(target: CheckPoint): Int {
        return abs(target.x - x) + abs(target.y - y)
    }
}

fun main() {

    val checkPoints = readLine()!!.toInt()
    val allCheckPoints: ArrayList<CheckPoint> = ArrayList()
    val advantages: ArrayList<Int> = ArrayList()
    var totalDistance = 0

    for (i in 0 until checkPoints) {
        //save data.
        val data = readLine()!!.split(" ")
        allCheckPoints.add(CheckPoint(data[0].toInt(), data[1].toInt()))

        if (i > 0) {
            totalDistance += allCheckPoints[i].getDistance(allCheckPoints[i - 1])
        }

        //cal advantage.
        if (i >= 2) {
            val cheatDistance = allCheckPoints[i].getDistance(allCheckPoints[i - 2])
            val officialDistance = allCheckPoints[i].getDistance(allCheckPoints[i - 1]) +
                    allCheckPoints[i - 1].getDistance(allCheckPoints[i - 2])

            val advantage = officialDistance - cheatDistance
            advantages.add(advantage)
        }
    }
//    print(totalDistance)
//    print(advantages)

    print(totalDistance - advantages.max()!!)

}