'''
Given a list of contacts which exist in a phone directory. The task is to implement search query for the
phone directory. The search query on a string 'str' displays all the contacts which prefix as 'str'. 
One special property of the search function is that, when a user searches for a contact from the contact 
list then suggestions (Contacts with prefix as the string entered so for) are shown after user enters 
each character.

Note : Contacts in the list consist of only lower case alphabets.

Example:

Input : contacts [] = {“gforgeeks” , “geeksquiz” }
        Query String = “gekk”

Output : Suggestions based on "g" are 
         geeksquiz
         gforgeeks

         Suggestions based on "ge" are 
         geeksquiz

         No Results Found for "gek" 

         No Results Found for "gekk" 
'''
from trie import Trie, charToIndex

class Contact:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __repr__(self):
        return f"{self.name}:{self.number}"

class PhoneDirectory:
    def __init__(self, contacts):
        self.trie = Trie(26)
        self.lastNodes = []
        self.currentNode = self.trie.root
        for contact in contacts:
            self.trie.insertWithData(contact.name, contact)

    def onEnterChar(self, c):
        index = charToIndex(c)
        if self.currentNode.children[index] is None:
            return []
        self.currentNode = self.currentNode.children[index]
        self.lastNodes.append(self.currentNode)
        return self.displayContacts(self.currentNode)

    def onDeleteChar(self):
        if len(self.lastNodes) == 0:
            return []
        self.lastNodes.pop()
        if len(self.lastNodes) == 0:
            return []
        self.currentNode = self.lastNodes[-1]
        return self.displayContacts(self.currentNode)

    def displayContactsUtil(self, node, result):
        if node.data:
            result.append(node.data)
        for i in range(len(node.children)):
            if node.children[i] is not None:
                self.displayContactsUtil(node.children[i], result)

    def displayContacts(self, node):
        result = []
        self.displayContactsUtil(node, result)
        return result

contacts = [
    Contact("vasu", 9555656686),
    Contact("arpit", 9819693488),
    Contact("sachi", 9650094684), 
    Contact("arjit", 8076110958),
    Contact("atulya", 9879879871), 
    Contact("tumul", 9976545309), 
    Contact("punchun", 8765430813), 
    Contact("mickey", 8604531399), 
    Contact("archit", 8419034703),
    Contact("chhotu", 7666588221), 
    Contact("haily", 8076110958),
    Contact("arshit", 9910302232)
]

def printS(a):
    for c in a:
        print(c)
    print()

phoneDirectory = PhoneDirectory(contacts)
printS(phoneDirectory.onEnterChar('a'))
printS(phoneDirectory.onEnterChar('r'))
printS(phoneDirectory.onEnterChar('c'))
printS(phoneDirectory.onDeleteChar())
printS(phoneDirectory.onDeleteChar())
printS(phoneDirectory.onDeleteChar())


