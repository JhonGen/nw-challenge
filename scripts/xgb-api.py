from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd
app = FastAPI()

class ScoringItem(BaseModel):
    MES_7:bool
    TIPOVUELO_I:bool
    OPERA_Copa_Air:bool
    OPERA_Latin_American_Wings:bool
    MES_12:bool
    OPERA_Grupo_LATAM:bool
    MES_10:bool
    OPERA_JetSmart_SPA:bool
    OPERA_Air_Canada:bool
    MES_9:bool
    OPERA_American_Airlines:bool

with open('XGB-model-cw.pkl', 'rb') as f:
    model = pickle.load(f)

@app.post('/')
async def scoring_endpoint(item:ScoringItem):
    df = pd.DataFrame([item.dict().values()], columns =['MES_7','TIPOVUELO_I','OPERA_Copa Air','OPERA_Latin American Wings','MES_12','OPERA_Grupo LATAM','MES_10','OPERA_JetSmart SPA','OPERA_Air Canada','MES_9', 'OPERA_American Airlines'])
    yhat = model.predict(df)
    return {"prediction": bool(yhat)}