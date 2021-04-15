from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

import datetime

app = FastAPI()

class Person(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    identification_number: Optional[str]
    date_of_birth: Optional[datetime.date]

class ComparisonRequest(BaseModel):
    person_1: Person
    person_2: Person

class ComparisonResponse(BaseModel):
    score: float
    
@app.post("/api/v1/comparison", response_model=ComparisonResponse)
def compare(request: ComparisonRequest):
    score = 1.0 if request.person_1.identification_number == request.person_2.identification_number else 0.0
    return { "score": score }
