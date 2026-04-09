from flask import Flask, render_template, request, send_file
import pandas as pd
from PIL import Image, ImageDraw, ImageFont
import os
import zipfile

app = Flask(__name__, template_folder='templates')

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "certificates"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        file = request.files['file']
        template = request.files['template']

        if file.filename == '' or template.filename == '':
            return "Please upload both CSV and Template!"

        y = int(request.form['y'])  # only Y needed (X auto center)

        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        template_path = os.path.join(UPLOAD_FOLDER, template.filename)

        file.save(file_path)
        template.save(template_path)

        # Clear old certificates
        for f in os.listdir(OUTPUT_FOLDER):
            os.remove(os.path.join(OUTPUT_FOLDER, f))

        df = pd.read_csv(file_path)

        if 'Name' not in df.columns:
            return "CSV must contain 'Name' column!"

        for i, row in df.iterrows():
            name = str(row['Name'])

            img = Image.open(template_path)
            draw = ImageDraw.Draw(img)

            # Try large font (better look)
            try:
                font = ImageFont.truetype("arial.ttf", 80)
            except:
                font = ImageFont.load_default()

            # CENTER ALIGN TEXT 🔥
            text_bbox = draw.textbbox((0, 0), name, font=font)
            text_width = text_bbox[2] - text_bbox[0]

            img_width, img_height = img.size
            x = (img_width - text_width) // 2

            draw.text((x, y), name, fill="black", font=font)

            output_path = f"{OUTPUT_FOLDER}/{name}.png"
            img.save(output_path)

        # Create ZIP inside output folder (avoid reload bug)
        zip_path = os.path.join(OUTPUT_FOLDER, "certificates.zip")

        with zipfile.ZipFile(zip_path, 'w') as zipf:
            for file in os.listdir(OUTPUT_FOLDER):
                if file.endswith(".png"):
                    zipf.write(os.path.join(OUTPUT_FOLDER, file), file)

        return send_file(zip_path, as_attachment=True)

    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)