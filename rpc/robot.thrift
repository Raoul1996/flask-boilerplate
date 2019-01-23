namespace py robot_data
service RobotReceiver {
    map<string,string> saveRobotData(),
    map<i32,string> RobotInfo(1: required string RobotName, 2: required string RobotInfo)
}
