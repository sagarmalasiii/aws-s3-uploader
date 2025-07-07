# 🗂️ Django AWS File Uploader API

A Django REST Framework-based API to upload, list, and delete files from an AWS S3 bucket.

---

## 🚀 Features

- 📤 Upload files directly to AWS S3
- 📁 View all uploaded files
- ❌ Delete files by filename
- 🔐 Environment variable-based configuration for security
- 📦 Clean Django project structure

---

## ⚙️ Technologies Used

- Python
- Django
- Django REST Framework
- Boto3 (AWS SDK)
- AWS S3
- python-decouple (.env file support)

---

## 📁 Folder Structure

aws_uploader/
├── api/
│ ├── views.py
│ ├── urls.py
├── aws_uploader/
│ ├── settings.py
│ ├── urls.py
├── .env
├── manage.py
├── requirements.txt
└── README.md

## 🔧 Setup Instructions

### 1. Clone the Repository

git clone https://github.com/sagarmalasiii/aws-s3-uploader.git
cd aws-s3-uploader

### 2. Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate # On Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. Add AWS Credentials in .env

AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_STORAGE_BUCKET_NAME=your-bucket-name

### 4. Run Migrations & Start Server

python manage.py migrate
python manage.py runserver


🧑‍💻 Author
Sagar Malasi
GitHub: @sagarmalasiii
LinkedIn: sagarmalasiii
