#!/usr/bin/env python3
import ipdb ;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")


    # don't remove this line, it's for debugging!
    ipdb.set_trace()

# lib/debug.py

# from  owner_pet import Author, Magazine, Article

# Create authors
author1 = Author("John Doe")
author2 = Author("Jane Smith")

# Create magazines
mag1 = Magazine("Tech Today", "Technology")
mag2 = Magazine("Health Weekly", "Health")

# Create articles
article1 = Article(author1, mag1, "The Future of AI")
article2 = Article(author1, mag2, "Healthy Living Tips")
article3 = Article(author2, mag1, "Tech Innovations")

# Test Author methods
print(author1.articles())  # Should return [article1, article2]
print(author1.magazines())  # Should return [mag1, mag2]
print(author1.topic_areas())  # Should return ["Technology", "Health"]

# Test Magazine methods
print(mag1.articles())  # Should return [article1, article3]
print(mag1.contributors())  # Should return [author1, author2]
print(mag1.article_titles())  # Should return ["The Future of AI", "Tech Innovations"]
print(mag1.contributing_authors())  # Should return []

# Run the script
if __name__ == "__main__":
    import pytest
    pytest.main()

