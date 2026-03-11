from fastapi import FastAPI,HTTPException
from src.schemas.schemas import UserRecord
from src.core.predictor import get_prediction



app = FastAPI()


@app.post("/UserDetails")
def get_userdetails(user:UserRecord):






@app.post("/prediction")
def return_prediction(id:int):
    try:
        prediction = get_prediction(input)
        return prediction

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )


