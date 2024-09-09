import os
import requests
from bs4 import BeautifulSoup

Not_found_link='data:image/png;base64,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'

def get_images_links(searchTerm):
    try:
        searchUrl = "https://www.google.com/search?q={}&site=webhp&tbm=isch".format(searchTerm)
        d = requests.get(searchUrl).text
        soup = BeautifulSoup(d, 'html.parser')

        img_tags = soup.find_all('img')

        imgs_urls = []
        for img in img_tags:
            if img['src'].startswith("http"):
                imgs_urls.append(img['src'])

        return(imgs_urls[0])
    except:
        return Not_found_link

# Ensure you have a function to fetch exercise images as you provided
def get_exercise_images_links(disease):
    """Get exercise images based on the specified disease."""
    base_path = os.path.join(os.getcwd(), r'C:\\SARAVANA\\FINALLL DIET\\Diet-Recommendation-System\\exercise_images')
    disease_folders = {
        'none': 'None',
        'diabetic': 'diabetic',
        'pcos': 'pcos',
        'pressure': 'pressure',
        'ulcer': 'ulcer',
        'overall': 'Overall'
    }
    folder = disease_folders.get(disease.lower(), 'diabetic')
    image_path = os.path.join(base_path, folder)

    exercise_images = []
    if os.path.exists(image_path):
        for image_name in os.listdir(image_path):
            if image_name.endswith(('.jpg', '.jpeg', '.png')):
                image_link = os.path.join(image_path, image_name)
                exercise_images.append({
                    'link': image_link,
                    'description': f'Exercise for {disease} - {image_name}'
                })
    else:
        exercise_images = [{'link': 'Not_found_link', 'description': 'No image available'}]

    return exercise_images































































# def get_exercise_images_links(disease):
#     """Get exercise images based on the specified disease."""
#     # Define the base path where exercise images are stored
#     base_path = os.path.join(os.getcwd(), r'C:\SARAVANA\FINALLL DIET\Diet-Recommendation-System\exercise_images')
#     disease_folders = {
#         'none': 'None',
#         'diabetic': 'diabetic',
#         'pcos': 'pcos',
#         'pressure': 'pressure',
#         'ulcer': 'ulcer',
#         'overall': 'Overall',
#         'other': 'other'  
#         # Default folder for unmapped diseases
#     }

#     # Get the folder name based on the disease, defaulting to 'other' if not listed
#     folder = disease_folders.get(disease.lower(), 'other')
#     image_path = os.path.join(base_path, folder)
    
#     # Initialize list for exercise images
#     exercise_images = []

#     # Check if the folder exists
#     if os.path.exists(image_path):
#         # List all images in the selected folder
#         for image_name in os.listdir(image_path):
#             if image_name.endswith(('.jpg', '.jpeg', '.png')):
#                 image_link = os.path.join(image_path, image_name)
#                 exercise_images.append({
#                     'link': image_link,
#                     'description': f'Exercise for {disease} - {image_name}'
#                 })
#     else:
#         # Folder does not exist or is empty
#         exercise_images = [{'link': Not_found_link, 'description': 'No images available'}]
    
#     return exercise_images



    
# def get_exercise_images_links(disease):
#     """Get exercise images based on the specified disease."""
#     # Define the base path where exercise images are stored
#     base_path = os.path.join(os.getcwd(), r'C:\SARAVANA\FINALLL DIET\Diet-Recommendation-System\exercise_images')

#     # Map diseases to their corresponding folders
#     disease_folders = {
#         'none': 'None',
#         'diabetic': 'diabetic',
#         'pcos': 'pcos',
#         'pressure': 'pressure',
#         'ulcer': 'ulcer',
#         'overall': 'Overall',
#         'other': 'other'  # Default folder for unmapped diseases
#     }

#     # Get the folder name based on the disease, defaulting to 'other' if not listed
#     folder = disease_folders.get(disease.lower(), 'other')
#     image_path = os.path.join(base_path, folder)
    
