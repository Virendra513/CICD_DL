import os
from src.projectDL_1 import logger 
from transformers import AutoTokenizer
from datasets import load_dataset, load_from_disk
from src.projectDL_1.config.configuration import ConfigurationManager
from src.projectDL_1.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
        self.tokenizer = AutoTokenizer.from_pretrained(config.tokenizer_name)
    
    def convert_examples_to_features(self, example):
        input_text = example['dialogue']
        target_text = example['summary']

        input_encoding = self.tokenizer(
            input_text,
            max_length=512,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        target_encoding = self.tokenizer(
            target_text,
            max_length=128,
            padding='max_length',
            truncation=True,
            return_tensors='pt'
        )

        return {
            'input_ids': input_encoding['input_ids'].squeeze(),
            'attention_mask': input_encoding['attention_mask'].squeeze(),
            'labels': target_encoding['input_ids'].squeeze()
        }
    
    def convert(self):
        dataset_samsum = load_from_disk(self.config.data_path)
        datset_samsum_pt = dataset_samsum.map(self.convert_examples_to_features, batched=True)
        datset_samsum_pt.save_to_disk(os.path.join(self.config.root_dir, 'samsum_dataset_pt'))