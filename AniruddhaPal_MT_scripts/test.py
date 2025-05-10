from ultralytics import YOLO

# Load a model
#model = YOLO("yolov8s.yaml")  # build a new model from scratch
model = YOLO("/home/sentics/ultralytics/thesis_pose_benchmark_forklift/syn/RNDp_960_forklift_syn_v1.0_8n/weights/best.pt")  # load a pretrained model (recommended for training)
#model = YOLO('/home/sentics/ultralytics/Floor_seg/18_03_25_RNDs_fl_v1.1_8n/weights/best.pt') 
#source = "/home/sentics/ultralytics/list.streams"
#source = "/home/sentics/DEmatic/09_13_data_pipeline/missed_rollers"
source = "/home/sentics/Aniruddha_thesis_results/ground_truth/forklift_test_set_gt"
result = model.predict(source,conf= 0.40, iou= 0.2, line_width = 2, device=0, save= True, save_txt= True , project = 'Aniruddha_pose_test',name = 'forklift_pose_960n_syn_new')
#result = model.predict(source,conf= 0.2, line_width = 2, device=1, save= True, save_txt= False, name = "roller_inferences", project= "dematic_rollers")
#result = model(source, save= True, project= "test_floorseg", conf=0.1, device= 0, iou=0.25, task='segment', boxes= False, show_conf=False)
##################################################################################################################

# from ultralytics import YOLOWorld

# # Initialize a YOLO-World modelfrom ultralytics import YOLOWorld

# # Initialize a YOLO-World model
# model = YOLOWorld('yolov8s-world.pt')  # or select yolov8m/l-world.ptc


# # Define custom classes
# model.set_classes("blackbox")

# # Save the model with the defined offline vocabulary
# model.save("custom_box_yolov8s.pt")
# model = YOLOWorld('yolov8s-world.pt')  # or select yolov8m/l-world.pt

# # Define custom classes
# model.set_classes("blackbox")

# # Save the model with the defined offline vocabulary
# model.save("custom_box_yolov8s.pt")