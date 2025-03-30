from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from crew import crew
import re
import json

app = FastAPI()

class ShlokaRequest(BaseModel):
    shloka: str

def extract_json_from_output(output_str):
    json_match = re.search(r'```json\n(.*?)\n```', output_str, re.DOTALL)
    if json_match:
        json_str = json_match.group(1)
        try:
            return json.loads(json_str)
        except json.JSONDecodeError:
            return None
    return None

@app.post("/summarize_shloka")
def summarize_shloka(request: ShlokaRequest):
    try:
        result = crew.kickoff(inputs={'topic': request.shloka})
        output_str = str(result)
        structured_json = extract_json_from_output(output_str)

        if not structured_json:
            raise ValueError("Could not parse JSON from output.")

        return {"status": "success", "data": structured_json}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    