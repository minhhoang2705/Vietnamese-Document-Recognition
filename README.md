# **_Vietnamese Document Recognition_**

## Overview
Vietnamese Document Recognition is a project aimed at developing a powerful OCR model specifically for Vietnamese documents. This project leverages the open-source PaddleOCR framework to be able to customize the model and train it with special data sets specific to the project.

## Features
- OCR for Vietnamese text
- User-friendly GUI for easy interaction
- Training and debugging tools for OCR models

## Installation
To get started with this project, clone the repository to your local machine: 
```
git add https://github.com/PaddlePaddle/PaddleOCR.git
```

And then in the tools folder, you can download my two files [predict_func.py](https://github.com/minhhoang2705/Vietnamese-Document-Recognition/blob/main/predict_func.py) and [uti.py](https://github.com/minhhoang2705/Vietnamese-Document-Recognition/blob/main/uti.py) and add those two files into the folder. 

For these two files, I made some adjustments so that my GUI could work well.

## Usage
### Training the OCR Models
To train your OCR models, it is best to look up the original PaddleOCR GitHub pages to find guidances.I have already trained a DB++ model for text detection and CRNN for text recognition. You can also use my [Train and Debug your OCR models with PaddleOCR](https://github.com/minhhoang2705/Vietnamese-Document-Recognition/blob/main/Train_and_Debug_Your_OCR_Models_with_PaddleOCR.ipynb) notebook as a template to train your own OCR models.

### Running the GUI
To run the graphical user interface, run the below command in the CLI:
```
python GUI.py
```
Here is my GUI

![image](https://github.com/minhhoang2705/Vietnamese-Document-Recognition/assets/86783160/f8e0c3cd-c246-4304-9c86-a86b5340efb6)

To run, you just have to choose an image and then click the process button to performs OCR.

Here is a demo

![image](https://github.com/minhhoang2705/Vietnamese-Document-Recognition/assets/86783160/b088748f-c5a2-4f24-af74-4463a0bd4642)

## Contributions
Contributions to the project are welcome.

## Acknowledgements

This project would not have been possible without the support and contributions from various individuals and organizations. We would like to extend our heartfelt thanks to:

- The developers and contributors of **[PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR.git)** for providing essential tools and libraries that were instrumental in this project.
- Our community of users and contributors who have provided valuable feedback, bug reports, and suggestions.

Special thanks to my mentor **Vin Thai Nguyen** for guidance and mentorship throughout the development of this project.

Lastly, we are grateful for the open-source community and everyone who has indirectly contributed by sharing their knowledge and resources, which have been invaluable to our work.


