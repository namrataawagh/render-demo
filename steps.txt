## Steps to Build and Deploy a Student Placement Prediction App

### 1. Train the Model and Save It Using Pickle
- Import necessary libraries: `pandas`, `numpy`, `sklearn`, and `pickle`.
- Load and preprocess the dataset containing student IQ, CGPA, and placement status.
- Train a Logistic Regression model.
- Save the trained model as `placement_model.pkl` using `pickle.dump()`.

### 2. Set Up Project Folder and Flask App
- Create a project folder `render-demo/`.
- Set up a virtual environment:
  ```sh
  python -m venv venv
  source venv/bin/activate  # macOS/Linux
  venv\Scripts\activate  # Windows
  ```
- Create a `.gitignore` file to exclude unnecessary files (e.g., `venv/`, `__pycache__/`, `*.pkl`).
- Place `placement_model.pkl` in the project folder.
- Create a `templates/` folder to store HTML files.
- Build a `Flask` app (`app.py`) to load the model and handle user input.
- Design an HTML interface (`index.html`) for users to enter IQ and CGPA values.

### 3. Run Locally
- Install required libraries:
  ```sh
  pip install flask scikit-learn pandas numpy
  ```
- Create a `requirements.txt` file by running:
  ```sh
  pip freeze > requirements.txt
  ```
- Run the Flask app:
  ```sh
  python app.py
  ```
- Open the browser and visit `http://127.0.0.1:5000` to test the app.

### 4. Create a GitHub Repository
- Initialize a Git repository:
  ```sh
  git init
  git add .
  git commit -m "Initial commit"
  ```
- Create a new GitHub repository and link it:
  ```sh
  git remote add origin <your-github-repo-url>
  git branch -M main
  git push -u origin main
  ```

### 5. Deploy on Render
- Sign in to [Render](https://render.com/) and create a new **Web Service**.
- Connect your GitHub repository.
- Set the **Build Command**: `pip install -r requirements.txt`
- Set the **Start Command**: `gunicorn app:app`
- Click **Deploy**.
- Once deployed, visit the provided Render URL to access your app.

Your Student Placement Prediction app is now live!

