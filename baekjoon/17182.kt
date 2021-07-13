// 201012

import java.util.*
import kotlin.collections.ArrayList

fun main() {

    val lineOne = readLine()!!.split(" ")
    val numberOfPlanet = lineOne[0].toInt()
    val startPoint = lineOne[1].toInt()

    val scanner = Scanner(System.`in`)

    val distances = ArrayList<ArrayList<Int>>()
    val checkPoints = ArrayList<Int>()

    for (i in 0 until numberOfPlanet) {
        val container = ArrayList<Int>()
        for (j in 0 until numberOfPlanet) {
            container.add(scanner.nextInt())
        }
        distances.add(container)
        checkPoints.add(0)
    }

    // cal minimum distance.
    for (i in 0 until numberOfPlanet) {
        //mid node.
        for (j in 0 until numberOfPlanet) {
            //start node.
            for (k in 0 until numberOfPlanet) {
                if (distances[j][k] > distances[j][i] + distances[i][k]) {

                    //더 작은 길로 변경.
                    distances[j][k] = distances[j][i] + distances[i][k]
                }
            }
        }
    }

//    println(distances)

    //탐색기.
    val searcher = Searcher(numberOfPlanet, distances)
    searcher.search(startPoint, checkPoints)

    print(searcher.totalLists.min())
}

class Searcher(val numberOfPlanet: Int, val allDistance: ArrayList<ArrayList<Int>>) {

    val totalLists = ArrayList<Int>()

    fun search(curNode: Int, myCheckPoint: ArrayList<Int>, stackFlag: Int = 1) {
        // flag 표시.
        myCheckPoint[curNode] = stackFlag

        var fullCheckFlag = true

        //인접 노드 체크.(순서대로)
        for (nextNode in 0 until numberOfPlanet) {
            if (myCheckPoint[nextNode] == 0) {
                search(nextNode, myCheckPoint.toMutableList() as ArrayList<Int>, stackFlag + 1)
                fullCheckFlag = false
            }

        }

        //다 채워졌을떄.
        if (fullCheckFlag) {

            var totalDistance = 0
            var lastIndexVal = myCheckPoint.indexOf(1)

//            println(myCheckPoint)
            for (nodeOrder in 2..numberOfPlanet) {

                //거리 추가.
                totalDistance += allDistance[lastIndexVal][myCheckPoint.indexOf(nodeOrder)]
                //인덱스 변경.
                lastIndexVal = myCheckPoint.indexOf(nodeOrder)


//                print(lastIndexVal + 1)
            }
//            println(totalDistance)
            totalLists.add(totalDistance)


        }

    }

}
