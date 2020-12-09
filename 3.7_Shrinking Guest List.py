#!/usr/bin/env python
# coding: utf-8

# # 3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# # • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# # • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# # • Print a message to each of the two people still on your list, letting them know they’re still invited.
# # • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

# In[18]:


# This is an old 3.6 excercise for better understanding of this proram.

guests = ["narayan hari", "pruthvi chhowala", "vishal jadav"]

print("\nMessege From " + guests[2].title() + " : ")
print("I am So Sorry Bhavik, I have an urgent meeting today at Bengaluru.")

guests[2] = "tarang chhowala"

print("\nGood Morining, " + guests[0].title() + " you are invited for dinner at my home today.")
print("Good Morining, " + guests[1].title() + " you are invited for dinner at my home today.")
print("Good Morining, " + guests[2].title() + " you are invited for dinner at my home today.")

print("\nMessege From Hotel Manager : ")
print("Sir, I able to arrange more tables for youy guests..")

guests.insert(0, "vasudev")
guests.insert(2, "madhav")
guests.append("jignesh")

print("\nPeoples in New List are : ")
print("1. " + guests[0].title())
print("2. " + guests[1].title())
print("3. " + guests[2].title())
print("4. " + guests[3].title())
print("5. " + guests[4].title())
print("6. " + guests[5].title())


# In[19]:


print("\nMessege From Hotel Manager : ")
print("Sorry Sir, Due to Covid-19 you can invite only 2 persons for dionner.")


# In[20]:


guests.pop()
guests.pop()
guests.pop()
guests.pop()


# In[21]:


print(guests)


# In[22]:


print("\nGood Afternoon, " + guests[0].title() + " you are still invited for dinner at my home today.")
print("Good Afternoon, " + guests[1].title() + " you are still invited for dinner at my home today.")


# In[23]:


guests.remove("vasudev")
guests.remove("narayan hari")


# In[24]:


print(guests)
# Finally we got an empty List as per program requirement.

