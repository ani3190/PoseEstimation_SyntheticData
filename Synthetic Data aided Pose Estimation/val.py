from ultralytics import YOLO

# Load a model
model = YOLO("/home/sentics/ultralytics/thesis_pose_benchmark_forklift/syn/RNDp_960_forklift_syn_v1.0_8s/weights/best.pt")  # load a custom model

# Validate the model
metrics = model.val(split='test', project= "Aniruddha_pose_test_labels", data= '/home/sentics/Misc_Datasets/Sentics_Pose_Dataset/POT_forklift_model/dataset/data_syn.yaml', iou =0.7, save=True)  # no arguments needed, dataset and settings remembered
metrics.box.map  # map50-95a
metrics.box.map50  # map50
metrics.box.map75  # map75
metrics.box.maps  # a list contains map50-95 of each category
metrics.pose.map # map50-95a