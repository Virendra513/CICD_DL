from transformers import TrainingArguments, Trainer, AutoTokenizer, AutoModelForSeq2SeqLM, DataCollatorForSeq2Seq
from datasets import load_from_disk, load_from_disk, Da
import torch
import os
from src.projectDL_1.entity.config_entity import ModelTrainerConfig
class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    def train(self):
        device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {device}")

        tokenizer = AutoTokenizer.from_pretrained(self.config.model_ckpt)
        model_pegasus = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_ckpt).to(device)
        seq2seq_data_collator = DataCollatorForSeq2Seq(tokenizer, model=model_pegasus)

        # loading data
        dataset_samsum_pt = load_from_disk(self.config.data_path)

        trainer_args = TrainingArguments(
            output_dir=self.config.root_dir,
            per_device_train_batch_size=self.config.per_device_train_batch_size,
            num_train_epochs=self.config.num_train_epochs,
            warmup_steps=self.config.warmup_steps,
            weight_decay=self.config.weight_decay,
            logging_steps=self.config.logging_steps,
            evaluation_strategy=self.config.evaluation_strategy,
            eval_steps=self.config.eval_steps,
            save_steps=self.config.save_steps,
            gradient_accumulation_steps=self.config.gradient_accumulation_steps
        )

        trainer = Trainer(
            model = model_pegasus,
            args = trainer_args,
            tokenizer = tokenizer,
            train_dataset = dataset_samsum_pt["test"],
            eval_dataset = dataset_samsum_pt["validation"],
            data_collator = seq2seq_data_collator
        )

        trainer.train()

        # saving the trained model
        model_pegasus.save_pretrained(os.path.join(self.config.root_dir, "pegasus_samsum_model"))
        # Save tokenizer
        tokenizer.save_pretrained(os.path.join(self.config.root_dir, "tokenizer"))
