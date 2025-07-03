converter = tf. lite . TFLiteConverter . from_keras_model ( model )
tflite_model = converter . convert ()
with open (" motion_model . tflite ", "wb") as f:
    f. write ( tflite_model )
