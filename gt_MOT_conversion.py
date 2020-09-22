import json
import time

data_file = 'b1cebfb7-284f5117.json'
data = json.load(open(data_file, 'r'))
converted_data = []
gt_file = open('gt.txt', 'w+')
frame_num = 1
initial_label_id = 0
for frame in data:
    labels = frame['labels']
    label_count = 0
    for label in labels:
        if (frame['index'] == 0 and label_count == 0):
            id_string = label['id']
            initial_label_id = int(id_string)-1

        id_string = label['id']
        id = int(id_string) - initial_label_id
        bbox = label['box2d']
        x1, y1, width, height = bbox['x1'], bbox['y1'], bbox['x2']- bbox['x1'], bbox['y2']-bbox['y1']
        conf = -1
        x, y, z = -1,-1,-1
        print('{}, {}, {}, {}, {}, {}, {}, {}, {}, {}'.format(frame_num,id,x1,y1,width,height,conf,x,y,z), file=gt_file)
        label_count += 1
    frame_num += 1