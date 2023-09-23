import os

def main():
  print ("Hellow from GitHub Actions!")
  token = os.environ.get ("TEST_SECRET")
  if not token:
    raise RuntimeError ("TEST_SECRET env var is not set!")
  print ("All good! we found our env var")

if __name__ == '__main__':
  main()
