import xapp_control_ricbypass
from e2sm_proto import *
from time import sleep

def main():

    # hardcoded slice policies
    slice_1_policy = slice_policy_m()
    slice_1_policy.s_id = 1
    slice_1_policy.min_ratio = 10
    slice_1_policy.max_ratio = 40

    slice_2_policy = slice_policy_m()
    slice_2_policy.s_id = 2
    slice_2_policy.min_ratio = 20
    slice_2_policy.max_ratio = 80

    # rrmPolicyRatio 
    rrmPolicyRatio = rrmPolicyRatio_m()
    rrmPolicyRatio.slice_policies.extend([slice_1_policy, slice_2_policy])

    print("Ready to send the following policies:")
    print(rrmPolicyRatio)

    # create control request
    rc_req = RAN_control_request()

    # create control elements
    rc_element = RAN_param_map_entry()
    rc_element.key = RAN_parameter.RRM_POLICY_RATIO
    rc_element.rrmPolicyRatio.CopyFrom(rrmPolicyRatio)

    # add elements in map of rc request
    rc_req.target_param_map.extend([rc_element])

    # put into master message and send
    master_mess = RAN_message()
    master_mess.msg_type = RAN_message_type.CONTROL
    master_mess.ran_control_request.CopyFrom(rc_req)

    buf = master_mess.SerializeToString()
    xapp_control_ricbypass.send_to_socket(buf)
    print("Control message sent, exiting...")



if __name__ == '__main__':
    main()

