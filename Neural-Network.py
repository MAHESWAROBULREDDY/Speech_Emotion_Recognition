"""
Neural network train file.
"""
import os
import joblib
import numpy as np
import matplotlib.pyplot as plt
from keras.layers import Dense
from keras.layers import Conv1D
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import Activation
from keras.models import Sequential
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from keras import callbacks
from sklearn.tree import DecisionTreeClassifier

#from config import SAVE_DIR_PATH
#from config import MODEL_DIR_PATH


class TrainModel:

    @staticmethod
    def train_neural_network(X, y) -> None:
        """
        This function trains the neural network.
        """

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

        x_traincnn = np.expand_dims(X_train, axis=2)
        x_testcnn = np.expand_dims(X_test, axis=2)

        print(x_traincnn.shape, x_testcnn.shape)
        print(y_train)
        print(X_train)
        print(X_test)
        print(y_test)
        print(y_test.shape)
        #fitting the DT
        DT_model_one = DecisionTreeClassifier()
        DT_model_one.fit(X_train, y_train)
        #Getting the score
        print(f"The classification accuracy is: {DT_model_one.score(X_train, y_train)}")
        print(f"The classification accuracy is: {DT_model_one.score(X_test, y_test)}")
        model = Sequential()
        model.add(Conv1D(16, 5,padding='same',input_shape=(40, 1), activation='relu'))
        model.add(Conv1D(32, 5,padding='same',activation='relu'))
        model.add(Conv1D(64, 5,padding='same',activation='relu'))
        model.add(Conv1D(128, 5,padding='same',activation='relu'))
        model.add(Dropout(0.1))
        model.add(Flatten())
        model.add(Dense(128, activation ='relu'))
        model.add(Dropout(0.1))
        model.add(Dense(64, activation ='relu'))
        model.add(Dense(8, activation='softmax'))
        print(model.summary)
        model.compile(loss='sparse_categorical_crossentropy',
                      optimizer='rmsprop',
                      metrics=['accuracy'])
                      
        '''earlystopping = callbacks.EarlyStopping(monitor ="val_loss", 
                                        mode ="min", patience = 5, 
                                        restore_best_weights = True)'''
                                        
        cnn_history = model.fit(x_traincnn, y_train,batch_size=32, epochs=50,validation_data=(x_testcnn, y_test))
        # Evaluating the model on the training and testing set
        score = model.evaluate(x_traincnn,y_train, verbose=0)
        print("Training Accuracy: ", score[1])
        score = model.evaluate(x_testcnn,y_test, verbose=0)
        print("Testing Accuracy: ", score[1])
        # Loss plotting
        plt.plot(cnn_history.history['loss'])
        plt.plot(cnn_history.history['val_loss'])
        plt.title('model loss')
        plt.ylabel('loss')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.savefig('loss.png')
        plt.close()

        # Accuracy plotting
        plt.plot(cnn_history.history['acc'])
        plt.plot(cnn_history.history['val_acc'])
        plt.title('model accuracy')
        plt.ylabel('acc')
        plt.xlabel('epoch')
        plt.legend(['train', 'test'], loc='upper left')
        plt.savefig('accuracy.png')
        
        
        predictions = model.predict(x_testcnn)
        print(predictions)
        #y_test = np.argmax(y_test)
        print(y_test)
        y_test = y_test.astype(int)
        #print('Confusion Matrix')
        print(confusion_matrix(y_test,np.argmax(predictions, axis = 1)))
        model_name = 'Emotion_Voice_Detection_Model.h5'

        # Save model and weights
        if not os.path.isdir('D:\Speech_Emotion_Recognition\Project\Speech_Emotion_Recognition'):
            os.makedirs('D:\Speech_Emotion_Recognition\Project\Speech_Emotion_Recognition')
        model_path = os.path.join('D:\Speech_Emotion_Recognition\Project\Speech_Emotion_Recognition', model_name)
        model.save(model_path)
        print('Saved trained model at %s ' % model_path)


if __name__ == '__main__':
    print('Training started')
    X = joblib.load('D:\Speech_Emotion_Recognition\Project\X.joblib')
    y = joblib.load('D:\Speech_Emotion_Recognition\Project\y.joblib')
    NEURAL_NET = TrainModel.train_neural_network(X=X, y=y)