import random
def main():
  die_rolls = 2
  sum = 0
  for i in range(0,die_rolls):
    roll = random.randint(1,6)
    print(f'You rolled a {roll}')
    sum += roll
  print(f'Sum of rolls {sum}')

if __name__== "__main__":
  main()