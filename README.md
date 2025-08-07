<div align="center">

# 🤟 SIGN BUDDY 🤟

*Bridging Communication Gaps Through AI-Powered ASL Learning*

![SIGN BUDDY](https://github.com/user-attachments/assets/67ec914b-0a20-4a3b-8580-48088d655857)

[![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)](https://pytorch.org)
[![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white)](https://tensorflow.org)
[![Google Colab](https://img.shields.io/badge/Google_Colab-F9AB00?style=for-the-badge&logo=google-colab&logoColor=white)](https://colab.research.google.com)

</div>

## 🎯 **Project Overview**

**Developed a bidirectional CNN system that translates ASL alphabet signs to English text and provides visual ASL demonstrations from text input, addressing the critical shortage of qualified ASL instructors affecting deaf children's education. Applied advanced computer vision techniques including transfer learning and performance optimization within a comprehensive machine learning project.**

## 🚨 **Problem Statement**

American Sign Language serves as the primary language for many deaf individuals, yet significant barriers exist in ASL education accessibility. Research indicates that language deprivation remains a critical issue for deaf children, with many lacking access to qualified ASL instructors. Only about one-fourth of parents first learn about ASL from their early intervention provider, highlighting the shortage of professional support. 

**Our project addresses this gap by creating an interactive, engaging platform for children to learn ASL alphabet recognition, making ASL learning more accessible to both deaf and hearing children.**

## 🏆 **Key Results**

### 🔄 **Bidirectional ASL System**
- Developed comprehensive ASL recognition system capable of translating ASL alphabet signs to English text and generating visual ASL demonstrations from text input

### ⚡ **Performance Optimization**
- **Achieved 93% training time optimization** by transitioning from single-threaded to multi-threaded data loading (num_workers=0 to multi-core) and batch size optimization
- **Reduced training time from 7+ hours to 30 minutes**

### 📊 **Dataset & Training**
- Trained CNN models on **87,000+ images** across **29 ASL alphabet classes** with robust data preprocessing and augmentation techniques
- Implemented transfer learning using **ResNet-18** for enhanced model performance

### 🎮 **User Experience**
- Designed child-friendly educational tool with gamification elements to make ASL learning engaging and accessible

## 🔬 **Methodologies**

To accomplish this, we utilized **supervised learning with Convolutional Neural Networks (CNNs)** for image classification. The system was trained on **Google Colab** using **PyTorch** and **TensorFlow** frameworks. 

**Key Technical Approaches:**
- **Transfer Learning**: Implemented pre-trained models including ResNet-18, optimized for hand gesture recognition
- **Data Pipeline**: Custom preprocessing pipelines using NumPy for image normalization and resizing
- **Visualization**: matplotlib for data visualization and model performance analysis
- **Optimization**: Data loading and batch size tuning resulted in **93% reduction in training time** while maintaining model accuracy across 29 ASL alphabet classes

## 📊 **Data Sources**

**Kaggle Datasets:** [ASL-Alphabet](https://www.kaggle.com/datasets/grassknoted/asl-alphabet)
- **87,000 images** across **29 classes** (26 letters + space, delete, nothing)
- **3,000 images per class** with consistent **200x200 pixel resolution**

## 🛠️ **Technologies Used**

<div align="center">

| **Languages & Frameworks** | **Libraries & Tools** | **Platforms** |
|:---------------------------|:---------------------|:--------------|
| 🐍 Python | 🔢 NumPy | ☁️ Google Colab |
| 🔥 PyTorch | 📊 matplotlib | 📈 Kaggle |
| 🧠 TensorFlow | 🧱 CNN Architecture | |
| | 🔄 Transfer Learning (ResNet-18) | |

</div>

## 👥 **Authors**

<div align="center">

**This project was completed in collaboration with:**

| **Name** | **Email** | **Institution** |
|:---------|:----------|:----------------|
| 🌟 **Cecilia Tran** | [ctran0905@berkeley.edu](mailto:ctran0905@berkeley.edu) | UC Berkeley |
| 🎯 **Bryan Pineda** | [bpineda2@fordham.edu](mailto:bpineda2@fordham.edu) | Fordham University |
| 🚀 **James Boateng** | [boatengj@lafayette.edu](mailto:boatengj@lafayette.edu) | Lafayette College |

</div>

---

<div align="center">

**MADE WITH ❤️ by the SIGN BUDDY TEAM**

*Making ASL education accessible, one sign at a time* 🤟

</div>
