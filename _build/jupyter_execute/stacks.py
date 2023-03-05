#!/usr/bin/env python
# coding: utf-8

# # Stacks and Queues
# 
# This chapter will discuss two data structures; stacks and queues. These data structures are based on arrays data structure, but unlike conventional arrays, there are restrictions on insertion, deletion, and reading items on the arrays.
# 
# Stacks and queues are dynamic arrays in which the element removed from the array by the delete operation is predetermined. In a stack, the element deletion from the array is the one most recently inserted. The stack implements a last-in, first-out, or LIFO policy. Similarly, in a queue, the element deleted is always the one that has been in the array for the longest time. The queue implements a first-in, first-out, or FIFO policy. There are several ways to implement stacks and queues on a computer. This chapter will use a simple array to implement each.
# 
# ## Stacks
# 
# The stacks are implemented on arrays; however, there are a few constraints:
# 
# - Elements are inserted only at the end of a stack, also called push operation
# - Elements are deleted only from the end of a stack, also called pop operation
# - Reading operation is executed from the end of a stack.
# 
# Think of a stack as a pile of plates stored, where adding and taking out plates from the pile occurs at the top of the stacks.
# 
# The insert operation on a stack is often called PUSH, and the delete operation, which does not take an element argument, is often called POP.
# 
# Programming languages don't have stack data types but can be built using the array data type. Stack is an example of an abstract data type.
# 
# > __*Abstract data type*—it’s a kind of data structure that is a set of theoretical rules that revolve around some other built-in data structure.__
# 
# {numref}`stack-operations` shows the number of operations can be done on a stack.
# 
# ```{list-table} List of operations on a stack
# :header-rows: 1
# :name: stack-operations
# 
# * - Operation
#   - Description
# * - push()
#   - adds an element to the top of the stack
# * - pop()
#   - removes an element from the top of the stack 
# * - peek()
#   - returns a copy of the element on the top of the stack without removing it
# * - is_empty()
#   - checks whether a stack is empty 
# * - is_full()
#   - checks whether a stack is at maximum capacity when stored in a static (fixed-size) structure
# ```
# 
# {numref}`stacks` shows, we can implement a stack of at most $n$ elements with an array $S[1..n]$. The array has an attribute $S.top$ that indexes the most recently inserted element. The stack consists of $S[1..S.top]$, where $S[1]$ is the element at the bottom of the stack and $S[S.top]$ is the element at the top.
# 
# When $S.top=0$, the stack contains no elements and is ***empty***. We can test to see whether the stack is empty by query operations STACK-EMPTY or calling a function ```is_empty()```. If we attempt to pop an empty stack, we say the stack ***underflow***. If $S.top$ exceeds $n$, the stack ***overflows***.
# 
# ```{figure} ./images/stacks.svg
# :height: 500
# :name: stacks
# 
# An array implementation of a Stack $S$. Stack elements appear only in the white color box positions. The green color box represents available space in an array. (a) Stack $S$ has 4 elements. The top element is 9. (b) Stack $S$ after the calls PUSH(S,17) and PUSH(S,3). (c) Stack $S$ after the call POP(S) has returned the element 3, which is the one most recently pushed. Although element 3 still appears in the array, it is no longer in the stack; the top is element 17.
# ```
# The following is the pseudocode implementation of stack, without stack overflow.
# 
# ```{code-block} python
# ---
# name: code_linenumbers
# linenos: True
# caption: |
#     Pseudocode of STACK-EMPTY(S)
# ---
# if S.top == 0
#     return TRUE
# else return FALSE
# ```
# 
# ```{code-block} python
# ---
# name: code_linenumbers
# linenos: True
# caption: |
#     Pseudocode of PUSH(S,x)
# ---
# S.top = S.top + 1
# S[S.top] = x
# ```
# 
# ```{code-block} python
# ---
# name: code_linenumbers
# linenos: True
# caption: Pseudocode of POP(S)
# ---
# if STACK-EMPTY(S)
#     error "underflow"
# else S.top = S.top-1
#     return S[S.top + 1]
# ```
# 
# >__The three stack operations takes $O(1)$ time.__
# 
# ## Queues
# In queues, we call the insert operation on a queue "enqueue", and the delete operation "dequeue". Similar to the POP operation in stack, dequeue takes no element argument. The FIFO property of a queue causes it to operate like a line of customers waiting to pay a cashier. The queue has a ***head*** and a ***tail***. When an element is enqueued, it takes its place at the tail of the queue, just as a newly arriving customer takes a place at the end of the line. The element dequeued is always the one at the head of the queue, like the customer at the head of the line who has waited the longest.
# 
# The {numref}`queues` shows one way to implement a queue of at most $n-1$ elements using an array $Q[1..n]$. The queue has an attribute $Q.head$ that indexes, or point to, its head. The attribute $Q.tail$ indexes the next location at which a newly arrived element will be inserted into the queue. THe elements in the queue reside in locations $Q.head, Q.head+1...,Q.tail-1$, where we "wrap around" in the sense that location 1 immediately follows location $n$ in a circular order. When $Q.head = Q.tail$, the queue is empty. Initially, we have $Q.head = Q.tail = 1$. If we attempt to dequeue an element from an empty queue, the queue ***underflows***. When $Q.head = Q.tail + 1$ or both $Q.head = 1$ and $Q.tail = Q.length$, the queue is full, and if we attempt to enqueue an element, then the queue ***overflows***.
# 
# ```{figure} ./images/queues.svg
# :height: 500
# :name: queues
# 
# An queue implementation using an array $Q[1..12]$. Queue elements appear only in the white color box positions. The green color box represents available space in an array. (a) THe queue has 5 elements, in location $Q[7..11]$. (b) THe configuration of the queue after the calls ENQUEUE(Q,17), ENQUEUE(Q,3), and ENQUEUE(Q,5). (c) The configuration of the queue after the call DEQUEUE(Q) returns the key value 15 formerly at the head of the queue. The new head has key 6. 
# ```
# 
# In our procedure ENQUEUE and DEQUEUE, we have omitted the error checking for underflow and overflow. The pseudocode assumes that $n=Q.length$.
# 
# ```{code-block} python
# ---
# name: code_linenumbers
# linenos: True
# caption: |
#     Pseudocode of ENQUEUE(Q,x)
# ---
# Q[Q.tail] = x
# if Q.tail == Q.length
#     Q.tail = 1
# else Q.tail = Q.tail + 1
# ```
# 
# ```{code-block} python
# ---
# name: code_linenumbers
# linenos: True
# caption: |
#     Pseudocode of DEQUEUE(Q)
# ---
# x = Q[Q.head]
# if Q.head == Q.length
#     Q.head = 1
# else Q.head = Q.head + 1
# return x
# ```
# 
# >__The two queues operations takes $O(1)$ time.__
# 
# 
# ## Conclusion
# Stacks are ideal for processing data in LIFO order. Applications of stacks, such as the "undo" function in a word processor and checking errors such as missing parenthesis in a code, are a few examples. Queue process requests based on FIFO order. Queues data structures are implemented on print servers, handling hardware, or real-time system interrupts are a few examples. In this chapter, only basic queues are discussed.
# 
# 
# 
# ## Bibliography
# ```{bibliography}
# 
# ```
# 

# 
