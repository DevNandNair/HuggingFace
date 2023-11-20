from transformers import pipeline

class TextAnalysis:
    def __init__(self):
        self.classifier = pipeline(task="text-classification", model="SamLowe/roberta-base-go_emotions", top_k=None)

    def analyze_text(self, sentences):
        return self.classifier(sentences)