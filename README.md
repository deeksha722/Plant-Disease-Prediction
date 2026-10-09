# 🌿 Plant Disease Prediction Using Deep Learning

---

## 📌 About the Project

The **Plant Disease Prediction** project uses Deep Learning and Convolutional Neural Networks (CNNs) to classify plant leaf images into healthy and diseased categories.

The project uses a dataset containing 23 classes across multiple plant types. A CNN model is developed to learn visual patterns from leaf images and predict their corresponding classes.

A Streamlit application provides an interactive interface for uploading leaf images and viewing model predictions.

## 🎯 Objectives

* 🌱 Classify healthy and diseased plant leaves.
* 📂 Explore and preprocess a plant disease image dataset.
* 🖼️ Resize and normalize images for model training.
* 🧠 Build a CNN model for multiclass image classification.
* 📊 Train and evaluate the model.
* 💾 Save the trained model for prediction.
* 🌐 Develop an interactive Streamlit application.

## 🛠️ Technologies Used

| Technology            | Purpose                               |
| --------------------- | ------------------------------------- |
| 🐍 Python             | Programming and implementation        |
| 🧠 TensorFlow / Keras | CNN model development                 |
| 📊 NumPy              | Numerical operations                  |
| 📈 Matplotlib         | Data visualization                    |
| 🖼️ Pillow            | Image processing                      |
| 🌐 Streamlit          | Interactive web application           |
| 📓 Jupyter Notebook   | Model development and experimentation |
| 🐙 GitHub             | Project hosting and version control   |

## 📂 Dataset

**Source:** Kaggle — Plant Disease Detection dataset

The dataset contains approximately **35,725 images across 23 classes**, covering healthy and diseased leaves from plants such as:

* 🍎 Apple
* 🌽 Corn
* 🫑 Pepper
* 🥔 Potato
* 🍅 Tomato

Images are resized to **128 × 128 pixels** and normalized before being passed to the CNN model.

*Note: The dataset is not included in this repository. Refer to the original dataset source for access.*

## ⚙️ Project Workflow

### 1️⃣ Data Exploration

* Loaded and explored the plant leaf image dataset.
* Examined the number of images and distribution across 23 classes.
* Inspected sample images and their corresponding labels.

### 2️⃣ Data Preprocessing

* Resized images to 128 × 128 pixels.
* Organized images into training, validation, and test sets.
* Normalized pixel values to the range 0–1.
* Prepared batches of images for model training.

### 3️⃣ CNN Model Development

Built a Convolutional Neural Network using TensorFlow/Keras.

The model architecture includes:

* **Convolutional layers:** Extract visual features from leaf images.
* **ReLU activation:** Introduces non-linearity.
* **Max pooling:** Reduces spatial dimensions.
* **Flatten layer:** Converts feature maps into a one-dimensional vector.
* **Dense layer:** Learns patterns for classification.
* **Softmax output layer:** Produces class probabilities for 23 classes.

### 4️⃣ Model Training and Evaluation

* Trained the CNN using labeled plant leaf images.
* Used training and validation data to monitor model learning.
* Prepared a separate test set for model evaluation.

*Refer to the notebook for the actual training history and evaluation metrics.*

### 5️⃣ Streamlit Application

* Developed an interactive interface using Streamlit.
* Enabled users to upload plant leaf images.
* Integrated the trained CNN model for image classification.
* Displayed the predicted plant disease class.

## 🧠 Model Architecture

The CNN follows this general structure:

**Input Image (128 × 128 × 3)**
⬇️
**Conv2D (32 filters) + ReLU**
⬇️
**MaxPooling2D**
⬇️
**Conv2D (64 filters) + ReLU**
⬇️
**MaxPooling2D**
⬇️
**Flatten**
⬇️
**Dense (128 neurons) + ReLU**
⬇️
**Dense (23 classes) + Softmax**

## 🚀 Getting Started

### Prerequisites

* Python
* pip
* Git

### Installation

**1️⃣ Clone the repository**

```bash
git clone <your-github-repository-url>
```

**2️⃣ Navigate to the project folder**

```bash
cd Plant-Disease-Prediction
```

**3️⃣ Install dependencies**

```bash
pip install -r requirements.txt
```

**4️⃣ Run the Streamlit application**

```bash
streamlit run app.py
```

*Note: The trained model and dataset must be available at the paths expected by the application and notebook.*

## 📁 Project Structure

```text
Plant-Disease-Prediction/
│
├── app.py
├── plant_disease_detection.ipynb
├── requirements.txt
└── README.md
```

The trained model file, `plant_disease_model.keras`, is not included in this repository because of its size. The application requires the model file to be available separately before predictions can run.

## 🔮 Future Enhancements

* 📊 Improve classification performance through further experimentation.
* 🔍 Evaluate the model using a confusion matrix and per-class metrics.
* 🌿 Add support for more plant species and disease categories.
* 🎨 Enhance the Streamlit interface.
* ☁️ Deploy the application for online access.

## 🎓 Learning Outcomes

Through this project, the following concepts were explored:

* Image data preprocessing and normalization.
* CNN architecture and feature extraction.
* Multiclass image classification using Softmax.
* Model training and validation.
* TensorFlow/Keras model saving and loading.
* Building an interactive application with Streamlit.

## ⚠️ Disclaimer

This project is developed for educational purposes. Predictions may be incorrect and should not be treated as definitive agricultural diagnoses. Consult a qualified agricultural expert before making important crop-management decisions.

## 👩‍💻 Author

**Deeksha Ravi Kumar**

B.Tech — Computer Science and Engineering
SRM Institute of Science and Technology, Ramapuram
