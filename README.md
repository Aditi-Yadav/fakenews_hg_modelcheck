# Fake News Detection Website

This project is a web application that detects fake news using a machine learning model. The application is built with Flask and utilizes the Hugging Face model `jy46604790/Fake-News-Bert-Detect` for text classification but it didnot give expected results, next we tried 'Pulk17/Fake-News-Detection' it works well.

## Project Structure

```
fake-news-detection-website
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── model.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup Instructions

1. **Clone the repository:**

   ```
   git clone <repository-url>
   cd fake-news-detection-website
   ```

2. **Create a virtual environment:**

   ```
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Run the application:**

   ```
   python app/main.py
   ```

2. **Open your web browser and go to:**

   ```
   http://127.0.0.1:5000
   ```

3. **Input text into the form to check if it is fake news or not.**

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
