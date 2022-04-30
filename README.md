# AI Sudoku

![GitHub](https://img.shields.io/github/license/aniruddhakj/Project_Sudoku?color=ff0000&logo=Github)
![GitHub followers](https://img.shields.io/github/followers/aniruddhakj?style=social)

AI Sudoku solver using CNN/KNN

This project uses convolutional neural networks to analyze a sudoku image and converts it to a digital format

## Index
- [Getting Started](https://github.com/aniruddhakj/Project_Sudoku/blob/main/README.md#getting-started)
- [Running the App](https://github.com/aniruddhakj/Project_Sudoku/blob/main/README.md#running-the-app)


## Getting Started
1. Download and install Python3 from [this link](https://www.python.org/downloads/)
2. Install [venv](https://pypi.org/project/virtualenv/) to create a virtual environment for the project.
    - You can do this using a terminal and type :
        ```bash
        py -m pip install --user virtualenv
        ```
    - For macOS and Linux:
        ```zsh
        python3 -m pip install --user virtualenv
        ```  
3. Now create and activate the virtual environment
    ```bash
    venv Sudoku
    ```
    - For Windows
        ```bash
        cd Sudoku\Scripts
        activate
        ```
    - For macOS and Linux
      ```zsh
      source Sudoku/bin/activate
      ```
4. Clone the repo, install the required modules using requirements.txt
     ```zsh
    pip3 install -r requirements.txt
    ```
    - For Apple Silicon/ M-series Mac users, please check out Apple's Tensorflow Metal [installation guide](https://developer.apple.com/metal/tensorflow-plugin/)

## Running the App
* Before running the App in itself, you can switch the model type between CNN and KNN.
    ```python3
    from UI import UI
    from ConvNet import CNN
    from KNN import KNN
    import os
    # Change the model type variable value to "CNN" to use the Convolutional Neural Network
    # Change the model type variable value to "KNN" to use the K Nearest Neighbours Classifier
    modeltype = "CNN"
    ```
* Head Over and run Start.py in a python script. Ensure internet connectivity before the first run, as it downloads the MNIST dataset and saves the model as "knn.sav" or "cnn.hdf5" depending upon the modeltype variable.
    ```zsh
    python3 Start.py
    ```
