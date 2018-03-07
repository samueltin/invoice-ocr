import os
import call_vision
import call_dialogflow

IMAGE_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'images')
IMAGE_FILE_LIST = ['invoice1.png', 'invoice2.png', 'invoice3.png']

def detent_text(image_file):

    invoice_img = os.path.join(IMAGE_DIR, image_file)
    ocr_result = call_vision.get_document(invoice_img, call_vision.FeatureType.BLOCK)
    print ('ocr result = ', ocr_result)

    return ocr_result

def categorize_invoice(ocr_result, index_list):
    intent_list=[]
    for i in index_list:
        intent = call_dialogflow.get_response(ocr_result[i])
        intent_list.append(intent)
    print ('intent list = ',intent_list)
    return intent_list




if __name__ == '__main__':

    ocr_result = detent_text(IMAGE_FILE_LIST[0])
    intent_list = categorize_invoice(ocr_result, [2,4,6])
    ocr_result = detent_text(IMAGE_FILE_LIST[1])
    intent_list = categorize_invoice(ocr_result, [4,7,10])
    ocr_result = detent_text(IMAGE_FILE_LIST[2])
    intent_list = categorize_invoice(ocr_result, [4,10,11])