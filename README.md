# 🎭 AI Face Analyzer

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/OpenCV-4.x-green?style=for-the-badge&logo=opencv&logoColor=white"/>
  <img src="https://img.shields.io/badge/DeepFace-Latest-orange?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge"/>
</p>

<p align="center">
  A real-time facial analysis application powered by <strong>DeepFace</strong> and <strong>OpenCV</strong> that detects and displays <em>age</em>, <em>gender</em>, <em>emotion</em>, and <em>age category</em> live from your webcam feed.
</p>

---

## 📸 Demo

> 📷 The app opens your webcam, detects faces in real time, and overlays a green bounding box with analysis results on each detected face.

```
┌──────────────────────────────────────┐
│  Male | Adult | Age: 27 | Happy      │
│ ┌────────────────────────────────┐   │
│ │                                │   │
│ │         [ Face Area ]          │   │
│ │                                │   │
│ └────────────────────────────────┘   │
└──────────────────────────────────────┘
```

---

## ✨ Features

- 🔍 **Real-time Face Detection** — Uses Haar Cascade classifier for fast, reliable detection
- 🧠 **AI-Powered Analysis** — DeepFace models analyze each detected face
- 🎂 **Age Estimation** — Predicts approximate age with category labels
- 👤 **Gender Detection** — Identifies dominant gender
- 😄 **Emotion Recognition** — Detects emotions: happy, sad, angry, surprised, neutral, and more
- 🏷️ **Age Categories** — Automatically classifies into Child / Teen / Adult / Senior
- ⌨️ **ESC to Quit** — Simple keyboard control to exit

---

## 🧩 Age Categories

| Category | Age Range |
|----------|-----------|
| 👶 Child  | Under 13  |
| 🧒 Teen   | 13 – 19   |
| 🧑 Adult  | 20 – 59   |
| 👴 Senior | 60+       |

---

## 🛠️ Tech Stack

| Library     | Purpose                          |
|-------------|----------------------------------|
| `OpenCV`    | Webcam capture & face detection  |
| `DeepFace`  | Age, gender & emotion analysis   |
| `NumPy`     | Array & image processing support |

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/ai-face-analyzer.git
cd ai-face-analyzer
```

### 2. Create a Virtual Environment (Recommended)

```bash
python -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install opencv-python deepface numpy
```

> **Note:** DeepFace will automatically download required model weights on first run.

---

## 🚀 Usage

```bash
python face_analyzer.py
```

- The webcam window titled **"AI Face Analyzer"** will open.
- Move in front of your camera — detected faces are highlighted with a green box.
- Press **`ESC`** to exit the application.

---

## 📁 Project Structure

```
ai-face-analyzer/
│
├── face_analyzer.py      # Main application script
└── README.md             # Project documentation
```

---

## 🔧 How It Works

```
Webcam Frame
     │
     ▼
Convert to Grayscale
     │
     ▼
Haar Cascade Face Detection
     │
     ▼
Crop Each Face Region
     │
     ▼
DeepFace.analyze()
  ├── Age Estimation
  ├── Gender Detection
  └── Emotion Recognition
     │
     ▼
Overlay Results on Frame
     │
     ▼
Display via cv2.imshow()
```

---

## ⚠️ Known Limitations

- Analysis runs per frame and may cause slight lag — consider adding frame-skipping for performance.
- Accuracy depends on lighting conditions and face angle.
- DeepFace models require an internet connection on first run to download weights.

---

## 📦 Requirements

```
python >= 3.8
opencv-python
deepface
numpy
```

You can also create a `requirements.txt`:

```bash
pip freeze > requirements.txt
```

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add some feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgements

- [DeepFace](https://github.com/serengil/deepface) by Sefik Ilkin Serengil
- [OpenCV](https://opencv.org/) — Open Source Computer Vision Library

---

<p align="center">Made with ❤️ using Python, OpenCV & DeepFace</p>
