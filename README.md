# 🎶 Markov Chain Text Composer

This project utilizes Markov Chains to generate text based on the content of PDF documents. 
Originally inspired by Kylie Ying's Python course on freeCodeCamp, it has been **adapted** to read and process PDFs, expanding its versatility.

## 🌟 Features

- **PDF Processing**: Extracts text from PDF files to build a Markov Chain model.
- **Text Generation**: Generates new text sequences that mimic the style and structure of the source material.
- **Customizable Output**: Allows users to specify the length and complexity of the generated text.

## 🛠️ Technologies Used

- **Python**: The core programming language for the project.
- **pypdf**: A pure-python PDF library used for extracting text from PDF files.

## 🚀 Getting Started

### 1️⃣ Prerequisites

- Ensure Python is installed on your system.
- Install the `pypdf` library:

  ```bash
  pip install pypdf
  ```

### 2️⃣ Clone the Repository

### 3️⃣ Prepare Your PDF

- Place the PDF file you want to process in the "texts/" directory and provide the relative path to the "reader.py".

### 4️⃣ Run the Composer

## 🧠 How It Works

1. **PDF Text Extraction**: The program uses the `pypdf` library to extract text from the provided PDF file.
2. **Markov Chain Construction**: It constructs a Markov Chain model based on the extracted text, analyzing the frequency and sequence of word occurrences.
3. **Text Generation**: Using the Markov Chain model, the program generates new text that emulates the style and structure of the source material.

## 🎓 Educational Foundation

This project is based on the Python course by Kylie Ying, available on freeCodeCamp. The course provides a comprehensive guide to building a Markov Chain text generator and understanding the underlying algorithms.

- [Learn Python by Building 12 Projects in This 3-Hour Course](https://www.freecodecamp.org/news/learn-how-to-build-12-python-projects-in-one-course/)

## 📸 Screenshot

(coming soon...)

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit pull requests with improvements or bug fixes.

## 📜 License

This project is licensed under the MIT License.
