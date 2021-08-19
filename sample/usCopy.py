import copy

def is_equal_id(id_head, id_tail):
    if id(id_head) == id(id_tail):
        print(True)

    else:
        print(False)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = left

if __name__ == '__main__':
    # ''' introduction '''
    # str_a = 'abc'
    # str_b = str_a
    # print('id(str_a) = %s' % id(str_a))
    # print('id(str_b) = %s' % id(str_b))

    # is_equal_id(str_a, str_b)

    # ''' type of mutable '''
    # list_a = [1,2,3]
    # print('list_a = %s' % list_a)
    # print('id(list_a) = %s' % id(list_a))

    # list_a.append(4)
    # print('list_a = %s' % list_a)
    # print('id(list_a) = %s' % id(list_a))

    # ''' type of inmutable '''
    # str_a = 'abc'
    # print('str_a = %s' % str_a)
    # print('id(str_a) = %s' % id(str_a))

    # str_a = str_a + 'def'

    # print('str_a = %s' % str_a)
    # print('id(str_a) = %s' % id(str_a))
    
    # ''' some variables show same ID '''
    # list_a = [1, 2, 3]
    # list_b = list_a
    
    # list_a.append(4)

    # print('list_a = %s' % list_a)
    # print('list_b = %s' % list_b)
    # print('id(list_a) = %s' % id(list_a))
    # print('id(list_b) = %s' % id(list_b))

    # ''' some variables show other ID '''
    # str_a = 'abc'
    # str_b = str_a
    # str_a = 'def'

    # print('str_a = %s' % str_a)
    # print('str_b = %s' % str_b)
    # print('str_a = %s' % id(str_a))
    # print('str_b = %s' % id(str_b))

    # ''' copy module for sample '''
    # list_a = [1, 2]
    # list_b = copy.copy(list_a)
    # list_a.append(3)

    # print('a = %s' % list_a)
    # print('b = %s' % list_b)
    # print('id(a) = %s' % id(list_a))
    # print('id(b) = %s' % id(list_b))

    # ''' difference between copy and deepcopy '''
    # ''' type of copy '''
    # list_a = [[1, 2], [3, 4]]
    # list_b = copy.copy(list_a)
    # list_a[1].append(5)

    # print('list_a = %s' % list_a)
    # print('list_b = %s' % list_b)
    # print('id(list_a) = %s' % id(list_a))
    # print('id(list_b) = %s' % id(list_b))

    # for i in range(2):
    #     print('id(a[%i]) = %s' % (i, id(list_a[i])))
    #     print('id(b[%i]) = %s' % (i, id(list_b[i])))

    # ''' type of deepcopy '''
    # a = [[1, 2], [3, 4]]
    # b = copy.deepcopy(a) #変更行
    # a[1].append(5)

    # print ("a = %s" % a)
    # print ("b = %s" % b)

    # print ("id(a) = %i" % id(a))
    # print ("id(b) = %i" % id(b))

    # print ("id(a[0]) = %i" % id(a[0]))
    # print ("id(b[0]) = %i" % id(b[0]))

    # print ("id(a[1]) = %i" % id(a[1]))
    # print ("id(b[1]) = %i" % id(b[1]))

    ''' direct '''
    # shallow|
    # c -> b | -> a
    print("direct")
    a = Node(123)
    b = Node(456, a)
    c = b
    c.left.value = 789
    print("c.left.value =", c.left.value)
    print("b.left.value =", b.left.value)

    print("copy")
    a = Node(123)
    b = Node(456, a)
    c = copy.copy(b)
    c.left.value = 789
    print("c.left.value =", c.left.value)
    print("b.left.value =", b.left.value)

    print("deepcopy")
    a = Node(123)
    b = Node(456, a)
    c = copy.deepcopy(b)
    c.left.value = 789
    print("c.left.value =", c.left.value)
    print("b.left.value =", b.left.value)

