import base64
from openai import OpenAI
from tts2 import tts
def name_meds():
  client = OpenAI(api_key='ENTER_OPENAI_APIKEY')

  # Function to encode the image
  def encode_image(image_path):
    with open(image_path, "rb") as image_file:
      return base64.b64encode(image_file.read()).decode('utf-8')

  # Path to your image
  image_path = "/home/alpha3/Desktop/Arm_project/24-25 sem1/Final pipeline/panorama.png"

  # Getting the base64 string
  base64_image = encode_image(image_path)

  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "name of the medicine",
          },
          {
            "type": "image_url",
            "image_url": {
              "url":  f"data:image/jpeg;base64,{base64_image}"
            },
          },
        ],
      }
    ],
  )


  print(response.choices[0].message.content)
  tts(response.choices[0].message.content)
if __name__ == "__main__":
  name_meds()