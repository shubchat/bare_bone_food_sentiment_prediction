from __future__ import print_function, unicode_literals
from sklearn.externals import joblib

import re
from pprint import pprint

from PyInquirer import style_from_dict, Token, prompt
from PyInquirer import Validator, ValidationError

from examples import custom_style_3

import warnings
warnings.filterwarnings("ignore")



class commentValidator(Validator):
    def validate(self, document):
        check=bool(re.match("^[a-zA-Z0-9_ ]*$",document.text))
        if check:
            ok = bool(re.match(r'\d',document.text))
            if  ok:
                raise ValidationError(
                    message='Your comments cannot be only numeric,please try again',
                    cursor_position=len(document.text))  # Move cursor to end
        else:

            raise ValidationError(
    message='Your comments cannot contain special values,please try again',
    cursor_position=len(document.text))  # Move cursor to end


def sentiment_predictor(comment):

    clf=joblib.load('Logistic_model.pkl')
    vectorizer=joblib.load('vectorizer_Logisticmodel.pkl')
    test_vector=vectorizer.transform([comment])
    if clf.predict(test_vector)==1:
        sentiment='Happy'
    else:
        sentiment='Unhappy'
    return sentiment




print(' Welcome to the Food review app,You were an amazing guest')


questions = [
    {
        'type': 'input',
        'name': 'comments',
        'message': 'Any comments on your Dinning experience?',
        'validate': commentValidator
        
    }
]

answers = prompt(questions, style=custom_style_3)





if answers['comments']=='':
    print('Hope to see you again,have a good one')
else:

    print("Your comment is {} and it seems you are {} ".format(answers['comments'],sentiment_predictor(answers['comments'])))
    #pprint(answers['comments'])






