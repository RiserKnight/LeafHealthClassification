model.save('HD_Model.h5')   #Saving H5 file filename.h5
converter = tf.lite.TFLiteConverter.from_saved_model('save_model')
tflite_model = converter.convert()
open("leaves_model.tflite", "wb").write(tflite_model)