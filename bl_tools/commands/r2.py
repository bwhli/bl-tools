from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Optional

import boto3
import httpx
import typer
from pydantic import BaseModel
from rich import print

from bl_tools import R2_AWS_ACCESS_KEY_ID, R2_AWS_SECRET_ACCESS_KEY, R2_ENDPOINT_URL
from bl_tools.r2_client import R2Client, R2Upload

app = typer.Typer()


@app.command(
    name="upload",
    help="Upload a single file to a Cloudflare R2 bucket.",
)
def upload(
    source_file_path: Path,
    destination_file_path: Path,
    bucket_name: str,
    endpoint_url: str = typer.Option(
        R2_ENDPOINT_URL,
        "--endpoint-url",
        "-e",
    ),
    aws_access_key_id: str = typer.Option(
        R2_AWS_ACCESS_KEY_ID,
        "--access-key-id",
        "-a",
    ),
    aws_secret_access_key: str = typer.Option(
        R2_AWS_SECRET_ACCESS_KEY,
        "--secret-access-key",
        "-s",
    ),
):
    r2_client = R2Client(
        endpoint_url,
        aws_access_key_id,
        aws_secret_access_key,
    )

    upload = R2Upload(
        source_file_path=str(source_file_path),
        destination_file_path=str(destination_file_path),
        bucket_name=bucket_name,
    )

    r2_client.upload_file(upload)

    print(f"{source_file_path} has been uploaded!")
