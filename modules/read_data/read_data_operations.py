import csv
import sys
sys.path.append("../")
from configs.main_config import ANSWERS_FILE_NAME, QUESTIONS_FILE_NAME, TAGS_FILE_NAME
# DONOT use pandas here as it laods all of data into RAM at once.


class ReadData:
    def __init__(self) -> None:
           self.answer_file=ANSWERS_FILE_NAME
           self.question_file=QUESTIONS_FILE_NAME
           self.tag_file=TAGS_FILE_NAME
    def count_content(self, file_name):
        cnt=0
        with open(file_name, encoding="latin1") as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',', )
            next(readCSV, None)  # skip the headers
            for row in readCSV:
                    cnt += 1
                    if cnt%1000==0:
                        print(f"Read {cnt} from file {file_name}")

    
            print(cnt,len(row))



                #print(cnt)




if __name__=="__main__":
    obj=ReadData()
    obj.count_content(ANSWERS_FILE_NAME)