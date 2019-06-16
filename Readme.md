#  Food review application

This is a mini food review application which based on the text review entered by the user predcits if the review is positive or negative(A classic sentiment analysis problem)
For example:
- Review1:I'm so happy to be here!!!(Predicted sentiment-Positive)
- Review2:The place was not clean and the food oh so stale!(Predicted sentiment-Negative)


## How to use the tool?

The Food review sentiment predictor has been rendered as a CLI tool using the excellent Pyinquirer package.

Steps to use and test the tool:
- Set up a different conda environment on your desktop to ensure your existing python system is not impacted
 and use requirements.txt to install all the required packages:
   conda create --name <env> --file requirements.txt 
- Now you need to install Pyinquirer through pip which is what is used to render the CLI tool:
   Pip install Pyinquirer
- run CLI_Food_review.py(by typing the command python CLI_Food_review.py)

## How the tool works?

Click on the below link to get a quick demo on how the tool works.

![alt test](https://img.youtube.com/vi/dZds8uCV5Sw/0.jpg)

(http://www.youtube.com/watch?v=dZds8uCV5Sw "Demo of how Food sentiment analysis tool works")


## Data used for ML model development

The data that was used for development of this application was developed using the files train.txt & test.txt(In the repo for your benefit).
- Training data(train.txt) contains 959 food reviews and with almost equal distribution of positive and negative sentiment
- Test data(test.txt) contains 40 reviews which dont have a sentiment marked (We use this to check our development regualization on in the wild data points)


## Methodology- TFIDF Vectorizer

We are here working on text data as input and all machine learning models need vectors as inputs.There are various methodologies available for vectorizing the text that need to be classified so that the machine learning model can ingest that for making a classification.The most advanced methodologies are :
- Word2vec or glove vector embeddings where we represent each word in n-embedding space similar to its representation in a huge corpus of text (wikipedeia etc) .Although amazingly good it is not suitable for linear models

- vectorizers like countvectorizers and term frequency–inverse document frequency(tfidf)

For the sake of simplicity and as we decided to go for a traditional logistic regression model we have used tfidf vectorizer in tf–idf value increases proportionally to the number of times a word appears in the document and is offset by the number of documents in the corpus that contain the word, which helps to adjust for the fact that some words appear more frequently in general(http://www.tfidf.com/)

## Methodology- The machine learning technique used for sentiment classification

The state of the art methodologies  in sentiment prediction or sentiment analysis is Deep learning based,example:
- https://arxiv.org/abs/1801.06146(Universal Language Model Fine-tuning for Text Classification)
- https://arxiv.org/abs/1810.04805(BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding
)

But we need to understand state of the art does not mean for every applied case.That is there are various parameters which drive which algorithm you should use when developing a decesion algorithm,Few of them are:

- Scale of the data

![alt test](https://cdn-images-1.medium.com/max/1600/1*867QVJdsBYHt8jd_0G_dfw.png)

As is shown in this amazingly cool demonstrative chart by Andrew Ng .The benefit that you may be able to get is subject to the amount of data available for training our algorithm.In our case we have only 959 training samples which indicates we would be equally wise using a traditional machine learning algorithm than a deep learning algorithm which would have higher complexity and would need more compute

- Availability of compute environment

Advanced machine learning algorithms like deep learning would need a higher compute(mainly GPU acceleartion) for a simplistic data problem like us investment in that is not justifiaable

- Implementation in real world

Before we started with the project we had decided we would develop a simple old school CLI based tool ,now if we would need this to be portable we would want to use a model which is a light weight decesion file .This further pushes us to use a simple traditional machine learning tool like Logistic regression.

Based on all of these factors we decided to proceed with using a traditional classification tool ,a Logistic regression model (scikit learn implementation) for our classification task.If you need details around Logistic regression check this out(https://www.coursera.org/lecture/machine-learning/classification-wlPeP)

## Further details on development of Machine learning model

Please refer to the jupyter notebook in the repo EDA_base_model.ipynb to get more details on how the model was developed.Summary is we developed the model on the training data using a cross validation across 5 folds which gave us an accuracy of 82.07% ,that is our ML model will be able to differentiate between a positive and negative sentiment around 82% of the time.Although this is not in high 90s(which is how the state of the art is ) considering we have limited us to only 959 data points we will take that to complete the pipeline of our tool

## Future enhancements opportunities

The accuracy of sentiment prediction could be improved to ~98% as per the SOTA results observed in the academic papers.Below are the few steps that need to be tried to reach there:
1. Increase the data by identifying open source food based reviews
2. Try transfer learning by using something like ULMFIT
3. Use Embedding based tokenizations of text comments
4. Once we have more data deep learning is the only way ahead




