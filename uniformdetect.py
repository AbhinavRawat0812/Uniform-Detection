""" from imageai.Detection.Custom import DetectionModelTrainer

trainer=DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="uniform")
trainer.setTrainConfig(object_names_array=["pant","blazer","tie"],batch_size=8,num_experiments=1,train_from_pretrained_model="pretrained-yolov3.h5")
trainer.trainModel() """


from imageai.Detection.Custom import DetectionModelTrainer

trainer=DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="uniform")
trainer.evaluateModel(model_path="uniform/models",json_path="uniform\json\detection_config.json", iou_threshold=0.5,object_threshold=0.3,nms_threshold=0.5)

""" from imageai.Detection.Custom import CustomObjectDetection

detector=CustomObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath("uniform/models/detection_model-ex-011--loss-0017.411.h5")
detector.setJsonPath("uniform/json/detection_config.json")
detector.loadModel()
detections=detector.detectObjectsFromImage(input_image="/content/2.jpeg", output_image_path="uni-detect.jpg")
for detection in detections:
    print(detection["name"], " : ", detection["percentage_probability"], " : ", detection["box_points"]) """