import os
import base64
from together import Together
import Api as key

client = Together(api_key=key.key)
print("\n" + "="*50)
print("Welcome to the Multi-Function Bot!")
print("="*50 + "\n")

user_input = input("Do you want to process your input as 'text' or 'image'? (Enter 'text' or 'image'): ").strip().lower()
if user_input == 'text':
        def chat(query):
                response = client.chat.completions.create(
                model="meta-llama/Meta-Llama-3.1-405B-Instruct-Turbo",
                messages=[
                        {
                                "role" : "user",
                                "content" : query
                        }
                ],
                
                max_tokens=512,
                temperature=0.7,
                top_p=0.7,
                top_k=50,
                repetition_penalty=1,
                stop=["<|eot_id|>"],
                # stream=True
                )

                print("\n" + "="*50)
                print(f"AI: {response.choices[0].message.content}")
                print("="*50 + "\n")

        print("\n" + "="*50)
        print("Welcome to the Text Processing Chatbot!")
        print("="*50 + "\n")

        while True:
         query = input("Please enter your question (or type 'exit' to quit): ")
         if query.lower() == 'exit':
                 break
         chat(query)

elif user_input == 'image':
# Get user input for the prompt and filename
                print("\n" + "="*50)
                print("Welcome to the Image Generation Tool!")
                print("="*50 + "\n")
        
                prompt = input("Enter the prompt for the image: ")
                filename = input("Enter the filename to save the image (e.g., 'my_image.png'): ")

                # Define image generation parameters
                model = "stabilityai/stable-diffusion-xl-base-1.0"
                width = 1024
                height = 1024
                steps = 40
                n = 1  # Generate only one image
                seed = 7677

                # Generate images using the Together API
                response = client.images.generate(
                prompt=prompt,
                model=model,
                width=width,
                height=height,
                steps=steps,
                n=n,
                seed=seed
                )

                # Check if the response contains the image data
                if response.data:
                # Decode the base64-encoded image data
                        image_data = response.data[0].b64_json
                        image_bytes = base64.b64decode(image_data)
                
                # Save the image to the specified file
                        with open(filename, 'wb') as image_file:
                                image_file.write(image_bytes)

                        print("\n" + "="*50)
                        print(f"Image has been saved successfully as '{filename}'.")
                        print("="*50 + "\n")
                else:
                        print("\n" + "="*50)
                        print("No image data found in the response.")
                        print("="*50 + "\n")