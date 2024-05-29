from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
import requests, os
from dotenv import load_dotenv
from django.core.files.storage import FileSystemStorage
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

load_dotenv()

connection_string = os.getenv("AZURE_STORAGE_CONNECTION_STRING_2")
resume_container = os.getenv("RESUME_CONTAINER_NAME")


# Create your views here.
def index(request):
    return render(request, "portfolio/index.html")


def resume(request):
    return render(request, "portfolio/resume.html")


def new_resume(request):
    print("=============hit ================")
    if request.method == "POST" and request.FILES["new_resume"]:
        print("=============PAST POST ================")
        print(request.POST.get("new_resume"))
        new_resume = request.FILES["new_resume"]

        print("=============PAST================")
        if new_resume:
            new_resume = request.FILES["new_resume"]
            print("=====================================")
            print(new_resume.name)

            blob_service_client = BlobServiceClient.from_connection_string(
                connection_string
            )

            # create a blob client using the local file name as then name for the blob
            blob_client = blob_service_client.get_blob_client(
                container=resume_container, blob="Amos_Njoroge_Resume.pdf"
            )

            print("\nUploading to Azure Storage as blob:\n\t" + new_resume.name)
            blob_client.upload_blob(new_resume, overwrite=True)

            return redirect(reverse("resume"))

    return render(request, "portfolio/new_resume.html")


def download_resume(request):
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    blob_client = blob_service_client.get_blob_client(
        container=resume_container, blob="Amos_Njoroge_Resume.pdf"
    )

    # Download the blob content to a byte array
    download_stream = blob_client.download_blob()
    pdf_content = download_stream.readall()

    # Create the response
    response = HttpResponse(pdf_content, content_type="application/pdf")
    response["Content-Disposition"] = 'attachment; filename="Amos_Njoroge_Resume.pdf"'

    return response
