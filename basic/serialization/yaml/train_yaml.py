from dataclasses import dataclass
import yaml


@dataclass
class Person:
    name: str
    age: str


YAML_DATA = """
!!python/object:__main__.Person
name: John Doe
age: 30
"""

# Loading data using yaml.SafeLoader, will fail on !!python/object tag
# print("Using yaml.SafeLoader:")
# loaded_data_safe = yaml.load(yaml_data, Loader=yaml.SafeLoader)
# print(loaded_data_safe)

# Loading data using yaml.FullLoader
print("\nUsing yaml.FullLoader:")
loaded_data_full = yaml.load(YAML_DATA, Loader=yaml.Loader)
print(loaded_data_full)
