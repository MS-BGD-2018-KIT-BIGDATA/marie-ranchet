import unittest


# Given a string and a non-negative int n, return a larger string
# that is n copies of the original string.

def string_times(string, n):
    return n*string

# Given an array of ints, return True if one of the first 4 elements
# in the array is a 9. The array length may be less than 4.
def array_front9(nums):
    if len(nums)<4:
        if 9 in nums:
            return True
    else :
        if 9 in nums[0:3]:
            return True
    return False


# Given a string, return the count of the number of times
# that a substring length 2 appears  in the string and also as
# the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
def last2(string):
    if len(string) < 2:
        return string
    pattern = string[-2:]
    count = 0
    for i in range (0, len(string) - 3):
        if string [i:i+2] == pattern:
            count += 1
    return count


#Write a program that maps a list of words into a list of
#integers representing the lengths of the correponding words.
def length_words(array):
    #utiliser la fonction map, en fait
    return list(map ( lambda x : (len(x)), array))
    # dico = {}
    # for a in array:
    #     dico[a] = len(a)
    # return dico

#write fizbuzz programm
def fizbuzz():
    maxInt = 20
    string = ""
    for i in range (1, maxInt):
        if i%3 == 0 and i%5 == 0:
            string += 'fizbuzz'
        else:
            if i%3 == 0:
                string += 'fiz'
            else:
                if i%5 == 0:
                    string += 'buzz'
                else:
                    string += str(i)
    return string

#Write a function that takes a number and returns a list of its digits.
def number2digits(number):
  return [int(x) for x in str(number)]

#Write function that translates a text to Pig Latin and back.
#English is translated to Pig Latin by taking the first letter of every word,
#moving it to the end of the word and adding 'ay'
def pigLatin(text):
    # utiliser qqch comme ca : ' '.join ([x[1:]+x[0]+'ay' for x in text.split(' ')])
    string = ""
    count = 1
    for wd in text.lower().split(" "):
        if count == 1:
            string = wd[1:].capitalize() + wd[0] + "ay "
        else :
            string = string + wd[1:] + wd[0] + "ay "
        count += 1
    return string[:-1] # to remove the last space

#Write a proramm that returna dictionary of occurences of the alphabet for a given string.
# Test it with the Lorem upsuj
#"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
def occurences(text):
    # result ={}
    # [result[i] += 1 if i in result else result[i] = 1 for i in text]
    dico = {}
    for a in text:
        if a not in dico:
            dico[a] = 1
        else:
            dico[a] += 1
    return dico

# Here's our "unit tests".
class Lesson1Tests(unittest.TestCase):
    print(fizbuzz())
    def testArrayFront9(self):
        self.assertEqual(array_front9([1, 2, 9, 3, 4]) , True)
        self.assertEqual(array_front9([1, 2, 3, 4, 9]) , False)
        self.assertEqual(array_front9([1, 2, 3, 4, 5]) , False)

    def testStringTimes(self):
        self.assertEqual(string_times('Hel', 2),'HelHel' )
        self.assertEqual(string_times('Toto', 1),'Toto' )
        self.assertEqual(string_times('P', 4),'PPPP' )

    def testLast2(self):
        self.assertEqual(last2('hixxhi') , 1)
        self.assertEqual(last2('xaxxaxaxx') , 1)
        self.assertEqual(last2('axxxaaxx') , 2)

    def testLengthWord(self):
        self.assertEqual(length_words(['hello','toto']) , [5,4])
        self.assertEqual(length_words(['s','ss','59fk','flkj3']) , [1,2,4,5])

    def testNumber2Digits(self):
        self.assertEqual(number2digits(8849) , [8,8,4,9])
        self.assertEqual(number2digits(4985098) , [4,9,8,5,0,9,8])

    def testPigLatin(self):
        self.assertEqual(pigLatin("The quick brown fox") , "Hetay uickqay rownbay oxfay")



def main():
    unittest.main()

if __name__ == '__main__':
    main()
