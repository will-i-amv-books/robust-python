from typing import List

def find_author(author_name):
    return

def add_authors_cookbooks(author_name: str, cookbooks: List[str] = []) -> bool:
    author = find_author(author_name)
    if author is None:
        assert False, "Author does not exist"
    else:
        for cookbook in author.get_cookbooks():
            cookbooks.append(cookbook)
        return True
