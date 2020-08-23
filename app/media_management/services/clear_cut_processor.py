class ClearCutProcessorService:

    def process_image(self, image_to_upload):
        # Fire an uploaded media to S3, to be processed with the original and clear_cut image stored
        print('clear cutting image...')

        original_s3_url, clear_cut_s3_url = (None, None)

        return original_s3_url, clear_cut_s3_url