#     # Initialize list for exercise images
#     exercise_images = []

#     # Check if the folder exists
#     if os.path.exists(image_path):
#         # List all images in the selected folder
#         for image_name in os.listdir(image_path):
#             if image_name.endswith(('.jpg', '.jpeg', '.png')):
#                 image_link = os.path.join(image_path, image_name)
#                 exercise_images.append({
#                     'link': image_link,
#                     'description': f'Exercise for {disease} - {image_name}'
#                 })
#     else:
#         # Folder does not exist or is empty
#         exercise_images = [{'link': Not_found_link, 'description': 'No images available'}]
    
#     return exercise_images

# # Example usage
# disease_selected = 'diabetic'  # Example disease selection
# images = get_exercise_images_links(disease_selected)

# # Displaying images
# for img in images:
#     print(f"Image Link: {img['link']} - {img['description']}")
    
# def get_exercise_images_links(disease):
#     """Get exercise images based on the specified disease."""
#     # Define the base path where exercise images are stored
#     base_path = os.path.join(os.getcwd(), r'C:\SARAVANA\FINALLL DIET\Diet-Recommendation-System\exercise_images')

#     # Map diseases to their corresponding folders
#     disease_folders = {
#         'none': 'None',
#         'diabetic': 'diabetic',
#         'pcos': 'pcos',
#         'pressure': 'pressure',
#         'ulcer': 'ulcer',
#         'overall': 'Overall',
#         'other':'other'
#     }

#     folder = disease_folders.get(disease, 'ulcer')  # Default to 'other' if disease is not listed
#     image_path = os.path.join(base_path, folder)
    
#     # List all images in the selected folder
#     exercise_images = []
#     for image_name in os.listdir(image_path):
#         if image_name.endswith(('.jpg', '.jpeg', '.png')):
#             image_link = os.path.join(image_path, image_name)
#             exercise_images.append({
#                 'link': image_link,
#                 'description': f'Exercise for {disease} - {image_name}'
#             })

#     return exercise_images

# def get_exercise_images_links(disease):
#     """Get exercise images based on the specified disease."""
#     # Define the base path where exercise images are stored
#     base_path = os.path.join(os.getcwd(), r'C:\SARAVANA\FINALLL DIET\Diet-Recommendation-System\exercise_images')

#     # Map diseases to their corresponding folders
#     disease_folders = {
#         'none': 'None',
#         'diabetic': 'diabetic',
#         'pcos': 'pcos',
#         'pressure': 'pressure',
#         'ulcer': 'ulcer',
#         'overall': 'Overall'
#     }

#     # Get the folder name based on the disease, defaulting to 'ulcer' if not listed
#     folder = disease_folders.get(disease.lower(), 'other')
#     image_path = os.path.join(base_path, folder)

#     exercise_images = []

#     # Check if the folder exists and fetch images, else use fallback images
#     if os.path.exists(image_path):
#         for image_name in os.listdir(image_path):
#             if image_name.endswith(('.jpg', '.jpeg', '.png')):
#                 image_link = os.path.join(image_path, image_name)
#                 exercise_images.append({
#                     'link': image_link,
#                     'description': f'Exercise for {disease} - {image_name}'
#                 })
#     else:
#         # Fallback to Google images if the folder doesn't exist or is empty
#         exercise_images = [{'link': link, 'description': f'Exercise for {disease}'} for link in get_images_links(disease)]
    
#     # If no images found, use the default 'not found' image
#     if not exercise_images:
#         exercise_images = [{'link': Not_found_link, 'description': 'No image available'}]

#     return exercise_images

# # Example usage
# disease_selected = 'diabetic'  # Example disease selection
# images = get_exercise_images_links(disease_selected)

# # Displaying images
# for img in images:
#     print(f"Image Link: {img['link']} - {img['description']}")

