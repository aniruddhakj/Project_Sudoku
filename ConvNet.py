'''This is the CNN algorithm used for image processing. This is trained on MNIST handwritten digits dataset.
After the model is built, it is then trained and evaluated and further saved as "cnn.hdf5" file'''
import tensorflow as tf

class CNN:
    '''This is the main class for the Convolutional Neural Network which is used for the program.'''

    def __init__(self):
        ''' This function initializes the Convolutional Neural Network (CNN) '''
        self.model = tf.keras.models.Sequential()
        self.modeltrained = False
        self.modelbuilt = False

    def build_and_compile_model(self):
        '''This function builds the CNN and compiles it'''
        if self.modelbuilt:
            return
        
        # Add a Convolutional layer
        self.model.add(tf.keras.layers.Conv2D(32, (3, 3), input_shape=(28, 28, 1), activation='relu'))
        
        # Add a Max pooling layer
        self.model.add(tf.keras.layers.MaxPool2D())
        
        # Add the flattened layer
        self.model.add(tf.keras.layers.Flatten())
        
        # Add the hidden layer
        self.model.add(tf.keras.layers.Dense(512, activation='relu'))
        
        # Adding a dropout layer
        self.model.add(tf.keras.layers.Dropout(0.2))
        
        # Add the output layer
        self.model.add(tf.keras.layers.Dense(10, activation='softmax'))
        
        # Compiling the model
        self.model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
        self.modelbuilt = True

    def train_and_evaluate_model(self):
        '''This function loads the Train/Test dataset, trains the model and evaluates it.
        It prints the accuracy attained on the test set in the end'''
        if not self.modelbuilt:
            raise Exception("Build and train the model first!")
        if self.modeltrained:
            return
        
        # MNIST datasets
        mnist = tf.keras.datasets.mnist

        # Loading the Train/Test data
        (x_train, y_train), (x_test, y_test) = mnist.load_data()
        x_train = x_train.reshape(x_train.shape[0], 28, 28, 1)
        x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)
        # Reshape to form a 3D Vector
        print(len(x_train), len(x_test))
        x_test = x_test.reshape(x_test.shape[0], 28, 28, 1)

        # Normalize the train/test dataset
        x_train, x_test = x_train / 255.0, x_test / 255.0

        # Train the model
        self.model.fit(x=x_train, y=y_train, epochs=5)

        # Evaluate the model
        test_loss, test_acc = self.model.evaluate(x=x_test, y=y_test)
        self.modeltrained = True

    def save_model(self):
        '''This function is used to save the built and trained model to a .hdf5 file.'''
        if not self.modelbuilt:
            raise Exception("Build and compile the model first!")
        if not self.modeltrained:
            raise Exception("Train and evaluate the model first!")
        self.model.save("cnn.hdf5", overwrite=True)