import boto3
import requests
from io import BytesIO
from PIL import Image
from bs4 import BeautifulSoup
from .models import Product, ProductGallery

# S3 Configuration
S3_BUCKET_NAME = "app8"
S3_BASE_UPLOAD_URL = "http://nos.wjv-1.neo.id"
S3_BASE_ACCESS_URL = "https://nos.wjv-1.neo.id"

s3_client = boto3.client(
    "s3",
    endpoint_url=S3_BASE_UPLOAD_URL,
    aws_access_key_id="009ed54e444dc9645ab3",
    aws_secret_access_key="FRaaDb55PRWIEyYPjTIrykKhB3FePmciINPGXmvI",
)


def extract_list_items(rich_text):
    """Extracts list items from a Wagtail RichText field."""
    soup = BeautifulSoup(rich_text, "html.parser")
    return [li.get_text(strip=True) for li in soup.find_all("li")]


def resize_image(image_data, max_width, max_height, quality=90):
    img = Image.open(BytesIO(image_data))
    aspect_ratio = img.width / img.height

    if aspect_ratio > max_width / max_height:
        new_width = int(img.height * (max_width / max_height))
        left_margin = (img.width - new_width) / 2
        top_margin = 0
        right_margin = left_margin + new_width
        bottom_margin = img.height
    else:
        new_height = int(img.width * (max_height / max_width))
        left_margin = 0
        top_margin = (img.height - new_height) / 2
        right_margin = img.width
        bottom_margin = top_margin + new_height

    img_cropped = img.crop((left_margin, top_margin, right_margin, bottom_margin))
    img_resized = img_cropped.resize((max_width, max_height), Image.LANCZOS)

    output_io = BytesIO()
    img_resized.save(output_io, "WebP", quality=quality)
    output_io.seek(0)

    return output_io


def process_blog_content(blog_content, max_width, max_height, quality=90):
    for item in blog_content:
        if item.block_type == "image":
            original_url = item.value.file.url
            image_filename = original_url.split("/")[-1]

            s3_original_path = f"app8/original_images/{image_filename}"
            s3_resized_path = f"app8/blog_utils/resized_images/{image_filename}"

            try:
                s3_client.head_object(Bucket=S3_BUCKET_NAME, Key=s3_resized_path)
                print("Resized image already exists on S3.")
            except:
                print("Resizing image...")

                response = requests.get(original_url, stream=True)
                if response.status_code != 200:
                    raise Exception(f"Failed to download image: {original_url}")

                resized_image = resize_image(
                    response.content, max_width, max_height, quality
                )

                s3_client.upload_fileobj(
                    resized_image,
                    S3_BUCKET_NAME,
                    s3_resized_path,
                    ExtraArgs={"ContentType": "image/webp", "ACL": "public-read"},
                )

            item.processed_image_url = (
                f"{S3_BASE_ACCESS_URL}/{S3_BUCKET_NAME}/{s3_resized_path}"
            )
        elif item.block_type in ["unordered_list", "ordered_list"]:
            item.list_items = extract_list_items(item.value.source)


def process_page_content(blog_content, max_width, max_height, quality=90):
    for item in blog_content:
        if item.block_type == "image":
            original_url = item.value.file.url
            image_filename = original_url.split("/")[-1]

            s3_original_path = f"app8/original_images/{image_filename}"
            s3_resized_path = f"app8/page_utils/resized_images/{image_filename}"

            try:
                s3_client.head_object(Bucket=S3_BUCKET_NAME, Key=s3_resized_path)
                print("Resized image already exists on S3.")
            except:
                print("Resizing image...")

                response = requests.get(original_url, stream=True)
                if response.status_code != 200:
                    raise Exception(f"Failed to download image: {original_url}")

                resized_image = resize_image(
                    response.content, max_width, max_height, quality
                )

                s3_client.upload_fileobj(
                    resized_image,
                    S3_BUCKET_NAME,
                    s3_resized_path,
                    ExtraArgs={"ContentType": "image/webp", "ACL": "public-read"},
                )

            item.processed_image_url = (
                f"{S3_BASE_ACCESS_URL}/{S3_BUCKET_NAME}/{s3_resized_path}"
            )
        elif item.block_type in ["unordered_list", "ordered_list"]:
            item.list_items = extract_list_items(item.value.source)




def process_product_content(blog_content, max_width, max_height, quality=90):
    for item in blog_content:
        if item.block_type == "image":
            original_url = item.value.file.url
            image_filename = original_url.split("/")[-1]

            s3_original_path = f"app8/original_images/{image_filename}"
            s3_resized_path = f"app8/product_utils/resized_images/{image_filename}"

            try:
                s3_client.head_object(Bucket=S3_BUCKET_NAME, Key=s3_resized_path)
                print("Resized image already exists on S3.")
            except:
                print("Resizing image...")

                response = requests.get(original_url, stream=True)
                if response.status_code != 200:
                    raise Exception(f"Failed to download image: {original_url}")

                resized_image = resize_image(
                    response.content, max_width, max_height, quality
                )

                s3_client.upload_fileobj(
                    resized_image,
                    S3_BUCKET_NAME,
                    s3_resized_path,
                    ExtraArgs={"ContentType": "image/webp", "ACL": "public-read"},
                )

            item.processed_image_url = (
                f"{S3_BASE_ACCESS_URL}/{S3_BUCKET_NAME}/{s3_resized_path}"
            )
        elif item.block_type in ["unordered_list", "ordered_list"]:
            item.list_items = extract_list_items(item.value.source)


def set_main_images(products):
    for product in products:
        images = ProductGallery.objects.filter(product=product)[:2]
        first_image = images[0] if images else None
        second_image = images[1] if len(images) > 1 else None
        product.first_image = first_image.image_thumbnail.url if first_image else None
        product.second_image = (
            second_image.image_thumbnail.url if second_image else None
        )