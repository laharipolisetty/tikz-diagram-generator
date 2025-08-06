🖊️ AI-Powered LaTeX TikZ Diagram Generator

An intelligent tool that automatically converts **natural language descriptions** into **publication-ready TikZ code** for LaTeX documents. Designed for **researchers**, **academicians**, and **technical writers**, this project eliminates the hassle of manual TikZ coding and speeds up diagram creation.

 ✨ Features

* 📝 Converts plain English descriptions to TikZ code.
* 🎨 Supports common diagram types: Circle, Rectangle, Triangle, Arrows, Grids, Flowcharts, Trees, and more.
* 🚀 Real-time diagram preview.
* ❌ No API dependency – works completely offline using a Pattern-Based Generator.
* 💡 Clean & responsive UI/UX interface.
* 🖥️ Built with Python (Flask) backend & HTML/CSS/JS frontend.



 📂 Project Structure

tikz-diagram-generator/
├── backend/
│   ├── app.py
│   ├── tikz_generator.py
│   └── requirements.txt
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   │   ├── TikzEditor.jsx
│   │   │   ├── TikzPreview.jsx
│   │   ├── pages/
│   │   │   └── index.jsx
│   │   ├── App.jsx
│   │   └── main.jsx
│   ├── package.json
├── README.md
└── .gitignore


 🛠️ Technologies Used

Python 3.10 (Flask)
HTML5 & CSS3
Vanilla JavaScript (Fetch API)
LaTeX TikZ Package

---

 🖥️ How to Run Locally

 1. Clone the Repository:

```bash
git clone https://github.com/your-username/tikz-diagram-generator.git
cd tikz-diagram-generator/backend
```

 2. Install Dependencies:

```bash
pip install flask flask-cors
```

 3. Run the Backend Server:

```bash
python app.py
```

4. Open Frontend:

Open `frontend/index.html` in your browser.

---

 🧩 Future Enhancements

* [ ] Add complex diagram patterns (UML, ER diagrams, etc.)
* [ ] Real-time LaTeX rendering preview
* [ ] Integration with IBM Watsonx / OpenAI APIs for intelligent auto-generation (Optional)
* [ ] User authentication and diagram history saving.

---

🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

 📄 License

This project is licensed under the **MIT License**.

---

🙌 Acknowledgments

* LaTeX & TikZ Documentation
* IBM Watsonx / OpenAI inspiration for AI-driven diagram generation.


