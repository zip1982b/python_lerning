



class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, character):
        """method that pushes a character on to a stack"""
        self.character = character
        self.stack.append(self.character)
        print("stack = {}".format(self.stack))





    def enqueueCharacter(self, character):
        """method that enqueues a character in the instance variable"""
        self.character = character
        self.queue.append(self.character)
        print("queue = {}".format(self.queue))

        


    def popCharacter(self):
        """ method that pops and returns the character at the top of the stack instance variable"""
        character = self.stack[-1]
        self.stack.pop()
        print('stack = {}'.format(self.stack))
        return character



    def dequeueCharacter(self):
        """ method that dequeues and returns the first character in the queue instance variable"""
        character = self.queue[0]
        self.queue.pop(0)
        print('queue = {}'.format(self.queue))
        return character





def is_palindrome(pali):
    for i in range(len(pali)//2):
        if pali[i] == pali[len(pali)-1-i]:
            continue
        else: return False
    return True





            


