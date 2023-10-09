from moviepy.editor import *
from pathlib import Path
import numpy as np
import requests
import cv2
from PIL import Image
import io
from io import BytesIO
import os
import requests
from PIL import Image
from io import BytesIO

# Create a function to download and save images from URLs
def download_images(url_list, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Loop through the list of URLs
    for i, url in enumerate(url_list):
        try:
            # Send an HTTP GET request to the URL
            response = requests.get(url)
            
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Open the image using PIL
                image = Image.open(BytesIO(response.content))

                # Generate a unique filename
                filename = f"image_{i+1}.jpg"
                image = image.convert('RGB')
                
                image.save(os.path.join(output_folder, filename))

                print(f"Image {i+1} downloaded and saved as {filename}")
            else:
                print(f"Failed to download image {i+1}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error downloading image {i+1}: {str(e)}")

def url2image(image_url):
    # Send an HTTP GET request to fetch the image
    response = requests.get(image_url)
    
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Get the content type of the response
        content_type = response.headers.get('Content-Type')
        
        # Check if the content type indicates an image (e.g., image/jpeg, image/png)
        if content_type and content_type.startswith('image'):
            # Read the image data as bytes
            image_data = response.content
            
            # Create a BytesIO object and write the image data
            image_io = io.BytesIO(image_data)
            
            # Open the image using Pillow (PIL)
            image = Image.open(image_io)
            
            # Convert the image to RGB format if it's not already
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Convert the Pillow Image to a NumPy array
            image_array = np.array(image)
            
            return image_array
        else:
            print(f"URL does not contain an image. Content type: {content_type}")
            return None
    else:
        print(f"Failed to fetch the image. Status code: {response.status_code}")
        return None



def create_video(images_list, duration, audio):
    img_clips = []
    duration_per_image = duration/len(images_list)
#creating slide for each image
    for img_path in images_list:
        slide = ImageClip(url2image(img_path),duration=duration_per_image)
        img_clips.append(slide)
    #concatenating slides
    video_slides = concatenate_videoclips(img_clips, method='compose')
    #exporting final video
    video_slides.write_videofile("output_video.mp4", fps=24)



if __name__ == "__main__":
    images_list = {'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$smallthumbimg_32357832.jpg',
                   'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$mediumthumbimg_1639668796.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$thumbimg_991609556.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$smallthumbimg_1820244206.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$thumbimg_1763513712.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$mediumthumbimg_1870567037.jpeg', 'https://news.google.com/Content/images/Homepage_Assets/footer-logo.png', 'https://news.google.com/Content/images/menu.png', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$thumbimg_1580428817.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$thumbimg_2089172002.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$thumbimg_1929733244.jpg', 'https://sb.scorecardresearch.com/p?c1=2&c2=37226950&cv=3.6.0&cj=1', 'https://news.google.com/Content/images/Homepage_Assets/Subscribe-logo.png', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$mediumthumbimg_784858077.jpg', 'https://news.google.com/Content/images/Logo_eng.png', 'https://news.google.com/Content/images/Logo_punjabi.png', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$mediumthumbimg_683429335.jpg', 'https://news.google.com/Content/images/Search.png', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$mediumthumbimg_816153959.JPG', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$thumbimg_1240019281.jpg', 'https://news.google.com/Content/images/Google-News-Follow.png', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$mediumthumbimg_1137548555.jpg', 'https://news.google.com/Content/images/Logo_eng_1.png', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$mediumthumbimg_2138906679.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$largeimg_1436700148.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$smallthumbimg_1412128110.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$mediumthumbimg_1955435205.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$smallthumbimg_2019378156.jpg', 'https://englishtribuneimages.blob.core.windows.net/gallary-content/2023/9/2023_9$smallthumbimg_136765304.jpg', 'https://www.facebook.com/tr?id=233432884227299&ev=PageView&noscript=1'}
    #create_video(images_list, 10, None)
    download_images(images_list, "output_folder")