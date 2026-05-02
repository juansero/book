# Artificial Intelligence with Python - Notebooks Repository

This repository accompanies the book **"Artificial Intelligence with Python"** by Juan Sellés. It contains example notebooks extracted and adapted from the content of the book. The original images from the manuscript have not been modified..


## Contents

- `1_EDA.ipynb` — Exploratory Data Analysis (pandas, matplotlib, seaborn): Examples of histograms, boxplots, and heatmaps.
- `2_Regression_Linear.ipynb`' — Linear Regression with scikit-learn (simulated example).
- `3_Classification_Tree.ipynb` — Simple Classification with DecisionTreeClassifier and tree visualization.
- `4_NN_Keras_MLP.ipynb` — Simple Neural Network with TensorFlow/Keras (educational example).
- `5_diffusion_simulation.py` — Educational demo: A step-by-step simulation of how a Diffusion Model removes noise from an image.
- `6_transformers_sentiment.py` — Transformer (Reader): Using the Hugging Face pipeline with the BETO model for sentiment analysis in Spanish.
- `7_chatgpt_api_assistant.py` — Transformer (Writer): Prompt Engineering and API connection to create a personalized ChatGPT assistant (Chef Yoda).
- `8_generative_ai.ipynb` — Overview and extra exercises related to the Generative AI concepts explained in the book.
- `📁 app_streamlit/` — Final Project Folder: Contains train_model.py and app.py to train a model and deploy it as a web application using Streamlit.

## 🚀 How to Use

**For Jupyter Notebooks (`.ipynb` files):**
*   **Recommended:** Open them directly in **Google Colab** (no installation required). You can simply replace `github.com` with `colab.research.google.com/github` in the URL of any notebook file.
*   **Local Environment:** Open them using Jupyter Notebook, JupyterLab, or VS Code.

**For Python Scripts (`.py` files):**
*   Run them directly in your terminal/command prompt: `python nombre_del_archivo.py`
*   To run the web app, navigate to the `app_streamlit/` folder and type: `streamlit run app.py`

## 🛠️ Requirements

If you are running the code locally, ensure you have Python 3.8+ installed. You can install all necessary libraries with a single command:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn tensorflow transformers openai streamlit joblib
```

## 📚 Find the Book / Encuentra el libro
You can purchase the book in **English** or **Spanish** using the following links:

🔗 [English book](https://www.amazon.es/dp/B0GDMKVZBK)

🔗 [Versión en Español](https://www.amazon.es/dp/B0GDMKVZBK)

## License and Attribution

This repository is part of the original book. For reference, see: https://www.amazon.es/dp/B0GDMKVZBK.

If you plan to use the content for commercial purposes, please contact the author to respect rights and conditions.

## Contribuciones

If you'd like to improve the notebooks (add tests, data, or improve visualizations), please open a pull request or an issue in the repository.

