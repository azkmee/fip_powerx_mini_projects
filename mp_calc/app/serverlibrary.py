def merge(array, p, q, r, byfunc):
    left_arr = array[p:q+1]
    right_arr = array[q+1:r+1]
    
    temp_arr = []
    while(len(left_arr) and len(right_arr) > 0):
        # compare first index if smaller
        # append to temp_arr
        # remove from left\right arr
        if byfunc == None:
            if (left_arr[0] < right_arr[0]):
                temp_arr += [left_arr[0]]
                left_arr = left_arr[1:]
            else:
                temp_arr += [right_arr[0]]
                right_arr = right_arr[1:]
        else:
            if (byfunc(left_arr[0]) < byfunc(right_arr[0])):
                temp_arr += [left_arr[0]]
                left_arr = left_arr[1:]
            else:
                temp_arr += [right_arr[0]]
                right_arr = right_arr[1:]
        
    if len(left_arr) > 0:
        for left_ in range(len(left_arr)):
            temp_arr += [left_arr[left_]]
            # append remaining left_arr into temp
    else :
        for right_ in range(len(right_arr)):
            temp_arr += [right_arr[right_]]
        # append remaining right_arr into temp
    
    array[p:r+1] = temp_arr
    # print(array)

def mergesort_recursive(array, p, r, byfunc):

    if(len(array[p:r+1]) <=1 ): #if 2 element or lesser, dont split
        pass
        
    else:
        ## if more than 2 elements
        ## split into half
        q = len(array[p:r])//2 + p #half index end(inclusive)
        mergesort_recursive(array, p, q, byfunc)
        mergesort_recursive(array, q+1, r, byfunc)
        
        # merge
        merge(array, p, q, r, byfunc)
          
def mergesort(array, byfunc= None):

    mergesort_recursive(array, 0, len(array)-1, byfunc)


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
