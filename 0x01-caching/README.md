# 0x01. Caching

## Project Overview
This project covers different caching algorithms and their implementation in Python. Caching is a technique used to temporarily store data for faster access. In this project, you will implement various cache replacement policies to manage data in a limited cache space. The cache will be limited to a maximum of four items, following the behavior defined in the provided `BaseCaching` class.

## Learning Objectives
By the end of this project, you should be able to:
- Understand what a caching system is and why it’s used.
- Define and implement various cache replacement policies:
  - FIFO (First-In-First-Out)
  - LIFO (Last-In-First-Out)
  - LRU (Least Recently Used)
  - MRU (Most Recently Used)
  - LFU (Least Frequently Used)
- Understand the limits of a caching system and how it manages memory.

## Requirements
- **Python Version**: Python 3.7
- **OS**: Ubuntu 18.04 LTS
- **Code Style**: All Python files must adhere to `pycodestyle` (version 2.5)
- **File Execution**: All files must be executable
- **Documentation**: Each module, class, and function should be documented with a clear description of its purpose.

## Project Files
The following files will be implemented:
- `base_caching.py`: Contains the `BaseCaching` class, which serves as the parent class for all cache implementations. This class defines:
  - A constant `MAX_ITEMS` to limit cache items to four.
  - An empty dictionary `cache_data` to store cached data.
  - Methods for printing the cache contents and raising errors if `put` or `get` methods are not implemented in child classes.

### Caching Algorithms
Each caching algorithm will be implemented in its own file, inheriting from `BaseCaching`:
1. **FIFO Cache**: Removes the oldest items first.
2. **LIFO Cache**: Removes the newest items first.
3. **LRU Cache**: Removes the least recently accessed items.
4. **MRU Cache**: Removes the most recently accessed items.
5. **LFU Cache**: Removes the least frequently used items.
