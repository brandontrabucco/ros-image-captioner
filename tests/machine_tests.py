#!/usr/bin/env python


"""Author: Brandon Trabucco
Tests the major functionality of the Image Caption Machine.
"""


import rospy
import image_caption_machine


if __name__ == "__main__":

    """Create the node.
    """
    m = image_caption_machine.get_machine()
    rospy.loginfo("Starting tests.")


    """Test the major fields.
    """
    rospy.loginfo("Places: " + str(m.places))
    rospy.loginfo("__call__: " + m())
    rospy.loginfo("Help: " + m.help())
    rospy.loginfo("Stop: " + m.stop())
    rospy.loginfo("Navigate: " + m.navigate("default"))
    rospy.loginfo("Learn: " + m.learn("default"))
    rospy.loginfo("Where: " + m.where())
    rospy.loginfo("Caption: " + m.caption())
    rospy.loginfo("Recite: " + m.recite())


    """Finished, and hopefully a success.
    """
    rospy.loginfo("All test cases finished.")
