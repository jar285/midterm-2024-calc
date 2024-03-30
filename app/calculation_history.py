import os
import pandas as pd
from dotenv import load_dotenv
import logging

class CalculationHistory:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.initialize()
        return cls._instance

    def initialize(self):
        load_dotenv()
        self.history_file = os.getenv('HISTORY_FILE_PATH', 'calculation_history.csv')
        self.history_file = os.path.abspath(self.history_file)
        self.history_df = self.load_or_initialize_history()
        logging.info(f"CalculationHistory initialized with history file: {self.history_file}")

    def load_or_initialize_history(self):
        if os.path.exists(self.history_file):
            try:
                self.history_df = pd.read_csv(self.history_file)
                logging.info(f"Calculation history loaded from file. File path: {self.history_file}")
            except pd.errors.EmptyDataError:
                logging.warning(f"Calculation history file is empty. File path: {self.history_file}")
                self.history_df = pd.DataFrame(columns=['Operation', 'Description', 'Result'])
        else:
            logging.info("No existing calculation history found, initializing new history.")
            self.history_df = pd.DataFrame(columns=['Operation', 'Description', 'Result'])
        return self.history_df

    def add_record(self, operation, description, result):
        new_record = {'Operation': operation, 'Description': description, 'Result': result}
        self.history_df = self.history_df.append(new_record, ignore_index=True)
        if len(self.history_df) > 10:
            self.history_df = self.history_df.tail(10)
        self.save_history()
        logging.info(f"Record added: {description} = {result}")

    def save_history(self):
        os.makedirs(os.path.dirname(self.history_file), exist_ok=True)
        self.history_df.to_csv(self.history_file, index=False)
        logging.info(f"Calculation history saved. File path: {self.history_file}")

    def load_history(self):
        try:
            self.history_df = pd.read_csv(self.history_file)
            logging.info(f"Calculation history reloaded. File path: {self.history_file}")
            return True
        except pd.errors.EmptyDataError:
            logging.warning(f"Attempted to reload history, but calculation history file is empty. File path: {self.history_file}")
            return False

    def clear_history(self):
        self.history_df = pd.DataFrame(columns=['Operation', 'Description', 'Result'])
        self.save_history()
        logging.info("Calculation history cleared.")

    def delete_history(self, index):
        try:
            self.history_df = self.history_df.drop(index).reset_index(drop=True)
            self.save_history()
            logging.info(f"Record deleted. Index: {index}")
            return True
        except KeyError:
            logging.warning(f"Attempted to delete record, but index does not exist. Index: {index}")
            return False

    @classmethod
    def _reset_instance_for_testing(cls):
        cls._instance = None
