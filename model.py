from imageai.Detection import ObjectDetection
#from main import *
#main_files.init()
# from google.colab.patches import cv2_imshow
# import cv2

# Инициализируем объект детектирования
# detector = ObjectDetection()

# Указываем путь к модели YOLOv3
# model_path = "./ai_bot_safety/yolov3.pt"

# # Устанавливаем модель YOLOv3 и указываем путь к файлу с весами
# detector.setModelTypeAsYOLOv3()
# detector.setModelPath(model_path)

# # Загружаем модель
# detector.loadModel()

# # Список всех объектов, которые знает модель
# detector.CustomObjects()

# # Распознаем образы на выбранной картинке c вероятностью не менее 30% и сохраняем ее в новый файл
# detections = detector.detectObjectsFromImage(
#     input_image="./ai_bot_safety/photos/input.jpg",
#     output_image_path="./ai_bot_safety/photos/output_image.jpg",
#     minimum_percentage_probability=30)

# for eachObject in detections:
#     print(eachObject["name"] , " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"] )
#     print("--------------------------------")

# detections





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
        # for i in detections:
        #     if i in detections.keys():
        #         return detections[i]
        for obj in detections:
            road_objects.append(obj)
    
        # for i in road_objects:
        #     return i

        return(obj["name"], " : ", obj["percentage_probability"], " : ", obj["box_points"])
        #     return obj
        # r = []
        # for key,value in detections.items():
        #     if key == "name":
        #         r.append(key)
        # return r
    

# def analyze_objects(detections):
#     road_objects = []
#     if len(detections) > 0:
#       for detection in detections:
#           if detection["name"] in ["car", "motorbike", "bicycle", "person", "bus", 'train', 'truck','traffic_light', 'stop_sign']:
#               road_objects.append(detection)

#     return road_objects

# def road_safety_rules():
#     print()
#     print("Привет! Это SafetyAI - приложение для безопасности на дороге.")
#     print("Правила безопасности на дороге очень важны, и я помогу вам их запомнить.")
#     print("Помните, что всегда соблюдайте правила дорожного движения и будьте внимательны на дороге.")
#     print("Пользуйтесь светофорами и пешеходными переходами.")
#     print("Никогда не переходите дорогу в неположенном месте.")
#     print("И помните, что на дороге всегда нужно быть осторожным и предсказуемым.")
#     print("Будьте внимательны на дороге и удачи!")


# def get_class(input_image, output_image, model_path):
#     input_image="./ai_bot_safety/photos/input.jpg"
#     # input_image="src"
#     output_image="./ai_bot_safety/photos/output_image.jpg"
#     #input_image = "input_image.jpg"
#     #output_image = "output_image.jpg"

#     detections = detect_objects_on_road(input_image, output_image, "./ai_bot_safety/yolov3.pt")
#     #road_objects = analyze_objects(detections)

#     return detections
    
    # if len(detections) > 0:
    #     return detections
    #     print("Обнаруженные участники дорожного движения:")
    #    for obj in detections:
    #         print(obj["name"], " : ", obj["percentage_probability"], " : ", obj["box_points"])
    # else:

    #     print("Ни одного участника дорожного движения не обнаружено!")

# road_safety_rules()
# get_class() 