import roslib
import rospy
import smach
import smach_ros
import tf2_ros
import StateSpace_BasicMachine
class Dump_Lower(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Dump_Lower")

        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'