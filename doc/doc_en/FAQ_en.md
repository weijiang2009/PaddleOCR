## FAQ

### TODOs

- the QA section is simplely TOO weak, just improve it.

### Details

1. **Prediction Error: got an unexpected keyword argument 'gradient_clip'**  
The installed version of paddle is incorrect.

2. **Error when converting attention recognition model: KeyError: 'predict'**  
Solved. Please update to the latest version of the code.

3. **About Inference Speed**  
When there are many words in the picture, the prediction time will increase. You can use `--rec_batch_num` to set a smaller prediction batch num. The default value is 30, which can be changed to 10 or other values.

4. **Service deployment and mobile deployment**  
The service deployment based on Serving and the mobile deployment based on Paddle Lite has been released.

5. **Release time of self-developed algorithm**  
SAST, SRN and end2end PSL has been released.

6. **The difference between ultra-lightweight model and General OCR model**  
At present, PaddleOCR has opensourced the Chinese models, namely the 8.6M ultra-lightweight and the general Chinese OCR model. The comparison between the two is as following:
    - Similarities: Both use the same **algorithm** and **training data**；  
    - Differences: The difference lies in **backbone network** and **channel parameters**, the ultra-lightweight model uses MobileNetV3 as the backbone network, the general model uses Resnet50_vd as the detection model backbone, and Resnet34_vd as the recognition model backbone. You can compare the two model training configuration files to see the differences in parameters.

|Model|Backbone|Detection configuration file|Recognition configuration file|
|-|-|-|-|
|8.6M ultra-lightweight Chinese OCR model|MobileNetV3+MobileNetV3|det_mv3_db.yml|rec_chinese_lite_train.yml|
|General Chinese OCR model|Resnet50_vd+Resnet34_vd|det_r50_vd_db.yml|rec_chinese_common_train.yml|

7. **What is the training data used by the open-source model? Can it be opensourced?**  
At present, the open source model, dataset and magnitude are as follows:
    - Detection:  
        English dataset: ICDAR2015  
        Chinese dataset: LSVT street view dataset with 3w pictures
    - Recognition:  
        English dataset: MJSynth and SynthText synthetic dataset, the amount of data is tens of millions.  
        Chinese dataset: LSVT street view dataset with cropped text area, a total of 30w images. In addition, the synthesized data based on LSVT corpus is 500w.

Among them, the public datasets are opensourced, users can search and download by themselves, or refer to [Chinese data set](./datasets_en.md), synthetic data is not opensourced, users can use open-source synthesis tools to synthesize data themselves. Current available synthesis tools include [text_renderer](https://github.com/Sanster/text_renderer), [SynthText](https://github.com/ankush-me/SynthText) and [TextRecognitionDataGenerator](https://github.com/Belval/TextRecognitionDataGenerator) et. al.

8. **Error in using the model with TPS module for prediction**  
Error message: Input(X) dims[3] and Input(Grid) dims[2] should be equal, but received X dimension[3]\(108) != Grid dimension[2]\(100)  
Solution：TPS does not support variable shape. Please set --rec_image_shape='3,32,100' and --rec_char_type='en'

9. **Custom dictionary used during training, the recognition results show that words do not appear in the dictionary**  
The used custom dictionary path is not set when making prediction. The solution is setting parameter `rec_char_dict_path` to the corresponding dictionary file.

10. **Results of cpp_infer and python_inference are very different**  
Versions of exported inference model and inference libraray should be the same. For example, on Windows platform, version of the inference libraray that PaddlePaddle provides is 1.8, but version of the inference model that PaddleOCR provides is 1.7, you should export model yourself(`tools/export_model.py`) on PaddlePaddle1.8 and then use the exported model for inference.
