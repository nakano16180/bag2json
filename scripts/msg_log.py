import rosbag
import json
import yaml

bag = rosbag.Bag('../etc/bag_test.bag')

def open_msg(msg, indent):
    try:
        dic = {}
        for m in type(msg).__slots__:
            #print indent*"    ", m
            dic[m] = open_msg(msg.__getattribute__(m), int(indent+1))
        return dic            
    except:
        #print indent*"    ", msg
        return msg

msg_list = []
for topic, msg, t in bag.read_messages():
    msg_list.append(msg)
bag.close()

info_dict = yaml.load(rosbag.Bag('../etc/bag_test.bag', 'r')._get_yaml_info())
print json.dumps(info_dict, indent=4)

json_msg = open_msg(msg_list[10], 0)

print "_____________________"
print json.dumps(json_msg, indent=4)