import json
import requests

from django.conf import settings
from media_management.errors import ClearCutLambdaError


class ClearCutProcessorService:

    def process_image(self, image_to_upload, clear_cut_config=None):
        # Fire an uploaded media to S3, to be processed with the original and clear_cut image stored
        request_data = {
            'image': image_to_upload,
        }

        try:
            request_data.update({
                'image_size_threshold': clear_cut_config.image_size_threshold,
                'noisy_pixel_tolerance': clear_cut_config.noisy_pixel_tolerance,
            })
        except (TypeError, AttributeError):
            pass

        request_data = json.dumps(request_data)

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
            print(f'response={response}')
            raise ClearCutLambdaError(f'[{response.status_code}] {response.json()}')

        original_s3_url = f'{saved_s3_location}0001_size_reduced_image.png'
        clear_cut_s3_url = f'{saved_s3_location}0008_edge_masked_image.png'

        return original_s3_url, clear_cut_s3_url
