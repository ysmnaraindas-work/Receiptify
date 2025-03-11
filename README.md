# RECEIPTIFY - OCR-Based Expense Tracking Application

## Project Description
**RECEIPTIFY** is a Streamlit-based application designed to help users track and analyze their expenses effortlessly. Utilizing **OCR (Optical Character Recognition)** technology, this application can scan shopping receipts, convert the extracted data into structured tables, and automatically generate **expense visualizations**.

## Key Features
- **Automatic Receipt Scanning**: Upload receipt images, and the app will extract the relevant data.
- **Data Visualization**: Display expenses based on store, category, and daily trends.
- **Export to Excel**: Download scanned data in Excel format.
- **Google Sheets Integration**: Save expense data directly to Google Drive.
- **SLA Compliance Analysis**: Analyze expenses using statistical methods and AI.

## System Architecture
1. **Upload receipt image** to the application.
2. **OCR Processing** using an AI model to extract and structure the receipt data.
3. **Data Cleansing & Formatting** using Pandas.
4. **Data Visualization** with Plotly and Streamlit.
5. **Save Data** to Google Sheets or export as an Excel file.

## Installation & Running the Application

### 1. Clone the Repository
```bash
git clone https://github.com/username/receiptify.git
cd receiptify
```

### 2. Install Dependencies
Ensure Python and pip are installed, then run:
```bash
pip install -r requirements.txt
```

### 3. Run the Application
```bash
streamlit run app.py
```

## Technologies Used
- **Python** (Streamlit, Pandas, OpenAI, Plotly, PIL)
- **OCR API** (Hugging Face + OpenAI GPT-4 Turbo)
- **Cloud Storage** (Google Sheets API)
- **Visualization** (Plotly, Streamlit Charts)

## Folder Structure
```
receiptify/
│── app.py          # Main Streamlit application
│── home.py         # Home page
│── program.py      # Data analysis and visualization module
│── README.md       # Project documentation
│── requirements.txt # Project dependencies
│── .env            # API Key for OpenAI (if needed)
└── assets/         # Folder for images or additional data
```

## Contributions
We welcome contributions from the community! Feel free to fork this repository and submit a **Pull Request** if you’d like to add features or fix bugs.

## License
This project is licensed under the **MIT License**.

## Contact & Portfolio
If you have any questions or would like to connect, please reach out:
- 📧 Email: [ysmnaraindas.work@gmail.com](mailto:ysmnaraindas.work@gmail.com)
- 💼 LinkedIn: [linkedin.com/in/yasminenaraindas-setiadi](https://linkedin.com/in/yasminenaraindas-setiadi/)

---
⭐ **Don't forget to give this repository a star if you find it useful!**

