import json
import yaml
import random
from datetime import datetime
from faker import Faker
import allure
class CommonUtils:

    @staticmethod
    def read_json_file(file_path):
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        return data


    @staticmethod
    def read_yaml_file(file_path):
        with open(file_path, 'r') as yaml_file:
            data = yaml.safe_load(yaml_file)
        return data

    @staticmethod
    def convert_to_date(date_string, format="%Y-%m-%d"):
        return datetime.strptime(date_string, format).date()

    @staticmethod
    def generate_random_number(start, end):
        return random.randint(start, end)

    @staticmethod
    def generate_fake_data():
        faker = Faker()
        return {
            "name": faker.name(),
            "email": faker.email(),
            "address": faker.address(),
            "phone": faker.phone_number()
        }

# Example usage:
if __name__ == "__main__":
    json_data = CommonUtils.read_json_file("data.json")
    print("JSON data:", json_data)

    yaml_data = CommonUtils.read_yaml_file("data.yaml")
    print("YAML data:", yaml_data)

    date_string = "2023-08-28"
    converted_date = CommonUtils.convert_to_date(date_string)
    print("Converted date:", converted_date)

    random_number = CommonUtils.generate_random_number(1, 100)
    print("Random number:", random_number)

    fake_data = CommonUtils.generate_fake_data()
    print("Fake data:", fake_data)
