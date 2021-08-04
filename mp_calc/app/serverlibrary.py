class Stack:
  pass

class EvaluateExpression:
  pass


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]



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

