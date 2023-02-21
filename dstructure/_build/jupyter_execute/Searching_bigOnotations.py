#!/usr/bin/env python
# coding: utf-8

# # Searching and Big O Notations
# In the last chapter, we discussed that several versions of the code might exist to achieve a task. However, some or just one version of the code may be efficient. Therefore, one of the units to measure the efficiency of a code is to calculate the number of steps required to achieve a desired result. We further explored that in a given data structure, the efficiency of a data structure varies with different operations, such as reading, searching, insertion, and deletion. In this chapter, we dive a little deeper and discuss what other factors can affect the performance of a code.
# 
# ## Organization of data
# Let's extend our discussion about an array data structure. Assume that an array is filled with an integer data type with random elements with no repetition of elements. Let's choose a real-world example - an array data structure filled with the last four digits of an SSN.
# For simplicity reasons, assume that the array data structure is the best choice for storing the number. The figure shows the array with elements stored randomly. The user searches for a particular SSN in an array. The processor starts the search from index 0 and then continues to search until the desired element is found. If the data is the last element (worst-case scenario), the search traverses the entire array's length. Hence, the number of steps in searching a data element of a worst-case scenario would be N, where N is the length of an array. On the contrary, inserting data into an array would require just one step. The new data appends at the end of the array and do not require any element shifting.
# 
# Let's extend the above assumption, but this time, the elements in the array are sorted. So, for example, if value 5245 is searched in an array, the search stops where the value is just greater than 5245; in this example, the search stops at index 4. This search is called a linear search.
# 
# <div class="alert alert-block alert-info">
# Linear search iterates over every element of the array, looking for the search value. The search stops as soon as the element it is iterating over is greater than the search value, since we know that the search value will not be found further within the array. 
# </div>
# 
# ## Test 1

# 
