from flask import Flask, request, render_template
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.preprocessing.sequence import pad_sequences
from flask_restful import Api, Resource
import tensorflow as tf
import numpy as np
import json
import string
import random
import os

# load the tokenizer and label encoder
with open('tokenizer.json') as f:
    data = json.load(f)
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(data)

with open('label_encoder.json') as f:
    data = json.load(f)
    le = LabelEncoder()
    le.classes_ = np.array(data)

with open('responses.json') as file:
    responses = json.load(file)

# load the trained model
model = tf.keras.models.load_model('my_model.h5')

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def info():
    return render_template('info.html')

class Chatbot(Resource):
    def post(self):
        try:
            # get user input
            data = request.get_json()
            texts_p = []
            prediction_input = data['input']
            # preprocess the input
            prediction_input = prediction_input.lower() # convert to lowercase
            prediction_input = ''.join(c for c in prediction_input if c not in string.punctuation) # remove punctuation
            prediction_input = ' '.join(prediction_input.split())
                
            # Replacing words using a dictionary
            with open("dictionary.json", "r") as f:
                replacement_dict = json.load(f)

            with open("Other_words.json", "r") as f:
                Other_words = json.load(f)

            if prediction_input in Other_words:
                pass
            else:
                prediction_words = prediction_input.split()
                prediction_words = [replacement_dict.get(word, word) for word in prediction_words]
                prediction_input = ' '.join(prediction_words)

                texts_p.append(prediction_input)
                prediction_input = tokenizer.texts_to_sequences(texts_p)
                prediction_input = np.array(prediction_input).reshape(-1)
                prediction_input = pad_sequences([prediction_input], maxlen=88)

                # get the output from the model
                output = model.predict(prediction_input)
                output = output.argmax()

                # find the tag and select a response
                response_tag = le.inverse_transform([output])[0]
                response = random.choice(responses[response_tag])

             # return the response
            return {'response': response}


        except Exception as e:
            return {'response' : "Doesn't Support the language you are using. ERROR!"}

api.add_resource(Chatbot, '/chatbot')



if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8888))
    app.run(host='0.0.0.0', port=port)
