from ultralytics import YOLO
import os
import csv
import re

def log_benchmark(model_path, csv_path="benchmark_results_forklift.csv"):
    # Extract model type from path
    model_type = re.search(r'([^/]+)/weights', model_path)
    if model_type:
        model_type = model_type.group(1)
    else:
        model_type = "unknown"
    print(model_type)
    # Load the model
    model = YOLO(model_path)
    
    # Validate the model
    metrics = model.val(
        split='val', 
        project="thesis_pose_benchmark_forklift_val", 
        data='/home/sentics/Misc_Datasets/Sentics_Pose_Dataset/POT_forklift_model/dataset/data.yaml', 
        iou=0.7,
        name=model_type
    )
    
    benchmark_data = {
            'model_type': model_type,
            # Box metrics
            'box_map': metrics.box.map,  # mAP 50-95
            'box_map50': metrics.box.map50,
            'box_map75': metrics.box.map75,
            'box_maps': ','.join(map(str, metrics.box.maps)) if isinstance(metrics.box.maps, list) else str(metrics.box.maps),
            'box_precision': metrics.box.p,  # Overall precision
            'box_recall': metrics.box.r,     # Overall recall
            
            # Pose metrics
            'pose_map': metrics.pose.map,  # Pose mAP 50-95
            'pose_map50': metrics.pose.map50,
            'pose_map75': metrics.pose.map75,
            'pose_maps': ','.join(map(str, metrics.pose.maps)) if isinstance(metrics.pose.maps, list) else str(metrics.pose.maps),
            'pose_precision': metrics.pose.p,  # Pose precision
            'pose_recall': metrics.pose.r,     # Pose recall
            
            # Additional pose-specific metrics if available
            'pose_kp_precision': getattr(metrics.pose, 'kp_p', 'N/A'),  # Keypoint precision
            'pose_kp_recall': getattr(metrics.pose, 'kp_r', 'N/A'),     # Keypoint recall
            'pose_oks': getattr(metrics.pose, 'oks', 'N/A'),           # Object Keypoint Similarity
            'pose_pck': getattr(metrics.pose, 'pck', 'N/A')            # Percentage of Correct Keypoints
        }
    
    # Check if file exists to determine if we need to write headers
    file_exists = os.path.isfile(csv_path)
    
    # Write to CSV
    with open(csv_path, 'a', newline='') as csvfile:
        fieldnames = benchmark_data.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(benchmark_data)
    
    print(f"Benchmark for {model_type} logged successfully to {csv_path}")
    return benchmark_data

# Example usage for a single model
model_paths = [
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_960_forklift_nosyn_v1.0_8n/weights/best.pt",
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_960_forklift_nosyn_v1.0_8s/weights/best.pt",
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_960_forklift_syn_v1.0_8n/weights/best.pt",
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_960_forklift_syn_v1.0_8s/weights/best.pt",
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_640_forklift_nosyn_v1.0_8m/weights/best.pt",
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_640_forklift_nosyn_v1.0_8n/weights/best.pt",
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_640_forklift_nosyn_v1.0_8s/weights/best.pt",
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_640_forklift_syn_v1.0_8m/weights/best.pt",
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_640_forklift_syn_v1.0_8n/weights/best.pt",
    "/home/sentics/ultralytics/thesis_pose_benchmark_forklift/RNDp_640_forklift_syn_v1.0_8s/weights/best.pt"

    # Add more model paths as needed
]

for path in model_paths:
    log_benchmark(path)