#!/usr/bin/env python
# coding: utf-8

# # 3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# # • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
# # • Use insert() to add one new guest to the beginning of your list.
# # • Use insert() to add one new guest to the middle of your list.
# # • Use append() to add one new guest to the end of your list.
# # • Print a new set of invitation messages, one for each person in your list.

# In[18]:


guests = ["narayan hari", "pruthvi chhowala", "vishal jadav"]

print("\nMessege From " + guests[2].title() + " : ")
print("I am So Sorry Bhavik, I have an urgent meeting today at Bengaluru.")

guests[2] = "tarang chhowala"

print("\nGood Morining, " + guests[0].title() + " you are invited for dinner at my home today.")
print("Good Morining, " + guests[1].title() + " you are invited for dinner at my home today.")
print("Good Morining, " + guests[2].title() + " you are invited for dinner at my home today.")


# In[19]:


print("\nMessege From Hotel Manager : ")
print("Sir, I able to arrange more tables for youy guests..")


# In[20]:


guests.insert(0, "vasudev")
guests.insert(2, "madhav")
guests.append("jignesh")


# In[25]:


print("\nPeoples in New List are : ")
print("1. " + guests[0].title())
print("2. " + guests[1].title())
print("3. " + guests[2].title())
print("4. " + guests[3].title())
print("5. " + guests[4].title())
print("6. " + guests[5].title())

