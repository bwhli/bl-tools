import os

from dotenv import load_dotenv

load_dotenv()

R2_ENDPOINT_URL = os.getenv("R2_ENDPOINT_URL")
R2_AWS_ACCESS_KEY_ID = os.getenv("R2_AWS_ACCESS_KEY_ID")
R2_AWS_SECRET_ACCESS_KEY = os.getenv("R2_AWS_SECRET_ACCESS_KEY")

print(R2_ENDPOINT_URL)
