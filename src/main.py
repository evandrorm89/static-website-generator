from textnode import TextNode, TextType
from website import copy_static


def main():
    text_node = TextNode(
        "This is some anchor text", TextType.LINK, "https://example.com"
    )

    print(text_node)

    copy_static()


if __name__ == "__main__":
    main()
