# python3

class Query:
    def __init__(self, query):
        self.type = query[0].strip()
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2].strip()

def process_queries():
  output = []
  phonebook = dict()

  n = int(input())
  for i in range(n):
    query = Query(input().split())

    if query.type == "add":
      phonebook[query.number] = query.name
    elif query.type == "del":
      # pop() will throw an exception if the second parameter is not provided
      phonebook.pop(query.number, None)
    elif query.type == "find":
        number_or_fail_msg = phonebook.get(query.number, "not found")
        output.append(number_or_fail_msg)

  return output

if __name__ == '__main__':
  output = process_queries()
  print("\n".join(output))
