from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Optional

import boto3
import httpx
import typer
from pydantic import BaseModel
from rich import print

from bl_tools import R2_AWS_ACCESS_KEY_ID, R2_AWS_SECRET_ACCESS_KEY, R2_ENDPOINT_URL


class R2Upload(BaseModel):
    source_file_path: str
    destination_file_path: str
    bucket_name: str


class R2Client:
    def __init__(
        self,
        endpoint_url: str | None,
        aws_access_key_id: str | None,
        aws_secret_access_key: str | None,
    ) -> None:
        """
        Initialize an R2 instance.

        Args:
            endpoint_url (str, optional): The URL of the R2 endpoint. Defaults to R2_ENDPOINT_URL.
            aws_access_key_id (str, optional): The AWS access key ID. Defaults to R2_AWS_ACCESS_KEY_ID.
            aws_secret_access_key (str, optional): The AWS secret access key. Defaults to R2_AWS_SECRET_ACCESS_KEY.
        """
        # Validate that all required values are provided.
        if endpoint_url is None:
            raise ValueError("endpoint_url is required.")
        if aws_access_key_id is None:
            raise ValueError("aws_access_key_id is required.")
        if aws_secret_access_key is None:
            raise ValueError("aws_secret_access_key is required.")

        self._endpoint_url = endpoint_url
        self._aws_access_key_id = aws_access_key_id
        self._aws_secret_access_key = aws_secret_access_key

        # Initialize the S3 client.
        self.s3 = boto3.resource(
            "s3",
            endpoint_url=self._endpoint_url,
            aws_access_key_id=self._aws_access_key_id,
            aws_secret_access_key=self._aws_secret_access_key,
        )

    @property
    def endpoint_url(self) -> str:
        return self._endpoint_url

    @property
    def aws_access_key_id(self) -> str:
        return self._aws_access_key_id

    @property
    def aws_secret_access_key(self) -> str:
        return self._aws_secret_access_key

    def upload_file(
        self,
        upload: R2Upload,
    ):
        self.s3.meta.client.upload_file(
            upload.source_file_path,
            upload.bucket_name,
            upload.destination_file_path,
        )

    def upload_files(
        self,
        uploads: list[R2Upload],
        threads: int = 8,
    ):
        with ThreadPoolExecutor(max_workers=threads) as executor:
            executor.map(self.upload_file, uploads)
