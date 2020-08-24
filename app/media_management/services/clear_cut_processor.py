import json
import requests

from django.conf import settings
from media_management.errors import ClearCutLambdaAPITimeout


class ClearCutProcessorService:

    def process_image(self, image_to_upload):
        # Fire an uploaded media to S3, to be processed with the original and clear_cut image stored
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

        try:
            saved_s3_location = response.json()['s3_results']
        except KeyError:
            raise ClearCutLambdaTimeout

        original_s3_url = f'{saved_s3_location}0001_size_reduced_image.png'
        clear_cut_s3_url = f'{saved_s3_location}0008_edge_masked_image.png'

        return original_s3_url, clear_cut_s3_url
