from fastapi import APIRouter
import base64
from io import BytesIO
from apps.mathNotes.utils import analyze_image  # Importing analyze_image function
from schema import ImageData
from PIL import Image

router = APIRouter()

@router.post('')
async def run(data: ImageData):
    try:
        image_data = base64.b64decode(data.image.split(",")[1])
        image_bytes = BytesIO(image_data)
        image = Image.open(image_bytes)
        responses = analyze_image(image, dict_of_vars=data.dict_of_vars)
        data = []
        for response in responses:
            data.append(response)
        print('response in route: ', responses)
        return {
            "message": "Image processed", 
            "type": "success",
            "data": data,
        }
    except Exception as e:
        print(f"Error processing request: {str(e)}")
        return {
            "message": "Error processing image",
            "type": "error",
            "error": str(e)
        }
        