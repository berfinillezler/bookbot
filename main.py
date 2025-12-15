from stats import get_num_words, get_num_characters, sort_list
import sys

if len(sys.argv) != 2:
   print(f"Usage: python3 main.py <path_to_book>")
   sys.exit(1)

def main():
  num_words = get_num_words(sys.argv[1])
  num_chars = get_num_characters(sys.argv[1])
  print(f"Found {num_words} total words")
  sorted_list = sort_list(num_chars)

  for item in sorted_list:
    if not item["char"].isalpha():
       continue
      
    character = item["char"]
    count = item["num"]
    print(f"{character}: {count}")

if __name__ == "__main__":
   main() 
  
