
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import boto3
from decouple import config

AWS_ACCESS_KEY = config("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = config("AWS_SECRET_ACCESS_KEY")
BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")

s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)

class UploadFileView(APIView):
    def post(self, request):
        file = request.FILES.get("file")
        if not file:
            return Response({"error": "No file provided"}, status=400)
        s3.upload_fileobj(file, BUCKET_NAME, file.name)
        file_url = f"https://{BUCKET_NAME}.s3.amazonaws.com/{file.name}"
        return Response({"message": "File uploaded", "url": file_url})

class ListFilesView(APIView):
    def get(self, request):
        files = s3.list_objects_v2(Bucket=BUCKET_NAME)
        file_list = [f["Key"] for f in files.get("Contents", [])]
        return Response({"files": file_list})

class DeleteFileView(APIView):
    def delete(self, request, filename):
        s3.delete_object(Bucket=BUCKET_NAME, Key=filename)
        return Response({"message": f"{filename} deleted"})
