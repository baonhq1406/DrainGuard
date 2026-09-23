from ultralytics import YOLO

model = YOLO("models/dataset_l_v0.pt")

model.predict(
    source="raw_images",
    device=0,
    conf=0.25,
    save=True,
    project="runs/predict",
    name="model_test_l_v0"
)