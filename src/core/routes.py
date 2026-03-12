from fastapi import FastAPI,HTTPException
from src.schemas.schemas import UserRecord
from src.core.predictor import get_prediction
from src.database.curd import insert_in_userrecords,insert_in_loan_predictions,get_by_id
from src.database.tables import userrecords,loan_predictions
app = FastAPI()





@app.post("/insertrecord")
def get_insertuserdetails(user:UserRecord):
    try:
        insert_in_userrecords(user.model_dump())
        result = get_prediction(user)
        insert_in_loan_predictions(result)
        return {'response':'Successful'}
    except Exception as e:
        return {"error": str(e)}

@app.get("/getUserrecord/{user_id}")
def get_user_records(user_id: int):
    result = get_by_id(user_id, userrecords)
    if result:
        return result

    return {"message": "User not found"}
@app.get("/getLoanriskrecord/{user_id}")
def get_loanrisk_records(user_id: int):
    result = get_by_id(user_id, loan_predictions)
    if result:
        return result

    return {"message": "User not found"}