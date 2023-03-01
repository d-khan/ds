#!/usr/bin/env python
# coding: utf-8

# # Hash Tables
# 
# As discussed in Chapter 2 that under the worst-case scenario, the linear search in an unordered array has an efficiency of $O(N)$, whereas the binary search in an ordered array has an efficiency of $O(log N)$. For example, a linear search in an unordered array of 1000 elements would take 1000 steps, and the binary search in an ordered array would take 10 steps. Compared to the linear search, binary search works 100 times faster; however, keeping arrays in order would be a demanding job where random values are inserted frequently in an array[^note1].
# 
# This chapter will explore another data structure called __hash tables__, which can search data in just $O(1)$ time[^note2].
# 
# ## What are Hash Tables?
# Hash tables, also known as hash map, dictionary, or associative array, is a dictionary-like data structure that consists of a key-value pair. Given a key, you can store values and, when needed can, retrieve the value back using its key. In other words, a hash table is a list of paired values. {numref}`hashtable` shows a two-column table where the first column is the key and the second is a corresponding value. 
# 
# ```{list-table} Patient medical record number
# :header-rows: 1
# :name: hashtable
# 
# * - Record number
#   - Patient name
# * - 555223
#   - John Smith
# * - 555980
#   - Sarah Connor
# * - 555000
#   - Issac Newton
# ```
# 
# >__A hash function maps data or keys of arbitrary size to fixed-size values.__
# 
# 
# The following is the implementation of a dictionary in Python and C++.
# 
# ```python
# //Python code
# # dictionary with keys and values of different data types
# record_number = {555223: "John Smith", 555980: "Sarah Connor", 555000: "Albert Einstein"}
# ```
# 
# ```c++
# //C++ code
# #include <iostream>
# #include <map>
# #include <string>
# using namespace std;
# 
# int main()
# {
# map<int, string>MedicalRecord;
# 
# //Adding the elements
# MedicalRecord[555223] = "John Smith";
# MedicalRecord[555980] = "Sarah Connor";
# MedicalRecord[555000] = "Issac Newton";
# 
# //Traversing through the map elements
# for (auto element :MedicalRecord)
# {
#     std::cout<<element.first<<" "<<element.second << endl;  
#     }
# return 0;
# }
# ```
# ## What is hashing and hash functions?
# Hashing is a process of transforming any given key or a string of characters into another value, called a hash value. A hash function can calculate the hash value for a given key.     
# 
# ```{figure} ./images/dict.svg
# :height: 200px
# :name: dictionary
# 
# Hash table
# ```
# I will explain the complicated and mathematically driven hash functions for simplicity's sake.
# 
# Let's continue using the same example described in {numref}`hashtable`. The hash function calculates the hash of a key by adding each number in the key. For example, the hash of the 555223 key will be 5+5+5+2+2+3=22. Similarly, the hash of 555980 and 555000 will be 32 and 15, respectively. Each hashed value corresponds to the memory index where the value is stored.
# 
# ```{figure} ./images/dict2.svg
# :height: 280px
# :name: dictionary2
# 
# Hash table example
# ```
# 
# When a user searches for a value against the key, the hash function calculates the hash of the key, and the resulting hash code is the index of the memory where the value of the key is stored. In the context of big O notation, a search would take $O(1)$. See {numref}`dictionary2`.
# 
# >__Finding any value within the hash table in a single step only works if we know the value’s key. If we tried to find a particular value without knowing its key, the outcome would be searching every key-value pair within the hash table, which is $O(N)$.__
# 
# ### Cryptographic and non-cryptographic functions
# Readers interested in Information Security must have heard of various hash functions such as MD5, SHA1, SHA2, etc. Cryptographic hash functions are a special class among hash functions that aim to provide certain security guarantees that non-cryptographic hash functions do not. For example, when obtaining a device fingerprinting, you should use a cryptographic hash function to have more guarantees of its output uniqueness.
# 
# #### Properties of cryptographic hash functions
# A cryptographic hash function must withstand all known types of cryptanalytic attacks. In theoretical cryptography, the security level of a cryptographic hash function has been defined using the following properties:
# 
# - __Deterministic:__ the same message always results in the same hash.
# - __Pre-image resistance:__ Given a hash value $h$, finding any message $m$ such that $h = hash(m)$ should be difficult. This concept is related to that of a one-way function[^note3]. Functions that lack this property are vulnerable to preimage attacks. For example, using the md5 hash function, the hash code of the "Students" string is aba064f896dc3eb1653c3b68b9548ef1. Reversing the process by inputting the hash code to the hash function to reveal the string should not be acceptable. The following command is compatible with the UNIX-like operating system.
# ```
# echo -n "Students" | md5
# ```
# - __Avalanche effect:__ a small change to a message (even if 1 is flipped) should change the hash value significantly so that the new hash value appears uncorrelated with the old hash value. For example, changing the string "Students" to "students" gives 75d37c6cbf460947005c97e3f12906a9 hash code. Remember that the input to the hash function is case-sensitive.
# 
# - __Collision resistant:__ It should be difficult to find two different messages, $m1$ and $m2$, such that $hash(m1) = hash(m2)$. Such a pair is called a cryptographic hash collision.
# 
# >__Suppose an attacker can control the keys that are used in your dictionary. In that case, they might be able to insert hundreds or thousands of colliding keys, making insert operations very slow. In some cases, this could cause a machine to become unresponsive or a database to become unusable -- a denial of service attack.__
# 
# >__Hash is not encryption. A hash function is a one-way function. Encryption, on the other hand, is known as a two-way function.__
# 
# On the other hand, non-cryptographic hash functions provide weaker guarantees in exchange for performance improvements. 
# 
# ## Collision resolution
# The hash function assigns each key to a unique memory cell, but most hash table designs employ an imperfect hash function, which might cause hash collisions where the hash function generates the same index for more than one key. The hash collision is depicted in {numref}`dictionary3`. Using the same example mentioned in {numref}`hashtable`, the new pair of keys (555890) and value is added; however, the hash function generates a hash code that points to the memory index, which already has data.
# 
# ```{figure} ./images/collision.svg
# :height: 280px
# :name: dictionary3
# 
# Hash Collisions
# ```
# 
# Collisions are dealt with two techniques: __open addressing (aka closed hashing)__ and __closed addressing (aka open hashing)__. Open addressing is a method of collision resolution in hash tables. With this method, a hash collision is resolved by probing or searching through alternative locations in the array (the probe sequence) until either the target record is found or an unused array slot is found, which indicates that there is no such key in the table {cite}`Tenanbaum`. Several techniques are based on open addressing, such as Linear Probing, Quadratic Probing, Double Hashing, and Cuckoo Hashing, a few examples.
# 
# >__Open addressing (closed hashing) and closed addressing (open hashing) terms can be confusing.__ 
# 
# Open hashing is a collision avoidance method that uses an array of a linked list to resolve the collision. It is also known as the separate chaining method (each linked list is considered a chain).
# 
# >__The difference between the two schemes is whether collisions are stored outside the table (closed addressing) or if collisions result in storing one of the records at another slot in the table (open addressing).__
# 
# ### Linear probing (Open Addresing)
# Linear probing is an example of open addressing and is one of the strategies used for resolving collisions in hash tables. When the hash function causes a collision by mapping a new key to a cell of the hash table already occupied by another key, linear probing searches the table for the closest following free location and inserts the new key. Lookups are performed similarly by searching the table sequentially, starting at the position given by the hash function, until finding a cell with a matching key or an empty cell.
# 
# #### Search
# To search for a given key $k$, the cells of memory are examined, beginning with the cell at index $h(k)$ (where h is the hash function) and continuing to the adjacent cells h(k) + 1, h(k) + 2, ..., until finding either an empty cell or a cell whose stored key is k. If a cell containing the key is found, the search returns the value from that cell. Otherwise, if an empty cell is found, the key cannot be in the table because it would have been placed in that cell in preference to any later cell that has not been searched.
# 
# #### Insertion
# To insert a key–value pair $(k,v)$ into the table (possibly replacing any existing pair with the same key), the insertion algorithm follows the same sequence of cells that would be followed for a search until finding either an empty cell or a cell whose stored key is $k$. The new key–value pair is then placed into that cell {cite}`collision1`. When the hash function causes a collision by mapping a new key to a cell of the hash table already occupied by another key, linear probing searches the table for the closest following free location and inserts the new key.
# 
# #### Deletion
# It is also possible to remove a key–value pair from the dictionary. However, the delete cannot simply mark the cell as empty. If the delete process mark the cells empty, then the search operation will stop the search when it passes the empty cell. As a result, the search cannot pass thru the empty cell. This problem can be solved by placing a special marker in place of the deleted cell, called a __tombstone__. The tombstone indicates that a cell was once occupied by a key but not any more. A tombstone can be used to store a new key. However, the insertion operation would follow the search operation (as discussed above) to verify that there is no duplicate in the table. However, the new key would be inserted into the first tombstone. However, after a series of intermixed insertion and deletion operations, some slots will contain tombstones. This will tend to lengthen the average distance from a record’s home position to the record itself, beyond where it could be if the tombstones did not exist. A typical database application will first load a collection of records into the hash table and then progress to a phase of intermixed insertions and deletions. After the table is loaded with the initial collection of records, the first few deletions will lengthen the average probe sequence distance for records (it will add tombstones). Over time, the average distance will reach an equilibrium point because insertions will tend to decrease the average distance by filling in tombstone slots{cite}`opendsa`.
# 
# One way of solving this problem is to periodically rehash the table by reinserting all records into a new hash table. Not only will this remove the tombstones, but it also provides an opportunity to place the most frequently accessed records into their home positions.
# 
# >__Record's or key's home position is the original position calculated by the hashing algorithm. The actual key position may be at the original position or at the first empty cell position.__
# 
# 
# ```{figure} ./images/Linear-probing.svg
# :height: 2400px
# :name: linearprobing
# 
# Search, insert and delete operations in linear probing
# ```
# 
# ## Hash table efficiency
# The efficiency of hash table depends on several factors:
# 
# __Type of hash function:__ Let's say you have a hash function that generates limited hash values. Even though you have available memory space, the little hash values will use a specific memory section. As a result, the collision is imminent. A good hash function, therefore, distributes its data across all available memory cells. The more we can spread our data, the fewer collisions we will have.
# 
# __Size of data in the hash table and available memory in the hash table:__ You probably know that a hash table's efficiency increases when the number of collisions decreases. For example, if you want to store only ten elements in a memory size of 1000 cells, the collision probability is 0.01. On the other hand, reserving many cells to store limited data is inefficient in utilizing memory. A good hash table balances, avoiding collisions and not consuming much memory. The researcher suggests for every 7 data elements stored in a hash table; the memory should have ten cells. In other words, the ratio of data to cells is called the load factor, which is 0.7 based on the suggestion. The higher the load factor, the slower the retrieval. With open addressing, the load factor cannot exceed 1 {cite}`Thomas`.
# 
# >__Hashing is an example of a space-time tradeoff[^note4]. If memory is infinite, the entire key can be used directly as an index to locate its value with a single memory access. On the other hand, if the time is infinite, values can be stored without regard for their keys, and a binary or linear search can be used to retrieve the element.__
# 
# ## Limitations and applications of hashing
# 
# - Hashing is not suitable for applications where multiple records with the same key value are permitted.
# - Hashing is not a suitable method for answering range searches. In other words, we cannot easily find all records (if any) whose key values fall within a specific range. Nor can we quickly find the record with the minimum or maximum key value or visit the records in key order. 
# - Hashing would be an excellent choice if implemented correctly, where all search is done by exact-match queries.
# - Hashing is suitable for both in-memory and disk-based searching and is one of the two most widely used methods for organizing large databases stored on disk (the other one is the B-tree).
# 
# >__The time complexity of hash tables under the best-case scenario is $O(1)$; however, under the worst-case scenario, the time complexity is $O(N)$.__
# 
# 
# ## Conclusion
# Hash tables, when implemented correctly, can deliver O(1) performance. Hash tables are used when data is organized in key-value pairs. The collisions can be rectified by open and closed addressing. In this chapter, we covered closed addressing. There is no need to use a hash function when the time complexity reaches O(N) since computing hash values is an extra burden to the processor.
# 
# 
# 
# [^note1]:A sorting algorithm is needed when random values are inserted in the array. A special case, where sorting would not be needed, if values are generated sequentially and added at the end of the array.
# 
# [^note2]:Average time complexity of hash table is $O(1)$. However, if hash function has some weaknesses which leads to hash collisions, then the time complexity will change to $O(n)$. This is discussed further in the chapter.
# 
# [^note3]:In computer science, a one-way hash function is designed in such a way that it is hard to reverse the process, that is, to find a string that hashes to a given value (hence the name one-way).
# 
# [^note4]:A space–time trade-off, also known as time–memory trade-off or the algorithmic space-time continuum in computer science is a case where an algorithm or program trades increased space usage with decreased time. Here, space refers to the data storage consumed in performing a given task (RAM, HDD, etc), and time refers to the time consumed in performing a given task (computation time or response time).
# 
# ## Bibliography
# ```{bibliography}
# 
# ```
# 
