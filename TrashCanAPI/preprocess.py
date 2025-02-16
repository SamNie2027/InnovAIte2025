from PIL import Image
from io import BytesIO
import base64
import logging
import re

def preprocess(img):
    '''
    Processes base64 image string from frontend into PIL Image
    Returns False if unable to process, PIL Image otherwise
    '''
    if not img:
        logging.error("No image provided")
        return False

    try:
        # Remove data URI prefix if present
        if img.startswith('data:image'):
            img = img.split(',', 1)[1]

        # Add padding if needed (common issue with some base64 implementations)
        missing_padding = len(img) % 4
        if missing_padding:
            img += '=' * (4 - missing_padding)

        # Decode base64 string
        decoded_img = base64.b64decode(img)
        
        # Convert to PIL Image
        img_buffer = BytesIO(decoded_img)
        pil_img = Image.open(img_buffer)
        
        # Convert to RGB if necessary (for PNG/JPG compatibility)
        if pil_img.mode != 'RGB':
            pil_img = pil_img.convert('RGB')
            
        return pil_img
        
    except (base64.binascii.Error, ValueError) as e:
        logging.error(f"Base64 decoding failed: {str(e)}")
        return False
    except Exception as e:
        logging.error(f"Image processing failed: {str(e)}")
        return False