# Chatbot-API
**INTRODUCTION<br>**
**Chatbot name:** Al-Siraj: An Islamic Chatbot.<br>
**AI Type:** Supervised AI.<br>
Al-Siraj is an Islamic chatbot. Which is built to handle the queries of Children (Age: <14). It consists of basic Islamic queries which can help them understand more about Islam. As the queries are basic knowledge, which also can help non-muslims to get knowledge about Islam. The API can get input in two languages only, Urdu and English. More languages can be added accordingly.<br>
**NOTE:** This is the **API** of the chatbot.<br>
#
**Versions:** <br>
**01: Main.py:** <br>
This version uses a Google Translate API to take and response user in multiple languages. Currently the code is done for two languages only.<br><br>
**02: Main (Without Translate).py:** <br>
This version is without the Google Translate API. It takes input and gives responses only in english. <br>
#
**Input Langugaes:** 
> Urdu.<br>
> English.<br>
#
**LANGUAGES**
> Python (3.11).
#
**LIBRARIES**
> Flask.<br>
> Flask-restful.<br>
> Google Cloud Translate.<br>
> Json.<br>
> Keras.<br>
> Numpy.<br>
> Scikit-Learn.<br>
> Tensorflow.
#
**MODEL**
> LSTM (Long Short Term Memory).<br><br>
**NOTE:** The Model (LSTM) is imported in this API. Because, The extracted/saved model is used at a certain accuracy. Which doesn't requires as much computational power as in training. The Model was trained in [Training Model](https://github.com/PersonXXIII/Chatbot-Training-Model).  <br>
The Trained model: [Trained Model](https://github.com/PersonXXIII/Chatbot-Trained-Model/).
#
**DATASET<br>**
Created in json format.<br>
**Intents:** 2000+<br>
**Queries:** 8500+<br>
#
**OTHER USED APIs**<br>
**Google Translate API:<br>**
To use the API you need a Json key. Which can be obtained from  [Gcloud Platform](https://console.cloud.google.com).
