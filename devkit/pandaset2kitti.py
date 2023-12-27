import os
import json
from tqdm import *

def read_json(json_file):
    with open(json_file) as f:
        return json.load(f)

def get_bbox(keypoints):
    return [min(keypoints[::2]), min(keypoints[1::2]), max(keypoints[::2]), max(keypoints[1::2])]

def read_gt(annos, merge_dict, category_ref, camera):
    # read gt and transform into kitti format
    anno_list = []
    annos = annos["annotations"]
    for anno in annos:
        if anno["sensor_name"] != camera:
            continue
        for i in range(len(anno["category_name"])):
            anno_line = []
            ref_cate = merge_dict[anno["category_name"][i]]
            if ref_cate == "Skip":
                continue
            anno_line.append(category_ref[ref_cate])
            bbox = get_bbox(anno["keypoints"][i])
            if bbox[0] < 0 or bbox[1] < 0 or bbox[2] > 1920 or bbox[3] > 1080:
                anno_line.append(1)
            else:
                anno_line.append(0)
            anno_line.append(anno["occlusion"][i])
            anno_line.append(-10)
            anno_line.extend(bbox)
            anno_line.append(anno["dimensions"][i][1])
            anno_line.append(anno["dimensions"][i][2])
            anno_line.append(anno["dimensions"][i][0])
            anno_line.extend(anno["location"][i])
            anno_line.append(anno["yaw"][i])
            anno_list.append(anno_line)
    return anno_list


def format_trans(gt_annos_path, target_path, camera):
    # Evaluation on following 5 categories
    category_ref = ["Car", "Truck", "Bus", "Bicycle", "Person"]
    # Merge raw categories to 5 categories
    merge_dict = {"Car": 0,     "Pickup Truck": 0,     "Medium-sized Truck": 1,     "Semi-truck": 1,
                    "Towed Object": "Skip",     "Other Vehicle - Uncommon": "Skip",    
                     "Other Vehicle - Construction Vehicle": "Skip",     "Other Vehicle - Pedicab": "Skip",     
                     "Emergency Vehicle": "Skip",     "Bus": 2,     "Bicycle": 3,     "Motorcycle": 3,  
                    "Train": "Skip",     "Tram / Subway": "Skip", "Trolley": "Skip", "Pedestrian": 4,     
                    "Personal Mobility Device": 3,     "Pedestrian with Object": 4,     
                    "Motorized Scooter": 3,     "Cones": "Skip",     "Construction Signs": "Skip",     
                    "Signs": "Skip",     "Temporary Construction Barriers": "Skip",     "Rolling Containers": "Skip",     
                    "Animals - Other": "Skip",     "Pylons": "Skip",     "Road Barriers": "Skip",     "Animals - Bird": "Skip"}

    seq_list = os.listdir(gt_annos_path)
    img_id = 0
    for seq in tqdm(seq_list):
        anno_seq_path = gt_annos_path + "/" + seq
        for img_ind in os.listdir(anno_seq_path):
            anno_img_path = anno_seq_path + "/" + img_ind
            gt_annos = read_json(anno_img_path)
            annos_list = read_gt(gt_annos, merge_dict, category_ref, camera)
            with open(target_path + "/" + str(img_id) + ".txt", "w") as f:
                for anno_obj in annos_list:
                    anno_str = ""
                    for obj_id, cate in enumerate(anno_obj):
                        anno_str += str(cate)
                        if obj_id < len(anno_obj)-1:
                            anno_str += " "
                    anno_str += "\n"
                    f.writelines(anno_str)
            img_id += 1

        


