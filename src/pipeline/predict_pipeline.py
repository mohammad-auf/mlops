import sys ,os
import pandas as pd
from src.exception import CustomException
from src.logger import logging
from src.utils import load_object



class PredictedPipeline:
    def __init__(self):

        pass
    
    def predicted(self,features):
        try:
            logging.info("Model has been loaded from load object")
            model_path=os.path.join("artifacts","model.pkl")
            preprocessor_path=os.path.join('artifacts','proprocessor.pkl')
            model =load_object(model_path)
            preoprocessor =load_object(preprocessor_path)
            
            data_scaled = preoprocessor.transform(features)
            preds =model.predict(data_scaled)
            return preds
        except Exception as e:
            logging.error(f"Error in prediction: {e}")
            raise CustomException(e,sys)

class CustomData:
    def __init__(self,gender,race,parental_level_education,lunch_type,test_preparation,writing_score,reading_score):
        self.gender =gender
        self.race_ethnicity = race
        self.parental_level_of_education =parental_level_education
        self.lunch =lunch_type
        self.test_preparation_course =test_preparation
        self.writing_score =writing_score
        self.reading_score = reading_score
        
    def get_data_as_data_frame(self):
        try:
            custom_data_input_dict ={
                "gender":[self.gender],
                "race_ethnicity":[self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course":[self.test_preparation_course],
                "writing_score":[self.writing_score],
                "reading_score":[self.reading_score]
            }
            
            return pd.DataFrame(custom_data_input_dict)
        except Exception as e:
            raise CustomException(e,sys)
        
    