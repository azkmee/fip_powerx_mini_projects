

def mergesort(array, byfunc=None):
  pass

class Stack:
  def __init__(self):
        self.__items = []
        
  def push(self, item):
      self.__items.append(item)
      pass

  def pop(self):
      if self.is_empty:
          return None
      else:
          return self.__items.pop()
      pass

  def peek(self):
      return self.__items[-1]
      pass

  @property
  def is_empty(self):
      return len(self.__items) == 0
      pass

  @property
  def size(self):
      return len(self.__items)
      pass


class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    self.expr = string if self.is_valid_string(string) else ''

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    self.expr = new_expr if self.is_valid_string(new_expr) else ''
  
  def is_valid_string(self, string):
    for char in string:
      if char not in self.valid_char:
        return False
    return True

  def is_operator(self, string):
    operators = '+-*/()'
    return string in operators

  def is_parenthesis(self, string):
    return string == '(' or string == ')'

  def insert_space(self):
    new_expr = ''
    for char in self.expr:
      # Throw out existing spaces in expression
      if char == ' ':
        continue
      # Add spaces next to operators
      if self.is_operator(char):
        new_expr += f" {char} "
      # Keep operands as-is
      else:
        new_expr += char
    return new_expr

  def process_operator(self, operand_stack, operator_stack):
    while not operator_stack.is_empty:
      op1 = int(operand_stack.pop())
      op2 = int(operand_stack.pop())
      operator = operator_stack.pop()
      if operator == '+':
        operand_stack.push(op2 + op1)
      elif operator == '-':
        operand_stack.push(op2 - op1)
      elif operator == '*':
        operand_stack.push(op2 * op1)
      elif operator == '/':
        operand_stack.push(op2 // op1)

  def evaluate(self):
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    
    for char in tokens:
      operator_substack = Stack()
      temp_arr = []
      if not self.is_operator(char) and char != ' ':
        operand_stack.push(char)
      elif char == '+' or char == '-':
        # Get all operators in stack before the first '(' or ')' operator
        while not operator_stack.is_empty and not self.is_parenthesis(operator_stack.peek()):
          temp_arr.append(operator_stack.pop())
        while len(temp_arr) != 0:
            operator_substack.push(temp_arr.pop())
        # Process all operators in operator substack
        self.process_operator(operand_stack, operator_substack)
        operator_stack.push(char)
      elif char == '*' or char == '/':
        # Get all operators at top of stack which are '*' or '/'
        if not operator_stack.is_empty:
          operator_substack = Stack()
          while operator_stack.peek() == '*' or operator_stack.peek() == '/':
            temp_arr.append(operator_stack.pop())
          while len(temp_arr) != 0:
            operator_substack.push(temp_arr.pop())
          # Process all operators in operator substack
          self.process_operator(operand_stack, operator_substack)
        operator_stack.push(char)
      elif char == '(':
        operator_stack.push(char)
      elif char == ')':
        # Get all operators in stack before the first '(' operator
        if not operator_stack.is_empty:
          operator_substack = Stack()
          while not operator_stack.peek() == '(':
            temp_arr.append(operator_stack.pop())
          while len(temp_arr) != 0:
            operator_substack.push(temp_arr.pop())
          if operator_stack.peek() == '(':
            operator_stack.pop()
          self.process_operator(operand_stack, operator_substack)

    while not operator_stack.is_empty:
      self.process_operator(operand_stack, operator_stack)
    
    result = operand_stack.pop()
    return int(result)


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





