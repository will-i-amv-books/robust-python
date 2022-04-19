from typing import Union, TypeVar, Generic, Tuple, List
from collections import defaultdict


Ingredient = Tuple[str, int, str]
Recipe = Tuple[Union[int, Ingredient]]
Cookbook = Tuple[str, int]

Node = TypeVar("Node")
Edge = TypeVar("Edge")


class Graph(Generic[Node, Edge]):
    def __init__(self):
        self.edges: dict[Node, List[Edge]] = defaultdict(List)

    def add_relation(self, node: Node, to: Edge):
        self.edges[node].append(to)

    def get_relations(self, node: Node) -> List[Edge]:
        return self.edges[node]


recipes: Graph[Recipe, Recipe] = Graph()
cookbook_recipes: Graph[Cookbook, Recipe] = Graph()
cookbooks: Graph[Cookbook, Cookbook] = Graph()

recipes.add_relation(
    (('Pasta Bolognese', 1, 'dish'), ), 
    (('Pasta with Sausage and Basil', 2, 'dish'), )
)
cookbook_recipes.add_relation(
    ('The Food Lab', 1), 
    (('Pasta Bolognese', 3, 'dish'), )
)
cookbooks.add_relation(
    (('Cheeseburger', 3, 'dish'), ), 
    (('Hamburger', 4, 'dish'), )
)
