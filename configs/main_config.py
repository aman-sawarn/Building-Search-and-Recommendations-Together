import sys
sys.path.append("../")

ANSWERS_FILE_NAME =  '../data/Answers.csv'
QUESTIONS_FILE_NAME =  '../data/Questions.csv'
TAGS_FILE_NAME =  '../data/Tags.csv'

ELASTIC_SEARCH_BODY_FOR_DOCUMENTS={"mappings": {
    "properties": {
          "title": {
                "type": "text"
          },
          "title_vector": {
                "type": "dense_vector",
                "dims": 512
      }
  }
   }
 }

 