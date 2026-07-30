import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_leaf_to_html_div_with_props(self):
        node = LeafNode("div", "Hello, world!", {"class": "my-class"})
        self.assertEqual(node.to_html(), "<div class=my-class>Hello, world!</div>")

    def test_leaf_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_leaf_to_html_div_with_more_than_one_prop(self):
        node = LeafNode(
            "a", "Click me", {"href": "https://example.com", "target": "_blank"}
        )
        self.assertEqual(
            node.to_html(), "<a href=https://example.com target=_blank>Click me</a>"
        )

    def test_repr(self):
        node = LeafNode("div", "This is a leaf node")
        self.assertEqual("LeafNode(div, This is a leaf node, None)", repr(node))


if __name__ == "__main__":
    unittest.main()
