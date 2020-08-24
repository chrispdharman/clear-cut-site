import json
import requests

from django.conf import settings


class ClearCutProcessorService:

    def process_image(self, image_to_upload):
        # Fire an uploaded media to S3, to be processed with the original and clear_cut image stored
        print('clear cutting image...')

        print(f'image_to_upload={image_to_upload}')

        request_data = json.dumps({
            'image': image_to_upload,
        })

        response = requests.post(
            url=settings.CLEAR_CUT_URL,
            json=request_data,
            headers={
                'Content-Type': 'application/json',
                'X-Api-Key': settings.CLEAR_CUT_API_KEY,
            }
        )

        print(f'response={response}')

        original_s3_url, clear_cut_s3_url = (None, None)

        return original_s3_url, clear_cut_s3_url
