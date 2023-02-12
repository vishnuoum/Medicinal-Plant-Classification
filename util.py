from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
from logConfig import logging
import heapq
from repository import getPlant

logging.info("-----Loading model-----\n\n\n")

# loading model
model = load_model("model")

logging.info("-----Model Loaded-----\n\n\n")


# defining classes
classes = [ 'Arive-Dantu','Betel','Basale','Crape_Jasmine','Curry','Drumstick','Fenugreek','Guava','Hibiscus','Indian_Beech','Indian_Mustard','Jackfruit',
            'Jamaica_Cherry-Gasagase','Jamun','Jasmine','Karanda','Lemon','Mango','Mexican_Mint','Mint','Neem','Oleander','Parijata','Peepal','Pomegranate',
            'Rasna','Rose_apple','Roxburgh_fig','Sandalwood','Tulsi']


# classification function
def classify(imagePath):

    # enclosing in try block to catch exception
    try:
        logging.info("-----Classify image with path = %s-----",imagePath)

        # loading image from path and converting to numpy array for prediction
        image = Image.open(imagePath)
        image = np.array(image)
        image = image.reshape(1,image.shape[0],image.shape[1],3)

        # ---- classication flow starts ----

        # prediction
        prediction = model.predict(image)[0]

        # finding the top class and its prediction score (accuracy)
        _class = np.argmax(prediction)
        predictionScore = prediction[_class]
        print(classes[_class],predictionScore)

        # ---- Result logic starts ----

        # if predictionScore greater than 90% return single class
        if(predictionScore>0.90):
            logging.info("-----Classification report = %s probability = %s-----",classes[_class],predictionScore)
            result = []
            details = getPlant(id=_class+1)
            result.append({"class":classes[_class],"confidence":float(prediction[_class]),"details":details})
            return result

        # if 90 >= predictionScore > 80 return two classes
        elif(predictionScore>0.80):
            logging.info("-----Classification probability less than 90% Returning top 2 classes-----")
            result = []
            _class = heapq.nlargest(2, range(len(prediction)), key=prediction.__getitem__)
            for i in _class:
                details = getPlant(id=i+1)
                result.append({"class":classes[i],"confidence":float(prediction[i]),"details":details})
            return result
        
        # if 80 >= predictionScore > 70 return two classes
        elif(predictionScore>=0.70):
            logging.info("-----Classification probability less than 80% Returning top 3 classes-----")
            result = []
            _class = heapq.nlargest(3, range(len(prediction)), key=prediction.__getitem__)
            for i in _class:
                details = getPlant(id=i+1)
                result.append({"class":classes[i],"confidence":float(prediction[i]),"details":details})
            return result
        
        # accuracy criteria not satisfied
        else:
            return "Not satisfied"
        
        # ---- Result logic starts ----

        # ---- classication flow ends ----

    # catch exception if any
    except Exception as e:
        print(e)
        return "error"


# classify("uploads/__0_1104004.png")