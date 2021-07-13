import kotlin.math.max
import kotlin.math.min

class Robot(var direction: Int, var position: List<Int>)
class Order(val idx: Int, val order: String, val iterations: Int)
class RuntimeManager(mapSize: List<String>, val robotList: ArrayList<Robot> = ArrayList()) {

    var mapWidth = mapSize[0].toInt()
    val mapHeight = mapSize[1].toInt()

    fun doOrder(order: Order): Boolean {
        if (order.order == "L") {
            val degree = (((order.iterations * 90) % 360))
            robotList[order.idx].direction -= degree
            if (robotList[order.idx].direction < 0) {
                robotList[order.idx].direction += 360
            }

        } else if (order.order == "R") {
            val degree = (((order.iterations * 90) % 360))
            robotList[order.idx].direction += degree
            if (robotList[order.idx].direction > 360) {
                robotList[order.idx].direction -= 360
            }

        } else if (order.order == "F") {
            if (order.iterations > 0) {
                var targetPosition: List<Int>? = null

                // get targetPosition.
                if ((robotList[order.idx].direction == 0) or(robotList[order.idx].direction == 360)) {
                    targetPosition =
                        listOf(robotList[order.idx].position[0], robotList[order.idx].position[1] + order.iterations)
                } else if (robotList[order.idx].direction == 90) {
                    targetPosition =
                        listOf(robotList[order.idx].position[0] + order.iterations, robotList[order.idx].position[1])
                } else if (robotList[order.idx].direction == 180) {
                    targetPosition =
                        listOf(robotList[order.idx].position[0], robotList[order.idx].position[1] - order.iterations)
                } else if (robotList[order.idx].direction == 270) {
                    targetPosition =
                        listOf(robotList[order.idx].position[0] - order.iterations, robotList[order.idx].position[1])
                }

                if (targetPosition == null){
                    print("aa")
                }

                val collisionRobotIndices: ArrayList<Int> = ArrayList()
                //로봇 충돌 확인.
                for ((idx, compareRobot) in robotList.withIndex()) {
                    // targetPosition과 robotList[order.idx].position 사이에 위치하는 로봇이 있으면 출력 후 프로세스 종료.
                    //return false
                    // 아니면 현재 로봇의 위치를 변경.

                    //본인인지 체크
                    if (compareRobot.position != robotList[order.idx].position) {
                        //본인 로봇이 아니면.
                        if ((compareRobot.position[1] == robotList[order.idx].position[1]) and
                            (compareRobot.position[1] == targetPosition!![1])
                        ) {
                            // row  충돌 체크.
                            if ((compareRobot.position[0] >= min(robotList[order.idx].position[0], targetPosition!![0])) and
                                (compareRobot.position[0] <= max(robotList[order.idx].position[0], targetPosition!![0]))
                            ) {
                                collisionRobotIndices.add(idx)
                            }
                        } else if ((compareRobot.position[0] == robotList[order.idx].position[0]) and
                            (compareRobot.position[0] == targetPosition!![0])
                        ) {
                            // col 충돌 체크.
                            if ((compareRobot.position[1] >= min(robotList[order.idx].position[1], targetPosition!![1])) and
                                (compareRobot.position[1] <= max(robotList[order.idx].position[1], targetPosition!![1]))
                            ) {
                                collisionRobotIndices.add(idx)
                            }
                        }
                    }
                }
                if (collisionRobotIndices.size > 0) {
                    //충돌중 가장 짧은 충돌 감지.
                    var min_val = 0.0
                    var min_index: Int? = null
                    for (colRobotIndex in collisionRobotIndices) {
                        //cal distance and choose shorten 1.
                        if (min_val == 0.0) {
                            min_index = colRobotIndex
                            min_val = Math.sqrt(
                                Math.pow(
                                    (robotList[order.idx].position[0] - robotList[colRobotIndex].position[0]).toDouble(),
                                    2.0
                                ) + Math.pow((robotList[order.idx].position[1] - robotList[colRobotIndex].position[1]).toDouble(), 2.0)
                            )
                        } else {
                            val cur_min_val = Math.sqrt(
                                Math.pow(
                                    (robotList[order.idx].position[0] - robotList[colRobotIndex].position[0]).toDouble(),
                                    2.0
                                ) + Math.pow((robotList[order.idx].position[1] - robotList[colRobotIndex].position[1]).toDouble(), 2.0)
                            )

                            if (cur_min_val < min_val) {
                                //인덱스 변경.
                                min_index = colRobotIndex
                                min_val = cur_min_val
                            }

                        }

                    }
                    print("Robot ${order.idx + 1} crashes into robot ${min_index!! + 1}")
                    return false
                }


                //로봇 충돌이 없는경우 벽 충돌 확인.
                if ((targetPosition!![0] <= 0) or
                    (targetPosition[0] > mapWidth) or
                    (targetPosition[1] <= 0) or
                    (targetPosition[1] > mapHeight)
                ) {
                    print("Robot ${order.idx + 1} crashes into the wall")
                    return false
                }


                //충돌 없음.
                robotList[order.idx].position = targetPosition
            }

        }

        return true
    }


}

fun main() {
    val mapSize = readLine()!!.split(' ')
    val runtimeManager = RuntimeManager(mapSize = mapSize)

    val line_two = readLine()!!.split(' ')
    val N: Int = line_two[0].toInt()
    val M: Int = line_two[1].toInt()

    for (i in 1..N) {
        val robot = readLine()!!.split(' ')
        if (robot[2] == "N") {
            runtimeManager.robotList.add(Robot(0, listOf(robot[0].toInt(), robot[1].toInt())))
        } else if (robot[2] == "E") {
            runtimeManager.robotList.add(Robot(90, listOf(robot[0].toInt(), robot[1].toInt())))
        } else if (robot[2] == "S") {
            runtimeManager.robotList.add(Robot(180, listOf(robot[0].toInt(), robot[1].toInt())))
        } else if (robot[2] == "W") {
            runtimeManager.robotList.add(Robot(270, listOf(robot[0].toInt(), robot[1].toInt())))
        }

    }

    var resultFlag = true

    for (i in 1..M) {
        val order = readLine()!!.split(' ')
        if (!runtimeManager.doOrder(Order(order[0].toInt() - 1, order[1], order[2].toInt()))) {
            //false 일 경우
            resultFlag = false
            break
        }


    }
    if (resultFlag) {
        print("OK")
    }

}

