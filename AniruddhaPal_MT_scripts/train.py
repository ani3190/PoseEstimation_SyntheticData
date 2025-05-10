from ultralytics import YOLO
####### without pretrained ########################
# Initialize a YOLO model for training without pre-trained weights
# model = YOLO('yolov8n.yaml', pretrained=False)

########## with pre-trained weights #################
# ###detection
# model = YOLO('yolov8m.pt')  # load a pretrained model (recommended for training)
# results = model.train(data="/home/sentics/ultralytics/datasets/Projects/sch_nord/data.yaml", device=1, name = "25_02_25_schnord_v1.8_8m", epochs=250, batch= 16, patience= 10, imgsz=640 ,project= "schnord")  # #train the model

# # # segmentation
# model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)
# results = model.train(data="/home/sentics/ultralytics/datasets/Projects/General_model/license_plate/data.yaml", device=1, name = "09_12_24_LPdet_v1.0", epochs=200, batch= 32, patience= 20, imgsz=640 ,project= "LPdet", task='detect')  # #train the model

# # # dPose
model = YOLO("yolov8m-pose.pt")  # load a pretrained model (recommended for training)
#model = YOLO("thesis_pose_benchmark_forklift/RNDp_forklift_syn_v1.0_8n/weights/last.pt")
#model = YOLO('C:/Users/sentics/ultralytics/Forklift_pose_real_synthetic_data_30_04_24.pt')
results = model.train(data="/home/sentics/Misc_Datasets/Sentics_Pose_Dataset/human_model/dataset/data.yaml",device=0, name = "human_yolo_640_8m_nosyn", epochs=150, batch= 16, patience= 15, imgsz=640 ,project= "Aniruddha_human_pose_640s", task = "pose", resume=False)  # #train the model

#### Using Multi-Gpu in training then run this code for validation
# Load a model
# model = YOLO("yolov8s.yaml")  # build a new model from scratch
# model = YOLO("yolov8s.pt")  # load a pretrained model (recommended for training)

# model.train(data="/home/sentics/ultralytics/data.yaml")  # train the model
# if RANK in (0, -1):
#     metrics = model.val()

# print("mAP50-95:",metrics.box.map)   # map50-95
# print("mAP50:",metrics.box.map50)  # map50
# print("mAP75:",metrics.box.map75 ) # map75
# print("mAP50-95 each category:",metrics.box.maps )  # a list contains map50-95 of each category

