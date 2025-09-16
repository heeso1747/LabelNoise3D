dataset_type = 'NuScenesDataset'
data_root = './data/nuscenes/'
class_names = [
    'car', 'truck', 'trailer', 'bus', 'construction_vehicle', 'bicycle',
    'motorcycle', 'pedestrian', 'traffic_cone', 'barrier'
]

point_cloud_range = [-50, -50, -5, 50, 50, 3]
input_modality = dict(use_lidar=True, use_camera=False)

train_pipeline = []
test_pipeline = []

train_dataloader = dict(dataset=dict(type=dataset_type, data_root=data_root))
val_dataloader = dict(dataset=dict(type=dataset_type, data_root=data_root))
test_dataloader = dict(dataset=dict(type=dataset_type, data_root=data_root))
