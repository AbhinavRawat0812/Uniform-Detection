from imageai.Detection.Custom import CustomObjectDetection

detector=CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("F:/ML&AI/PROJECT/UniformDetection/uniform/models/detection_model-ex-011--loss-0017.411.h5")
detector.setJsonPath("F:/ML&AI/PROJECT/UniformDetection/uniform/json/detection_config.json")
detector.loadModel()
detections=detector.detectObjectsFromImage(input_image="F:/ML&AI/PROJECT/UniformDetection/unitest.jpg", output_image_path="uni-detect.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"])