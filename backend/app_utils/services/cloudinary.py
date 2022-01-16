import os

import cloudinary
import cloudinary.uploader
import cloudinary.api


cloudinary.config(
    cloud_name = os.getenv('STORAGE_NAME'), 
    api_key=os.getenv('STORAGE_API_KEY'), 
    api_secret=os.getenv('STORAGE_SECRET')
)


def delete_media(public_id: str):
    if not public_id:
        return
    cloudinary.api.delete_resources([public_id])


def upload_media(media, user):
    if not media:
        return

    import ipdb; ipdb.set_trace()

    result = cloudinary.uploader.upload(
        media.file,
        folder=os.getenv('STORAGE_MEDIA_FOLDER'),
    )


    return {
        'url': result['secure_url'],
        'media_id': result['public_id'],
        'content_type': 'application/png',
    }
