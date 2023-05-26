import gradio as gr
from paddleocr_v3_inference import inferenceOCR
import cv2

def inference(input_image):
    result_image, return_json = inferenceOCR(input_image)
    return cv2.cvtColor(result_image, cv2.COLOR_BGR2RGB), return_json

if __name__ == "__main__":
    gr.Interface(
        title="PaddleOCR_PyTorch",
        fn=inference,
        inputs="image",
        outputs=["image", gr.JSON()]).launch()