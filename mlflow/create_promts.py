import mlflow
import mlflow.genai

mlflow.set_tracking_uri("http://localhost:5000")

mlflow.genai.register_prompt(
    name="sentiment-classifier",
    template="Определи тональность текста: {{text}}\nОтвет (позитивный/негативный/нейтральный):",
    commit_message="Version 1 - basic",
)

mlflow.genai.register_prompt(
    name="sentiment-classifier",
    template="Ты аналитик текста. Определи тональность: {{text}}\nОтвет строго одним словом:",
    commit_message="Version 2 - with role",
)

mlflow.genai.register_prompt(
    name="sentiment-classifier",
    template='Текст: {{text}}\nВерни JSON: {"sentiment": "positive|negative|neutral"}',
    commit_message="Version 3 - JSON output",
)

mlflow.genai.register_prompt(
    name="text-summarizer",
    template="Кратко изложи текст в 2-3 предложениях:\n\n{{text}}",
    commit_message="Version 1 - basic",
)

mlflow.genai.register_prompt(
    name="text-summarizer",
    template="Ты редактор. Создай резюме не более 3 предложений:\n\n{{text}}\n\nРезюме:",
    commit_message="Version 2 - with constraints",
)

print("Done!")