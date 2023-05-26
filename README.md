# PaddleOCR_PyTorch

> 本项目旨在：对[PaddleOCR2PyTorch](https://github.com/frotms/PaddleOCR2Pytorch)项目做在线可视化，让体验与部署更轻松。

- 在线演示：[SwanHub Demo](https://blackswanai.cn/ZeYiLin/PaddleOCR_PyTorch/demo)
- 权重文件：[LFS Files](https://blackswanai.cn/ZeYiLin/PaddleOCR_PyTorch/tree/main)

![image-20230526202340274](https://typoraimagbed.oss-cn-beijing.aliyuncs.com/image-20230526202340274.png)

---



## 🚢PaddleOCR

[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)是PaddlePaddle推出的一套丰富、领先、且实用的OCR工具库。

本项目所用的权重为PP_V3系列，以LFS托管于[SwanHub](https://blackswanai.cn/ZeYiLin/PaddleOCR_PyTorch)

- 文本检测模型（2.42MB）：[ch_ptocr_v3_det_infer.pth](https://blackswanai.cn/ZeYiLin/PaddleOCR_PyTorch/blob/main?path=ch_ptocr_v3_det_infer.pth) 
- 文本识别模型（10.17MB）： [ch_ptocr_v3_rec_infer.pth](https://blackswanai.cn/ZeYiLin/PaddleOCR_PyTorch/blob/main?path=ch_ptocr_v3_rec_infer.pth)，



## 🔧How To Use

### 🚀推理

找到`./paddleocr_v3_inference.py`，在第166行修改为你的本地图像路径即可。

```python
if __name__ == '__main__':
    image = cv2.imread("./doc/imgs/1.jpg")
    draw_img, return_json = inferenceOCR(image)
    print(return_json)
    cv2.imwrite("./drawed_img.jpg", draw_img)
```

### 🎨GUI界面

[🦢在线体验链接](https://blackswanai.cn/ZeYiLin/PaddleOCR_PyTorch/demo)

GUI界面使用Gradio构建，本地运行：

```
python app.py
```

![image-20230526204222356](https://typoraimagbed.oss-cn-beijing.aliyuncs.com/image-20230526204222356.png)



## 参考

- [PaddleOCR2Pytorch](https://github.com/frotms/PaddleOCR2Pytorch)
- [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)
- [PytorchOCR](https://github.com/WenmuZhou/PytorchOCR)
- [Paddle](https://github.com/PaddlePaddle)
- [Pytorch](https://pytorch.org/)
- https://github.com/frotms/image_classification_pytorch
- https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.0/doc/doc_ch/models_list.md



















