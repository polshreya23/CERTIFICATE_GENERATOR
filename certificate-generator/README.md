# Bulk Certificate Generator (Offline Web App)

A fast and efficient web application that generates certificates in bulk using a CSV file.
This tool works completely offline and helps organizations create hundreds of certificates in seconds.

## Features

1.Upload participant data (CSV file)
2.Upload certificate template (PNG/JPG)
3.Generate certificates instantly
4.Download all certificates as ZIP
5.Works completely offline
6.Automatic center alignment of names

## Tech Stack

Backend: Flask (Python)
Data Handling: Pandas
Image Processing: Pillow (PIL)
Frontend: HTML, CSS

## Project Structure

certificate-generator/
│
├── app.py
├── templates/
│   └── index.html
├── uploads/
├── certificates/
└── README.md

##  How It Works

1.User uploads a CSV file containing participant names
2.User uploads a certificate template (image)
3.The system reads the CSV using Pandas
4.Each name is placed on the certificate using Pillow
5.Certificates are generated and saved
6.All certificates are zipped and downloaded

## 📄 CSV Format

Make sure your CSV file follows this format:

Name
Shreya
Saloni
Akshata
Anjali

## Installation & Setup

### 1️.Clone the repository

git clone https://github.com/your-username/certificate-generator.git
cd certificate-generator

### 2️.Install dependencies

pip install flask pandas pillow

### 3️.Run the application

python app.py

### 4️.Open in browser

http://127.0.0.1:5000

## Usage

1.Upload your CSV file
2.Upload certificate template (PNG/JPG)
3.Enter text position (Y-axis)
4.Click **Generate Certificates**
5.Download ZIP file

## Key Highlights

1.Fully offline solution (no internet required)
2.Saves hours of manual work
3.Scalable for large events
4.Beginner-friendly implementation

## Future Improvements

1.Add QR code verification
2.Drag-and-drop text positioning
3.Live preview before generation
4.Multiple fields (course, date, etc.)

## Author

Shreya Pol

## If you like this project

Give it a ⭐ on GitHub!
