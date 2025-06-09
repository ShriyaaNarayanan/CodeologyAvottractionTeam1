# CodeologyAvottractionTeam1
Avottraction uses a modern approach to detect “attraction signals” in text through advanced natural language processing. First, the text is cleaned by removing special characters, expanding contractions, and more so that only meaningful information remains. Then, we fine-tune a DistilBERT model to learn subtle context. By splitting the data carefully, we can accurately measure performance and avoid overfitting. Using the Hugging Face Trainer framework simplifies training and evaluation, and early stopping helps us quit when the model stops improving. Overall, Avottraction is flexible enough to adapt to different fields or integrate into chat systems, showing practical ways to apply text classification.

🗒️ Overview
Tech Areas: Machine Learning, Web Development

Tools / Technologies:

- Machine Learning Model: DistilBERT
- Python
- Hugging Face Transformers
- scikit-learn
- PyTorch, NLTK, and regex for preprocessing
- pandas and numpy for data manipulation
- Web Dev: HTML, CSS
- Data: OpenAI API, Reddit PRAW
