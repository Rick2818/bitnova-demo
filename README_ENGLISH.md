# 🌟 Bitnova AI — Proof of Work  
**Author:** Ricardo Bolaños  

---

## 🧠 Overview

**Bitnova AI** is a digital incubator for Bitcoin savings, designed to empower Salvadoran and Latin American families through accessible financial education, micro‑savings, and AI‑driven guidance.  

This is a **Proof of Work (PoW)** demonstrating the core technical architecture:  
a simple, scalable system that combines a **Python (FastAPI) backend** with an **HTML, CSS, and JavaScript frontend**, connected through a REST API.

---

## 🎯 Project Purpose

This initial version showcases how Bitnova AI can recommend **when and how much to save**, without requiring users to know financial terms or report income.  
The AI automatically suggests an appropriate savings amount based on the user’s **occupation** (e.g., student, homemaker, informal worker) and **local economic context**.

### Inclusive Approach
Unlike traditional finance apps, Bitnova AI removes friction by guiding users with friendly, human conversation:

> 🗣️ “Hi 👋 I’m your savings companion, Bitnova AI. What do you do for work?”  
> Based on your answer, the AI estimates your potential and encourages you to start a realistic savings habit — even from as little as **$0.05 per day.**

---

## ⚙️ Technical Architecture

```
bitnova-ai-proof-of-work/
├── backend/            # Python (FastAPI)
│   ├── app.py          # REST API with savings logic
│   └── requirements.txt
├── frontend/           # HTML, CSS, and JavaScript
│   ├── index.html      # Web interface
│   ├── style.css       # Visual design (modern fintech style)
│   └── script.js       # API connection logic
└── README.md
```

### Backend — Python (FastAPI)
- Endpoint `/api/recommendation` receives user name and occupation.  
- Calculates a suggested savings amount based on socioeconomic segment.  
- Returns a motivational message personalized for the user’s context.

### Frontend — HTML, CSS, JS
- Simple, colorful, and educational interface.  
- No financial input required.  
- The AI accompanies the user step by step.

---

## 🧩 Example Flow

**User:** “I’m a student.”  
**AI Response:**  
> “Perfect 🎓 As a student, I recommend saving $0.10 per day.  
> In one month, you’ll have $3 toward your first goal. Small steps lead to big change!”

---

## 🌍 Key Benefits

✅ **Financial education for everyone** — removes social and technical barriers.  
✅ **Human‑centered design** — kids, teens, and adults can all use it easily.  
✅ **Built for the informal economy** — no budgets or bank accounts required.  
✅ **Scalable** — ready for integration with K1.sv, Blink, Athena, Chivo, and other local partners.  
✅ **Transparent and safe** — Bitnova AI never holds funds or performs trading.  

---

## 🧱 Tech Stack

| Layer | Technology | Purpose |
|-------|-------------|----------|
| Backend | **Python + FastAPI** | Recommendation API |
| Frontend | **HTML, CSS, JavaScript** | User interface |
| Middleware | **CORS** | Communication between backend & frontend |
| Deployment | **Render / Railway / Localhost** | Easy, fast deployment |

---

## 🚀 Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/your_username/bitnova-ai-proof-of-work.git
   cd bitnova-ai-proof-of-work
   ```

2. **Start the backend**
   ```bash
   cd backend
   pip install fastapi uvicorn
   uvicorn app:app --reload
   ```

3. **Open the frontend**
   - Simply open `frontend/index.html` in your browser.

---

## 💡 Next Steps

- Integrate conversational AI (educational mode).  
- Add savings goals and progress tracking.  
- Create dashboards and analytics visualization.  
- Deploy the public version on Render or Vercel.  

---

## 📸 Visual Mockup
![Bitnova AI Mockup](design/mockup-bitnova-ai.png)  
> *Note: This image is temporary and will be replaced with the final design.*

---

## ⚖️ License

This project is released under the **MIT (FOSS)** License.  
> © 2025 Ricardo Bolaños — *Bitnova AI is a protected brand and concept.*  
> The source code may be reused with attribution, but the commercial identity and name remain reserved.

---

## 🤝 Contact

💼 [LinkedIn: Ricardo Bolaños](https://www.linkedin.com/in/ricbol/)  
✉️ **rick28191@gmail.com**  

> *Connect, collaborate, or propose partnerships to help build the future of inclusive Bitcoin savings.*
