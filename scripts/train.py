from ultralytics import YOLO

model = YOLO("yolo26m-seg.pt")

model.train(
	data="data.yaml",
	imgsz=640,
	epochs=50,
	batch=2,
	device=0,
	workers=4,
	name="drainguard_m_v0"
)
