#Work on Fast APi for the backend.
from pydantic import BaseModel
from fastapi import FastAPI, HTTPException



app = FastAPI()

assessments = []

# import basemodel from pydantic and assign class 
class AssessmentCreate(BaseModel):
    system_name: str
    organisation: str
    description: str

class AssessmentUpdate(BaseModel):
    system_name: str | None = None
    organisation: str | None = None
    description: str | None = None

#create get api
@app.get("/health")
async def health_check():
    return {
        "status": "OK",
        "service": "Responsibility Lens API"
    }

@app.get("/assessments")
async def assessments_list():
    return  assessments

#create post api

@app.post("/assessments")
async def create_assessment(assessment:AssessmentCreate):
    assessment_data = assessment.model_dump()

    assessment_data["id"] = len(assessments) + 1

    assessments.append(assessment_data)

    return assessment_data

#test an Id 
@app.get("/assessments/{assessment_id}")
async def get_assessment(assessment_id: int):
    for assessment in assessments:
        if assessment ["id"] == assessment_id:
            return assessment

    raise HTTPException(
        status_code=404,
        detail="Assessment not found"
    )

@app.patch("/assessments/{assessment_id}")
async def update_assessment(assessment_id: int, 
                            assessment_update: AssessmentUpdate):

    update_data = assessment_update.model_dump(exclude_unset=True)

    for assessment in assessments:
        if assessment ["id"] == assessment_id:
            assessment.update(update_data)
            return assessment

    raise HTTPException(
        status_code=404,
        detail="Assessment not Found"
    )

@app.delete("/assessments/{assessment_id}")
async def delete_assessment(assessment_id: int):
    for assessment in assessments:
        if assessment ["id"] == assessment_id:
            assessments.remove(assessment)
            return {
                "message": "Assessment deleted successfully",
                "id": assessment_id
                }

    raise HTTPException(
        status_code=404,
        detail="Assessment not Found"
    )