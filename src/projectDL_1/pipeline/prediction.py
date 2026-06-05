from src.projectDL_1.config.configuration import ConfigurationManager
from transformers import pipeline
from transformers import AutoTokenizer

class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrianed(self.config.model_name)
        gen_kwargs = {"length_penalty": 0.8, "num_beams": 8, "max_length": 128}
        pipe = pipeline("summaization", model=self.conig.model_path, tokenizer=tokenizer)

        print("Dialogue: ", text)
        output  = pipe(text, **gen_kwargs)[0]["summary_text"]
        print("\nModel Summary:")
        print(output)

        return output
    