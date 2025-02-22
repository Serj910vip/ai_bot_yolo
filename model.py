from imageai.Detection import ObjectDetection


def get_class(input_image, output_image, model_path):
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(model_path)
    detector.loadModel()

    detections = detector.detectObjectsFromImage(
        input_image=input_image,
        output_image_path=output_image,
        minimum_percentage_probability=30
    )
    road_objects = []
    if len(detections) > 0:
        for obj in detections:
            road_objects.append(obj)
        return(obj["name"], " : ", obj["percentage_probability"], " : ", obj["box_points"])
       

