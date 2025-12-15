from collections import defaultdict

def get_num_words(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    num_words = len(file_contents.split())
  return num_words

def get_num_characters(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    lowered_file_contents = file_contents.lower()

    my_dictionary = defaultdict(int)
    for i in lowered_file_contents:

      my_dictionary[i] += 1

    return my_dictionary

def sort_list(char_dict):
  char_list = []
  
  for char, count in char_dict.items():
    char_list.append({
      "char": char,
      "num" : count
    })

  def sort_on(item):
    return item["num"]
  
  char_list.sort(reverse=True, key=sort_on)
  return char_list
  